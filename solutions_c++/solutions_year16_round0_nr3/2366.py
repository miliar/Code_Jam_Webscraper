#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(int i=a;i<b;i++)
#define pb push_back
#define mod 1000000007
#define reset(s,val) memset(s,val,sizeof(s))
#define eps 1e-9
#define pi acos(-1)
#define sqr(x) (x)*(x)
#define two(x) (1<<(x))

long long n,j,lis[22],ans[11],t,p[11][16];

bool test(int b)
{
    long long num = 0;
    For(i,0,16) num+=lis[i]*p[b][i];
    for(long long i=3;i*i<=num;i+=2) if(num%i==0)
    {
        ans[b]=i;
        return true;
    }
    return false;
}

int main( ){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    For(i,2,11)
    {
        p[i][0]=1;
        For(j,1,16) p[i][j]=p[i][j-1]*i;
    }
    ans[10]=ans[4]=3;
    ans[9]=ans[7]=ans[5]=ans[3]=2;
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<":"<<endl;
        cin>>n>>j;
        For(num,1<<15,1<<16) if(num&1&&__builtin_popcount(num)%6==0)
        {
            reset(lis,0);
            For(i,0,16) if((1<<i)&num) lis[i]=1;
            if(test(2)&&test(6)&&test(8))
            {
                j--;
                for(int i=15;i>=0;i--) cout<<lis[i];
                cout<<' ';
                For(i,2,11) cout<<ans[i]<<' ';
                cout<<endl;
            }
            if(!j) break;
        }
    }
}
