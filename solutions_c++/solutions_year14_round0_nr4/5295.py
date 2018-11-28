#include <iostream>
using namespace std;


void merge(double a[],int l,int h,int m)
{
    int n1=m-l+1;
    int n2=h-m;
    double *a1 = new double[n1];
    double *a2 = new double[n2];
    int q,j,k;
    for(q=0;q<n1;q++)
        a1[q]=a[q+l];
    for(j=0;j<n2;j++)
        a2[j]=a[j+m+1];
        q=l;
        k=0;
        j=0;
    for(q=l;k<n1 && j<n2;q++)
    {
        if(a1[k]>=a2[j])
        {
            a[q]=a2[j];
            j++;
        }
        else
        {
            a[q]=a1[k];
            k++;
        }
    }
        while(k<n1)
        {
            a[q]=a1[k];
            k++;
            q++;
        }

        while(j<n2)
        {
            a[q]=a2[j];
            j++;
            q++;
        }

}
void msort(double a[],int l,int h)
{
    int m;
    if(l<h)
    {
        m=(l+h)/2;
        msort(a,l,m);
        msort(a,m+1,h);
        merge(a,l,h,m);
    }

}



int main()
{
    int t,n,D;
    cin>>t;
    int y,k;
    int q,j;
    for(q=1;q<=t;q++)
    {
      cin>>n;
      int *x=new int[n];
      int j;
      D=0;
      y=0;
      double *a=new double[n];
      double *b=new double[n];
      for(j=0;j<n;j++)
        cin>>a[j];
       for(j=0;j<n;j++)
        cin>>b[j];

        msort(a,0,n-1);
        msort(b,0,n-1);

         for(j=0;j<n;j++)
           x[j]=0;


         for(j=0;j<n;j++)
          {
           for(k=j;k<n;k++)
           {
               if(a[j]<b[k]&&(x[k]==0))
                    {
                      y++;
                      x[k]++;
                      break;
                    }
            }
          }


        for(j=0;j<n;j++)
        x[j]=0;

       for(j=0;j<n;j++)
          {
           for(k=j;k<n;k++)
           {
               if(b[j]<a[k]&&(x[k]==0))
                    {
                      D++;
                      x[k]++;
                      break;
                    }
            }
          }
      cout << "Case #" <<q<<": " <<D<<" "<<(n-y)<<endl;
      delete a;
      delete b;
      delete x;
    }

    return 0;
}

