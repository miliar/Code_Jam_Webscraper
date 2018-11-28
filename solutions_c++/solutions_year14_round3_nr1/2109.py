#include <bits/stdc++.h>
using namespace std;

/*
int solve(int curn1,int curd1,int curn2,int curd2,int p,int q,int steps)
{
    if(curn>p || curd>q)
        return 0;
    else if cmp(curn1,curd1,curn2,curd2,steps)
        return steps;
    else return mmin( solve()
}
*/
int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
   #define int long long int
    int t,p,q;
    char c;
    cin>>t;
    map<pair<int,int>,int> m,r;
    m[make_pair(0,1)]=INT_MAX;
    m[make_pair(1,1)]=1;
    for(int y=0;y<12;y++)
        {

                for(map<pair<int,int>,int>::iterator i=m.begin();i!=m.end();++i)
                {
                    for(map<pair<int,int>,int>::iterator j=m.begin();j!=m.end();++j)
                    {
                        int numr=(i->first.first)*(j->first.second)+(i->first.second)*(j->first.first);
                        int demr=2*(i->first.second)*(j->first.second);
                        int mygcd=__gcd(numr,demr);
                        numr/=mygcd;
                        demr/=mygcd;
                        int tmp=r[make_pair(numr,demr)];
                        if(tmp==0)
                        {
                            r[make_pair(numr,demr)]=min(i->second,j->second)+1;
                        }
                        else
                        {
                            r[make_pair(numr,demr)]=min(tmp,min(i->second,j->second)+1);
                        }
                    }
                }
                for(map<pair<int,int>,int>::iterator i=r.begin();i!=r.end();++i)
                {
                    int tmp=m[make_pair(i->first.first,i->first.second)];
                        if(tmp==0)
                        {
                            m[make_pair(i->first.first,i->first.second)]=i->second;
                        }
                        else
                        {
                            m[make_pair(i->first.first,i->first.second)]=min(tmp,i->second);
                        }
                   // m[make_pair(i->first.first,i->first.second)]=i->second;
                }
                r.clear();
        }
   for(int tc=1;tc<=t;tc++)
    {
        string s;
        cin>>s;
        int cc=0;
        p=0,q=0;
        for(cc=0;cc<s.size() && s[cc]!='/';cc++)
            p=p*10+(s[cc]-'0');
        for(int j=(cc+1);j<s.size();j++)
            q=q*10+(s[j]-'0');
        if(m[make_pair(p,q)]==INT_MAX || m[make_pair(p,q)]==0)
                printf("Case #%lld: impossible\n",tc);
        else printf("Case #%lld: %lld\n",tc,m[make_pair(p,q)]-1);
    }
}
