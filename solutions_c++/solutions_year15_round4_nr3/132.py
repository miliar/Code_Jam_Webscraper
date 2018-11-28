/**
 * @author neko01
 */
//#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstring>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <queue>
#include <vector>
#include <cmath>
#include <set>
#include <map>
using namespace std;
typedef long long LL;
#define min3(a,b,c) min(a,min(b,c))
#define max3(a,b,c) max(a,max(b,c))
#define pb push_back
#define mp(a,b) make_pair(a,b)
#define clr(a) memset(a,0,sizeof a)
#define clr1(a) memset(a,-1,sizeof a)
#define dbg(a) printf("%d\n",a)
typedef pair<int,int> pp;
const double eps=1e-9;
const double pi=acos(-1.0);
const int INF=0x3f3f3f3f;
const LL inf=(((LL)1)<<61)+5;
map<string,int>mp1,mp2;
map<string,int>::iterator it;
vector<vector<string> >a(25);
int main()
{
    freopen("C-small-attempt0 (1).in" , "r" , stdin);
    freopen("C-small-attempt0 (1).out" , "w" , stdout);
    int t,cnt=0;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        string s;
        mp1.clear();
        mp2.clear();
        while(cin>>s){
            mp1[s]=1;
            if (getchar()=='\n')
                break;
        }
        while(cin>>s){
            mp2[s]=1;
            if (getchar()=='\n')
                break;
        }
        n-=2;
        for(int i=0;i<n;i++){
            a[i].clear();
            while(cin>>s){
                a[i].pb(s);
                if (getchar()=='\n')
                    break;
            }
        }
        int ans=0;
        for(it=mp1.begin();it!=mp1.end();++it){
            string tmp=it->first;
            if(mp2.count(tmp))
                ans++;
        }
        int res=INF;
        for(int i=0;i<(1<<n);i++){
            map<string,int>tmp1,tmp2;
            map<string,int>::iterator it1;
            int sum=0;
            for(int j=0;j<n;j++){
                if(i&(1<<j)){
                    for(int k=0;k<a[j].size();k++)
                        tmp2[a[j][k]]=1;
                }
                else{
                    for(int k=0;k<a[j].size();k++)
                        tmp1[a[j][k]]=1;
                }
            }
            for(it1=tmp1.begin();it1!=tmp1.end();++it1){
                string tmp=it1->first;
                if(!mp1.count(tmp)&&((tmp2.count(tmp)||mp2.count(tmp))))
                    sum++;
            }
            for(it=mp1.begin();it!=mp1.end();++it){
                string tmp=it->first;
                if(!mp2.count(tmp)&&!tmp1.count(tmp)&&tmp2.count(tmp))
                    sum++;
            }
            if(sum<res) res=sum;
        }
        printf("Case #%d: %d\n",++cnt,ans+res);
    }
    return 0;
}
