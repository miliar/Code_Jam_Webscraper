#include <bits/stdc++.h>
using namespace std;
#define ll          long long
#define MOD         1000000007
#define ll          long long
#define pb          push_back
#define pii         pair<int,int>
#define vi          vector<int>
#define all(a)      (a).begin(),(a).end()
#define F           first
#define S           second
#define endl        '\n'
#define PI          3.14159265359d
#define sz(x)       (int)x.size()
#define INF         INT_MAX
int main()
{
    freopen("C:/Users/User/Desktop/in.txt","r",stdin);
    freopen("C:/Users/User/Desktop/out.txt","w",stdout);
    int i,t,T,k,cur,flip[1005],res;
    string s;
    cin>>T;
    for(t=1;t<=T;t++)
    {
        cin>>s>>k;
        memset(flip,0,sizeof flip);
        for(i=cur=res=0;i<=s.length()-k;i++)
        {
            if(i>=k)
                cur-=flip[i-k];
            if(cur%2)
                s[i]='+'+'-'-s[i];
            if(s[i]=='-')
            {
                cur++;
                res++;
                flip[i]++;
            }
        }
        for(;i<s.length();i++)
        {
            if(i>=k)
                cur-=flip[i-k];
            if(cur%2)
                s[i]='+'+'-'-s[i];
            if(s[i]=='-')
                break;
        }
        cout<<"Case #"<<t<<": ";
        if(i<s.length())
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<res<<endl;
    }
    return 0;
}
