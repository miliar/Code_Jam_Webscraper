//#include <bits/stdc++.h>
//using namespace std;
//typedef long long LL;
//typedef long double LD;
//typedef unsigned long long ULL;
//typedef pair<int, int> PI;
//typedef pair<PI, PI > PII;
//const double eps=1e-5;
//const LL mod=1e9+7;
//const double pi=acos(-1.0);
//const int MAXN=201000;
//const int MAXM=299900;
//const int N=1e6+5;
//int n,m,a[12345];
//int main()
//{
//    int t;
//    cin>>t;
//    while(t--)
//    {
//        cin>>n>>m;
//        for(int i=0;i<m;i++)
//        {
//            scanf("%d",&a[i]);
//        }
//
//    }
//    return 0;
//}

#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair<PI, PI > PII;
const double eps=1e-5;
const int inf=1e5;
const LL mod=1e9+7;
const double pi=acos(-1.0);
const int N=1e3+5;
string s;
int n;
struct node{
    string s;
    int step;
};
int Check(node x)
{
    for(int i=0;x.s[i];++i)
        if(x.s[i]=='-') return 0;
    return 1;
}
set<string>st;
int bfs()
{
    st.clear();
    node now;
    now.s=s;now.step=0;
    if(Check(now))
        return 0;
    st.insert(s);
    queue<node>q;
    q.push(now);
    while(!q.empty())
    {
        now=q.front();
        q.pop();

        for(int i=0;i<n;i++)
        {
            node rear=now;
            for(int j=0;j<=i;j++){
                if(now.s[j]=='+'){
                    rear.s[i-j]='-';
                }
                else
                    rear.s[i-j]='+';
            }
            if(st.find(rear.s)!=st.end())
                continue;
            st.insert(rear.s);
            if(Check(rear))
                return now.step+1;
            rear.step=now.step+1;
            q.push(rear);
        }
    }
}
int main()
{
    freopen("C:/Users/Kewowlo/Desktop/1.in","r",stdin);
    freopen("C:/Users/Kewowlo/Desktop/2.out","w",stdout);
    int t,cas=1;
    cin>>t;
    while(t--)
    {
        cin>>s;
        n=s.length();
        printf("Case #%d: ",cas++);
        cout<<bfs()<<endl;
    }
    return 0;
}
/*
+-+-+-++--
*/
