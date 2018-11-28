#include <bits/stdc++.h>
using namespace std;
#define For(i,a,b) for(long long i=a;i<b;i++)
#define reset(a,b) memset(a,b,sizeof(a))
#define mod 1000000007
#define pi acos(-1)
#define eps 0.000001
#define pb push_back

int n,r,p,s,c[3],nex[3],t,N;
string ans[15],ss;

void prog()
{
    For(i,0,n)
    {
        nex[0]=c[0]+c[2];
        nex[1]=c[0]+c[1];
        nex[2]=c[2]+c[1];
        c[0]=nex[0];
        c[1]=nex[1];
        c[2]=nex[2];
    }
}

void solve(int i)
{
    if(i==0) ans[0]="P";
    else if(i==1) ans[0]="R";
    else ans[0]="S";
    For(i,1,1+n)
    {
        ans[i]="";
        for(char c:ans[i-1])
        {
            if(c=='P') ans[i]+="PR";
            else if(c=='R') ans[i]+="RS";
            else ans[i]+="PS";
        }
    }
    ss=ans[n];
    int seg=4;
    For(i,0,n-1)
    {
        for(int st=0;st<N;st+=seg)
        {
            For(i,0,seg/2)
            {
                if(ss[st+i]<ss[st+i+seg/2]) break;
                if(ss[st+i]>ss[st+i+seg/2])
                {
                    For(j,0,seg/2) swap(ss[st+j],ss[st+j+seg/2]);
                    break;
                }
            }
        }
        seg*=2;
    }
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(0);
    cin>>t;
    For(cas,1,1+t)
    {
        cout<<"Case #"<<cas<<": ";
        cin>>n>>r>>p>>s;
        N=r+p+s;
        bool flag=false;
        For(i,0,3)
        {
            reset(c,0);
            c[i]=1;
            prog();
            if(c[0]==p&&c[1]==r&&c[2]==s)
            {
                flag=true;
                solve(i);
                cout<<ss<<endl;
                break;
            }
        }
        if(!flag) cout<<"IMPOSSIBLE"<<endl;
    }
}
