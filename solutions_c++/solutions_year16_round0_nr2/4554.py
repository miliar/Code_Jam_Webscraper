#include<bits/stdc++.h>
#define pn() printf("\n")
#define ps() printf(" ")
#define si(x) scanf("%d",&x)
#define pi(x) printf("%d",x)
#define sll(x) scanf("%I64d",&x)
#define pll(x) printf("%I64d",x)
#define sc(x) scanf("%c",&x)
#define pc(x) printf("%c",x)
#define sf(x) scanf("%f",&x)
#define pf(x) printf("%f\n",x)
#define sd(x) scanf("%lf",&x)
#define pd(x) printf("%.9lf\n",x)
#define sld(x) scanf("%Lf",&x)
#define pld(x) printf("%.9Lf\n",x)
#define MOD 1000000007
#define ll long long
#define eps 1e-10
using namespace std;
map<string,int>m1;
string ss;
int ans;
bool operator<(const string a,const string b){
   return m1[a]>m1[b];
}
void djistras(string ss){
  priority_queue<string>pq;
  int i,j;
  m1[ss] = 0;
  pq.push(ss);
  while(!pq.empty()){
     string tmp = pq.top();
     //cout<<tmp<<" "<<m1[tmp]<<endl;
     pq.pop();
     int cnt = 0;
     for(i=0;i<tmp.size();++i)
        if(tmp[i]=='-')
            cnt++;
     if(cnt==0){
        ans = m1[tmp];
        break;
     }
     string nxt;
     for(i=0;i<tmp.size();++i){
        nxt.clear();
        for(j=i;j>=0;--j)
            if(tmp[j]=='-')
                nxt.push_back('+');
            else
                nxt.push_back('-');
        for(j=i+1;j<tmp.size();++j)
            nxt.push_back(tmp[j]);
        if(!m1.count(nxt)){
            m1[nxt] = m1[tmp]+1;
            pq.push(nxt);
        }else if(m1[tmp]+1<m1[nxt]){
           m1[nxt] = m1[tmp]+1;
            pq.push(nxt);
        }

     }
  }
}

int main(void){

    int t,n,m,i,j,test;
    cin>>t;
    for(test=1;test<=t;++test){
            m1.clear();
            cin>>ss;
            djistras(ss);
            cout<<"Case #"<<test<<": "<<ans<<endl;
    }
    return 0;
}
