#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<queue>
#define second SD
#define first FT
#define push_back PB
#define make_pair MP
using namespace std;
typedef long long LL;
typedef pair<int,int> P;
const int maxn=5+1e6,MOD=7+1e9;
string s1,s2;
int k,l,s;
int ans,sum,_max;
int cal(string ss)
{
         int cnt=0;
         for(int i=0;i<=s-l;i++){
                  bool ok=1;
                  for(int j=0;j<l;j++){
                           if(ss[j+i]!=s2[j]) {
                                    ok=0;
                                    break;
                           }
                  }
                  if(ok) cnt++;
         }
         return cnt;
}
void bfs()
{
         queue<string> q;
         while(!q.empty()) q.pop();
         q.push("");
         while(!q.empty()){
                  string now=q.front();
                  q.pop();
                  if(now.length()==s) {
                           sum++;
                           int tp=cal(now);
                           ans+=tp,_max=max(_max,tp);
                           continue;
                  }
                  for(int i=0;i<k;i++){
                           string tmp=now+s1[i];
                           q.push(tmp);
                  }
         }
}
int main()
{
         freopen("B-small-attempt0.in","r",stdin);
         //freopen("ans.out","w",stdout);
         int T,ca=0;
         scanf("%d",&T);
         while(T--){
                  cin>>k>>l>>s;
                  cin>>s1>>s2;
                  sum=ans=0,_max=-1;
                  bfs();
                  printf("Case #%d: %.6lf\n",++ca,1.0*(double)_max-1.0*(double)ans/sum);
         }
         return 0;
}
