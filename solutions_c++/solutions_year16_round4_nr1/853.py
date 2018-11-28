#define LOCAL
#include<bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef double DB;
const int maxn=12;
vector<char> ans;
map<int,vector<char> > mp[(1<<maxn)][(1<<maxn)];
void stand(vector<char>& vec,int L,int R)
{
    if(L==R) return;
    int M=(L+R)>>1;
    stand(vec,L,M);
    stand(vec,M+1,R);
    for(int i=0;i<R-M;i++)
    {
        if(vec[L+i]==vec[M+1+i]) continue;
        else if(vec[L+i]<vec[M+1+i]) break;
        else
        {
            vector<char> tmp;
            tmp.resize(vec.size());
            for(int j=L;j<=M;j++) tmp[j+R-M]=vec[j];
            for(int j=M+1;j<=R;j++) tmp[j-R+M]=vec[j];
            for(int j=L;j<=R;j++) vec[j]=tmp[j];
            break;
        }
    }
}
void dfs(vector<char> vec,int P,int R,int S,int dep)
{
    stand(vec,0,vec.size()-1);
    mp[P][R][S]=vec;
    if(dep==12)
    {
        assert(vec.size()==(1<<12));
        return;
    }
    vector<char> nx;
    for(int i=0;i<vec.size();i++)
    {
        if(vec[i]=='P') nx.push_back(vec[i]),nx.push_back('R'),R++;
        else if(vec[i]=='R') nx.push_back(vec[i]),nx.push_back('S'),S++;
        else nx.push_back('P'),nx.push_back(vec[i]),P++;
    }
    dfs(nx,P,R,S,dep+1);
}
int main()
{
#ifdef LOCAL
    freopen("Ain","r",stdin);
    freopen("Aout","w",stdout); 
#endif
    vector<char> vec;
    vec.push_back('P');
    dfs(vec,1,0,0,0);
    vec.clear();vec.push_back('R');
    dfs(vec,0,1,0,0);
    vec.clear();vec.push_back('S');
    dfs(vec,0,0,1,0);
    int T,kase=0;
    scanf("%d",&T);
    while(T--)
    {
        int N,R,P,S;
        scanf("%d%d%d%d",&N,&R,&P,&S);
        if(!mp[P][R].count(S)) printf("Case #%d: IMPOSSIBLE\n",++kase);
        else
        {
            printf("Case #%d: ",++kase);
            for(int i=0;i<mp[P][R][S].size();i++) printf("%c",mp[P][R][S][i]);puts("");
        }
    }
}
