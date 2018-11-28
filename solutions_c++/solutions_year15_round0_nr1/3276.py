#include<iostream>
#include<string>
#include<cstdio>
#include<cstdlib>
using namespace std;
int T,ti;
int n,m,ans;
string s;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin>>T;
    while(T--)
    {
        cout<<"Case #"<<++ti<<": ";
        cin>>n>>s;
        m=0;
        ans=0;
        for(int i=0;i<=n;i++)
        {

            if(m<i && s[i]!='0') {ans+=i-m;m=i;}
            m+=s[i]-'0';
        }
        cout<<ans<<endl;
    }
}
