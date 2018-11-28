#include <iostream>

using namespace std;




void merge(double arr[],int l,int h,int m);
void merge_sort(double arr[],int l,int h)
{
    int m;
    if(l<h)
    {
        m=(l+h)/2;
        merge_sort(arr,l,m);
        merge_sort(arr,m+1,h);
        merge(arr,l,h,m);
    }

}
void merge(double arr[],int l,int h,int m)
{
    int i,j,k;
    int n1=m-l+1;
    int n2=h-m;
    double *arr1 = new double[n1];
    double *arr2 = new double[n2];
    for(i=0;i<n1;i++)
        arr1[i]=arr[i+l];
    for(j=0;j<n2;j++)
        arr2[j]=arr[j+m+1];
        i=l;
        k=0;
        j=0;
    for(i=l;k<n1 && j<n2;i++)
    {
        if(arr1[k]>=arr2[j])
        {
            arr[i]=arr2[j];
            j++;
        }
        else
        {
            arr[i]=arr1[k];
            k++;
        }
    }
        while(k<n1)
        {
            arr[i]=arr1[k];
            k++;
            i++;
        }

        while(j<n2)
        {
            arr[i]=arr2[j];
            j++;
            i++;
        }

}


int main()
{
    int t,n,x,y,k,i,j;

    cin>>t;
    for(i=1;i<=t;i++)
    {
      cin>>n;
      int *c=new int[n];

      x=0;
      y=0;
      double *a=new double[n];
      double *b=new double[n];
      int j;
      for(j=0;j<n;j++)
        cin>>a[j];
       for(j=0;j<n;j++)
        cin>>b[j];

       // merge_sort(a,0,n-1);
       // merge_sort(b,0,n-1);

         for(j=0;j<n;j++)
           c[j]=0;


         for(j=0;j<n;j++)
          {
           for(k=0;k<n;k++)
           {
               if(a[j]<b[k]&&(c[k]==0))
                    {
                      y++;
                      c[k]++;
                      break;
                    }
            }
          }


        for(j=0;j<n;j++)
        c[j]=0;

       for(j=0;j<n;j++)
          {
           for(k=0;k<n;k++)
           {
               if(b[j]<a[k]&&(c[k]==0))
                    {
                      x++;
                      c[k]++;
                      break;
                    }
            }
          }
      cout << "Case #" <<i<<": " <<x<<" "<<(n-y)<<endl;
      delete a;
      delete b;
      delete c;
    }

    return 0;
}
