#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<stack>

using namespace std;
int t,x,r,c,f,cc,i;
int main()
{
     //freopen("D-small-attempt1.in","r",stdin);
     //freopen("D.txt","w",stdout);
     cin>>t;
     cc=t;
     while(t--)
     {
         cin>>x>>r>>c;
         if(x==1) { cout<<"Case #"<<cc-t<<": GABRIEL\n"; continue; }
         f=1;
         if((r*c)%x==0)
         {
             for(i=2;i<x;i++)
             {
                 if(min(r,c)<i) {f=0; break; }
             }
         }
         else f=0;
         if(f==0) cout<<"Case #"<<cc-t<<": RICHARD\n";
         else  cout<<"Case #"<<cc-t<<": GABRIEL\n";
     }
     return 0;
}
