#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    int t;
    long double A[100],B[100],C[100];
    cin>>t;
    FILE *file;
    file=fopen("war1.o","w");
    for(int k=1;k<=t;k++)
    {
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
            cin>>A[i];
        for(int i=0;i<n;i++)
        {
            cin>>B[i];
            C[i]=B[i];
        }
        sort(A,A+n);
        sort(B,B+n);
        sort(C,C+n);
        int posmax=n-1,posmin=0,ans1=0,ans2=0;
        for(int i=0;i<n;i++)
        {
            if(A[i]>B[posmin])
            {
                posmin++;
                ans1++;
            }
        }
        int f=-1;
        for(int i=0;i<n;i++)
        {
           for(int j=f+1;j<n;j++)
           {
               if(C[j]>A[i])
               {
                    ans2++;
                    f=j;break;
               }
           }
        }
        fprintf(file,"Case #%d: %d %d\n",k,ans1,n-ans2);
        //cout<<ans1<<" "<<n-ans2<<endl;

    }

}
