#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef long double LD;
typedef unsigned long long ULL;
typedef pair<int, int> PI;
typedef pair<PI, PI > PII;
const double eps=1e-5;
const int inf=1e5;
const double pi=acos(-1.0);
const int N=5e5+5;

//char s1[25], s2[25];
//char s1[25], a2[25];
//int n;
string a[2005], b[2005];
int uN, vN;
int g[1005][1005];
int linker[1005];
bool used[1005];
bool dfs(int u)
{
    for(int v = 1; v <= vN; v++)
        if(g[u][v] && !used[v])
        {
            used[v] = true;
            if(linker[v] == -1 || dfs(linker[v]))
            {
                linker[v] = u;
                return true;
            }
        }
    return false;
}
int hungary()
{
    int res = 0;
    memset(linker,-1,sizeof(linker));
    for(int u = 1; u <= uN; u++)
    {
        memset(used,false,sizeof(used));
        if(dfs(u))res++;
    }
    return res;
}
map<string, int>mp, mpp;
void init()
{
    memset(g, 0, sizeof(g));
    mp.clear(), mpp.clear();
}
int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int t, ca=1;
    scanf("%d", &t);
    while(t--)
    {
        int n;
        scanf("%d", &n);
//        scanf("%s%s", s1, s2);
        uN=1, vN=1;
        init();
        printf("Case #%d: ", ca++);
        for(int i=0;i<n;i++)
        {
            string s1, s2;
            cin>>s1>>s2;
            if(!mp[s1])mp[s1]=uN++;
            if(!mpp[s2])mpp[s2]=vN++;
            g[mp[s1]][mpp[s2]]=1;
        }
//        uN++, vN++;
        printf("%d\n", n-uN-vN+2+hungary());
//        n=strlen(s1);
//        for(int i=0;i<n1;i++)
//            if(s1[i]==s2[i])
//            {
//                if(s1[i]=='?')
//                    a1[i]='0', a2[i]='0';
//                else
//                    a1[i]=s1[i], a2[i]=s2[i];
//            }
//            else if(s1[i]=='?')
//                a1[i]=a2[i]=s2[i];
//            else if(s2[i]=='?')
//                a1[i]=a2[i]=s1[i];
//            else
//            {
//                a1[i]=s1[i], a2[i]=s2[i];
//                if(s1[i]>s2[i])
//                {
//                    for(int j=i+1;j<n1;j++)
//                    {
//                        if(s1[j]=='?')
//                            a1[j]='0';
//                        if(s2[j]=='?')
//                            a2[j]='9';
//                    }
//                }
//                else
//                {
//                    for(int j=i+1;j<n1;j++)
//                    {
//                        if(s1[j]=='?')
//                            a1[j]='9';
//                        if(s2[j]=='?')
//                            a2[j]='0';
//                    }
//                }
//                break;
//            }
//        LL aa1=0, aa2=0;
//        for(int i=0;i<n;i++)
//            aa1=aa1*10+a1[i]-'0';
//        for(int i=0;i<n;i++)
//            aa2=aa2*10+a2[i]-'0';
//        int c1=abs(aa1-aa2);
//        for(int i=0;i<n1;i++)
//            if(s1[i]==s2[i])
//            {
//                if(s1[i]=='?')
//                    a1[i]='0', a2[i]='0';
//                else
//                    a1[i]=s1[i], a2[i]=s2[i];
//            }
//            else if(s1[i]=='?')
//                a1[i]=a2[i]=s2[i];
//            else if(s2[i]=='?')
//                a1[i]=a2[i]=s1[i];
//            else
//            {
//                a1[i]=s1[i], a2[i]=s2[i];
//                if(s1[i]>s2[i])
//                {
//                    bool flag=0;
//                    for(int j=i;j>=0;j--)
//                        if(s1[j]=='?' && s2[j]=='?')
//                        {
//                            a2[j]='1';
//                            flag=1;
//                            break;
//                        }
//                        else if(s1[j]=='?')
//                        {
//                            if(s2[j]!='0')
//                            {
//                                a2[j]=s2[j]-1;
//                                flag=1;
//                                break;
//                            }
//                        }
//                        else if(s2[j]=='?')
//                        {
//
//                        }
//                    if(flag)
//                    {
//                        for(int j=i+1;j<n1;j++)
//                        {
//                            if(s1[j]=='?')
//                                a1[j]='9';
//                            if(s2[j]=='?')
//                                a2[j]='0';
//                        }
//                    }
//                    else
//                        for(int j=i+1;j<n1;j++)
//                        {
//                            if(s1[j]=='?')
//                                a1[j]='0';
//                            if(s2[j]=='?')
//                                a2[j]='9';
//                        }
//                }
//                else
//                {
//                    for(int j=i+1;j<n1;j++)
//                    {
//                        if(s1[j]=='?')
//                            a1[j]='9';
//                        if(s2[j]=='?')
//                            a2[j]='0';
//                    }
//                }
//                break;
//            }
//        printf("%s %s\n", s1, s2);
    }
    return 0;
}
/*
2
?2? ?8?
?9 10
*/
