#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
ll x,n,ans,c=1,l,r,d,sum,i,t;
bool visited[10];
void solve(ll s)
{
    while(s)
    {
        d=s%10;
        s/=10;
        visited[d]=1;
    }
}
bool valid()
{
    for(int i=0 ; i<=9 ; i++)
        if(!visited[i]) return 0;
    return 1;
}
int main(){
	freopen("A-large.txt", "r", stdin);
	freopen("ALarge.txt", "w", stdout);
    cin>>t;
    while(t--)
    {
        memset(visited,0,sizeof(visited));
        cin>>x;
        cout<<"Case #"<<c++<<":"<<" ";
        if(x==0)    cout<<"INSOMNIA"<<endl;
        else
        {
            i=1;d=x;
            while(!valid())
            {
                sum=x*i;
                solve(sum);
                i++;
            }
            cout<<sum<<endl;
        }
    }
}
