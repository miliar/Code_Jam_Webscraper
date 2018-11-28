#include <bits/stdc++.h>
#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MOD 1000000007
#define lli long long int
#define li long int

using namespace std;
int arr[10];
bool check()
{   int i;
    for(i=0;i<10;i++)
        if(arr[i]==0) return false;
    return true;
}
int main()
{   ios_base::sync_with_stdio(false);
    cin.tie(0);
    lli t,n,i,j,num;
    cin>>t;
    for(i=1;i<=t;i++)
    {   cin>>n;
        cout<<"Case #"<<i<<": ";
        if(n==0) cout<<"INSOMNIA";
        else
        {   for(j=0;j<10;j++) arr[j]=0;
            j=1;
            while(!check())
            {   num=j*n;
                while(num>0)
                {   arr[num%10]=1;
                    num/=10;
                }
                j++;
            }
            cout<<(j-1)*n;
        }
        cout<<endl;
    }
    return 0;
}
