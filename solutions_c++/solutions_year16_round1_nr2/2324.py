#include<bits/stdc++.h>
#define MOD 1000000007
#define MX 100010
#define ll long long
#define sc(n) scanf("%d",&n)
#define pr(m) printf("%d\n",m)
#define pi acos(-1.0)

using namespace std;
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("OutBsmall.txt","w",stdout);
    int t,tc=1,i,j;
    sc(t);
    int arr[5000]= {};
    while(t--)
    {
        int n;
        sc(n);
        int MAX=-1;
        for(j=0; j<n*2-1; j++)
            for(i=0; i<n; i++)
            {
                int x;
                sc(x);
                if(x>MAX) MAX=x;
                arr[x]++;
            }
        cout<<"Case #"<<tc++<<": ";
        for(i=1; i<=MAX; i++)
            if(arr[i]%2==1)
            {
                cout<<i<<" ";
                arr[i]=0;
            }
        cout<<endl;
    }



    return 0;
}
