//TooSimple!
#include<bits/stdc++.h>
using namespace std;
typedef long long int uli;
map<char,char>mp;
char winner(char a,char b){
   if(mp[a]==b)return a;
   return b;
}
string solve(int n,int q[3],string o){
   if(q[0]+q[1]+q[2]==1){
      for(int i=0;i<3;i++)if(q[i]!=0)return string(1,o[i]);
   }
   int x=(1<<(n-1))-q[0];
   if(x<0 || q[1]<x || q[2]<x)return "";
   int n1=q[1]-x;
   int n2=q[2]-x;
   if(n1+n2!=q[0])return "";

   string t="";
   for(int i=0;i<n1;i++)t.push_back(winner(o[0],o[1]));
   for(int i=0;i<n2;i++)t.push_back(winner(o[0],o[2]));
   for(int i=0;i<x;i++)t.push_back(winner(o[1],o[2]));
   string no="";
   no.push_back(winner(o[0],o[1]));
   no.push_back(winner(o[0],o[2]));
   no.push_back(winner(o[1],o[2]));

   int nq[3]={0,0,0};
   for(char ch:t)
      for(int i=0;i<3;i++)
         if(ch==no[i])
            nq[i]++;
   string w=solve(n-1,nq,no);
   if(w.empty())return "";
   string ans="";
   for(char ch:w){
      if(ch==winner(o[0],o[1]))ans+=string(1,o[0])+string(1,o[1]);
      if(ch==winner(o[0],o[2]))ans+=string(1,o[0])+string(1,o[2]);
      if(ch==winner(o[1],o[2]))ans+=string(1,o[1])+string(1,o[2]);
   }
   return ans;
}
int main(){
   freopen("al.in","r",stdin);
   freopen("al.out","w",stdout);
   mp['P']='R';
   mp['R']='S';
   mp['S']='P';
   int t;
   scanf("%d",&t);
   for(int tt=1;tt<=t;tt++){
      cerr<<"t="<<tt<<endl;
      int n,r,p,s;                  
      scanf("%d %d %d %d",&n,&r,&p,&s);
      int q[3]={p,r,s};
      string ans=solve(n,q,"PRS");
      if(!ans.empty())printf("Case #%d: %s\n",tt,ans.c_str());
      else printf("Case #%d: IMPOSSIBLE\n",tt);
   }
   return 0;
}
