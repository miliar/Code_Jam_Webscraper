#include<cstdio>
#include<map>
#include<cmath>
#include<cstring>
#include<iostream>
#include<cctype>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const int M=100005;
const LL mod=1e9+7;
const double eps=1e-8;
struct P
{
    string s;
    int stp;
};
string Cal(string s,int n)
{
    int L=0,R=n;
    while(L<R)
    {
        swap(s[L],s[R]);
        s[L]=(s[L]=='+')?'-':'+';
        s[R]=(s[R]=='+')?'-':'+';
        L++;
        R--;
    }
    if(L==R)
        s[L]=(s[L]=='+')?'-':'+';
    return s;
}
bool J(string &s,int &len)
{
    for(int i=0;i<len;i++)
        if(s[i]=='-')
        return false;
    return true;
}
int main()
{
    freopen("test1.in","r",stdin);
    freopen("test2.out","w",stdout);
    int T,kase=1,ans;
    string s;
    scanf("%d",&T);
    while(T--)
    {
        cin>>s;
        map<string,bool> v;
        queue<P> Q;
        P p,q;
        p.s=s,p.stp=0;
        Q.push(p);
        v[s]=true;
        int len=s.size();
        while(!Q.empty())
        {
            p=Q.front();
            //cout<<p.s<<" "<<p.stp<<endl;
            Q.pop();
            if(J(p.s,len))
            {
                ans=p.stp;
                break;
            }
            for(int i=0;i<len;i++)
            {
                string str=Cal(p.s,i);
                //cout<<str<<endl;
                if(v[str]==false)
                {
                    v[str]=true;
                    q.s=str;
                    q.stp=p.stp+1;
                    Q.push(q);
                }
            }
        }
        printf("Case #%d: %d\n",kase++,ans);
    }
    return 0;
}
/*


*/
