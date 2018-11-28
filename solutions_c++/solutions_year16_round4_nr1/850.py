#include <bits/stdc++.h>

using namespace std;

string res,ans;
int rev[(1<<13)];
int R,P,S;
int n,AA;

void check(int t,int T,int lvl)
 {
  if (lvl == n)
   {
    if (ans[t] < ans[T]) AA=1;
    if (ans[t] > ans[T]) AA=2;
    return;
   }
  int L1=2*t,L2=2*T;
  if (rev[t]) L1=2*t+1;
  if (rev[T]) L2=2*T+1;
  check(L1,L2,lvl+1);
  if (AA) return;
  check(4*t+1-L1,4*T+1-L2,lvl+1);
 }

void solve(int t,int lvl,int ch)
 {
  if (lvl == n)
   {
    ans[t]=char(ch);
    if (ch == 'R') R++;
    if (ch == 'S') S++;
    if (ch == 'P') P++;
    return;
   }
  int ch2;
  if (ch == 'S') ch2='P'; else
  if (ch == 'P') ch2='R'; else
  if (ch == 'R') ch2='S';
  solve(2*t,lvl+1,ch);
  solve(2*t+1,lvl+1,ch2);
  AA=0;
  check(2*t,2*t+1,lvl+1);
  rev[t]=AA-1;
 }

int t,t1,r,p,s;

string get(int t,int lvl)
 {
  if (lvl == n)
   {
    string rt="";
    rt+=ans[t];
    return rt;
   }
  string ret="";
  if (rev[t])
    ret+=get(2*t+1,lvl+1);
  ret+=get(2*t,lvl+1);
  if (!rev[t])
    ret+=get(2*t+1,lvl+1);
  return ret;
 }

bool f;

int main()
 {
   freopen("A.in","r",stdin);
   freopen("A.out","w",stdout);
   cin>>t;
   for (t1=1;t1<=t;t1++)
    {
     cout<<"Case #"<<t1<<": ";
     cin>>n>>r>>p>>s; n++;
     ans=res="";
     f=0;
     for (int i=0;i<=2*(1<<n)+1;i++) ans+='Z',res+='Z';
     R=P=S=0;
     solve(1,1,'S');
     if (R == r && P == p && S == s)
      { f=1; res=min(res,get(1,1)); }
     R=P=S=0;
     solve(1,1,'P');
     if (R == r && P == p && S == s)
      { f=1; res=min(res,get(1,1)); }
     R=P=S=0;
     solve(1,1,'R');
     if (R == r && P == p && S == s)
      { f=1; res=min(res,get(1,1)); }
     if (!f) cout<<"IMPOSSIBLE"<<endl;
     if (f) cout<<res<<endl;
    }
 }
