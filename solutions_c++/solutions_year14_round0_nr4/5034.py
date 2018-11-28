#include <iostream>


using namespace std;

void mergedharam(double arr[],int l,int h,int m);
void mergesot(double arr[],int l,int h)
{
    int m;
    if(l<h)
    {
        m=(l+h)/2;
        mergesot(arr,l,m);
        mergesot(arr,m+1,h);
        mergedharam(arr,l,h,m);
    }

}
void mergedharam(double arr[],int l,int h,int m)
{
    int n1=m-l+1;
    int n2=h-m;
    double *arr1 = new double[n1];
    double *arr2 = new double[n2];
    int q,j,k;
    for(q=0;q<n1;q++)
        arr1[q]=arr[q+l];
    for(j=0;j<n2;j++)
        arr2[j]=arr[j+m+1];
        q=l;
        k=0;
        j=0;
    for(q=l;k<n1 && j<n2;q++)
    {
        if(arr1[k]>=arr2[j])
        {
            arr[q]=arr2[j];
            j++;
        }
        else
        {
            arr[q]=arr1[k];
            k++;
        }
    }
        while(k<n1)
        {
            arr[q]=arr1[k];
            k++;
            q++;
        }

        while(j<n2)
        {
            arr[q]=arr2[j];
            j++;
            q++;
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

        mergesot(a,0,n-1);
        mergesot(b,0,n-1);

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
