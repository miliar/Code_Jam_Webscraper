#include<bits/stdc++.h>
using namespace std;
const int maxn=1000000+10 ;

map<string,int> mp ;
int mcnt ;
int ID(const string &s)
{
    auto it=mp.find(s) ;
    if(it!=mp.end()) return it->second ;
    return mp[s]=++mcnt ;
}

vector<int> v[30] ;
int val[maxn],ans ;
void add(int x,int type)
{
    if(val[x]==3) return ;
    val[x]|=(type ? 1 : 2) ;
    if(val[x]==3) ans++ ;
}

char s[maxn] ;

int solve()
{
    int n ; scanf("%d",&n) ; gets(s) ;
    mp.clear() ; mcnt=0 ;
    for(int i=0;i<30;i++) v[i].clear() ;
    for(int i=0;i<n;i++)
    {
        gets(s) ;
        int len=strlen(s) ;
        for(int j=0;j<len;)
        {
            string st ;
            while(j<len && s[j]!=' ') st.push_back(s[j++]) ;
            j++ ; v[i].push_back(ID(st)) ;
        }
    }
    int ret=mcnt ;
    for(int i=0;i<(1<<n);i++) if((i&1) && !(i&2))
    {
        fill(val,val+mcnt+1,0) ;
        ans=0 ;
        for(int j=0;j<n;j++) for(auto k : v[j])
            add(k,i&(1<<j)) ;
        ret=min(ret,ans) ;
    }
    return ret ;
}

main()
{
    if(fopen("C.in","r"))
        freopen("C.in","r",stdin) ,
        freopen("C.out","w",stdout) ;
    int T,tc ; scanf("%d",&T) ;
    while(T--) printf("Case #%d: %d\n",++tc,solve()) , fprintf(stderr,"tc = %d\n",tc) ;
}
