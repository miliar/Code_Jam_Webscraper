#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    int tt=1;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        double A[n];
        double B[n];
        for(int i=0;i<n;i++) cin>>A[i];
        for(int i=0;i<n;i++) cin>>B[i];
        sort(A,A+n);
        sort(B,B+n);
        //for(int i=0;i<n;i++) cout<<A[i]<<" ";
        //cout<<endl;
        //for(int i=0;i<n;i++) cout<<B[i]<<" ";
        //cout<<endl;

        int i1=0,i2=n-1;
      int count_nk1=0;
        for(int i=0;i<n;i++)
        {
            if(A[i]> B[i1])
            {
                count_nk1++;
                i1++;
            }
            else
            {
                i2--;
            }
        }
         int count_nk2=0;
         i1=0,i2=n-1;
         for(int i=n-1;i>=0;i--)
         {
             if(A[i]>B[i2])
             {
                 count_nk2++;
                 i1++;
             }
             else
             {
                 i2--;
             }
         }
         cout<<"Case #"<<tt<<": "<<count_nk1<<" "<<count_nk2<<endl;
         tt++;

    }
}
