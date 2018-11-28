#include<iostream>
using namespace std ;
void bubble_sort (int arr[], int n)
 {
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n - i - 1; ++j)
      if (arr[j] > arr[j + 1])
     {
        int temp = arr[j];
        arr[j] = arr[j + 1];
        arr[j + 1] = temp;
      }
  }
int main()
{
    int t,x ;
    cin>>t ;
    x=t;
    while(t--)
    {
        int n,i,ans,flag,j,k=0 ;
        cin>>n ;
        int a[n*(2*n-1)];
        for(i=0;i<n*(2*n-1);i++)
        {
            cin>>a[i];
        }
        int arr[n];
         for(i=0;i<n;i++)
        {
            arr[i]=0;
        }
        for(i=0;i<(n*(2*n-1));i++)
        {
            ans=0,flag=0;
            for(j=0;j<(n*(2*n-1));j++)
            {
                //cout<<a[i]<<" "<<a[j]<<endl;
                if(a[j]==a[i])
                {
                    ans++;
                }
            }
            if(ans%2==1)
            {
                for(j=0;j<n;j++)
                {
                    if(a[i]==arr[j])
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                {

                }
                else
                {
                    arr[k]=a[i];
                    k++;
                }

            }
        }
        bubble_sort (arr, n);
        cout<<"Case #"<<x-t<<": " ;
        for(i=0;i<n;i++)
        {
            cout<<arr[i]<<" ";
        }
        cout<<endl;
    }
    return 0 ;
}
