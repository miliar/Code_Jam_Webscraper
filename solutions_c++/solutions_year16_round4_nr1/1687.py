#include <bits/stdc++.h>
using namespace std;

string solve(int n,int r,int p,int s)
{
   int pr[10];
   bool flag,ex;
   string str,curr,t,ans,buf;
   for (int i=0;i<r;i++) str+= 'R';
   for (int i=r;i<r+p;i++) str+= 'P';
   for (int i=r+p;i<r+p+s;i++) str+= 'S';
   for (int i=0;i<(1<<n);i++) pr[i] = i+1;
   ex = false;
   do
   {
       flag = true;
       curr = "";
       for (int i=0;i<(1<<n);i++) curr+=str[pr[i]-1];
       buf = curr;
       while (curr.length()>1)
       {
           t = "";
           for (int i=0;i<curr.length();i+=2)
           {
               if (curr[i]==curr[i+1])
               {
                   flag = false;
                   break;
               }
               if (curr[i]=='R')
               {
                   if (curr[i+1]=='S') t+='R'; else t+='P';
               }

               if (curr[i]=='P')
               {
                   if (curr[i+1]=='R') t+='P'; else t+='S';
               }

               if (curr[i]=='S')
               {
                   if (curr[i+1]=='P') t+='S'; else t+='R';
               }
           }
           curr = t;
       }
       if (flag)
       {
        if (!ex) ans = buf; else
        {
            if (ans>buf) ans = buf;
        }
        ex = true;
       }
   }while (next_permutation(pr,pr+(1<<n)));
  if (!ex) return "IMPOSSIBLE"; else return ans;
}

int main()
{
    ios_base::sync_with_stdio(false);
    freopen("in.txt","r",stdin);
   freopen("out.txt","w",stdout);
   int T,n,r,p,s;
   cin>>T;

   for (int test=1;test<=T;test++)
   {
       cin>>n>>r>>p>>s;
       cout<<"Case #"<<test<<": "<<solve(n,r,p,s)<<endl;
   }
    return 0;
}
