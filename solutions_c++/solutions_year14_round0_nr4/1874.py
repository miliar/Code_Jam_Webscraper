#include "iostream"
#include "cstdio"
#include "set"
#include "algorithm"
#include "cmath"
using namespace std;

int t,n;
double A[1010],B[1010];
int ans1,ans2;
int main()
{
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    cin>>t;
    for(int  cas=1; cas<=t; cas++)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>n;
        ans1=n;
        ans2=0;
        for(int i=0; i<n; i++)
            cin>>A[i];
        for(int i=0; i<n; i++)
            cin>>B[i];
        sort(A,A+n);
        sort(B,B+n);

        int l=0,r=n-1;
        for(int i=n-1; i>=0; i--)
        {

            if(A[r]>B[i])
            {
                ans2++;
                r--;
            }
            else
                l++;
        }

        for(int i=0; i<n; i++)
        {
            double* temp=upper_bound(B,B+n,A[i]);
            if(temp<B+n)
            {
                *temp=-1;
                sort(B,B+n);
                ans1--;
            }
        }
        cout<<ans2<<" "<<ans1<<endl;
    }
    return 0;
}
