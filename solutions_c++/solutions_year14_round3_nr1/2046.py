#include<iostream>
#include<vector>
#include<fstream>

using namespace std;
typedef int64_t lint;

bool ptwo(lint x)
{
    return (x != 0) && ((x & (x - 1)) == 0);
}

lint gcd(lint u, lint v) {
return (v != 0)?gcd(v, u%v):u;
}
int main()
{
    fstream in("A-small-attempt0.in");
    fstream out("ans.txt");
 int t;
 in>>t;
 for(int o=1;o<=t;o++)
 {
     lint P,Q;
     in>>P;
     char t; in>>t;
     in>>Q;

     lint ans=0;
     int Pone=0 ,Qone=0;
     bool flag=true;
     if(ptwo(Q))
     {

         while(Q!=0){Q=Q>>1;Qone++;}
         while(P!=0){P=P>>1;Pone++;}
         ans=Qone-Pone;
     }
     else
     {
         int k=0;
         lint Q1=Q;
         while(Q1%2==0){Q1/=2;k++;}
         //cout<<"\n"<<(1<<k)<<"\n";
         lint pos=Q/(1<<k);
        // cout<<pos<<"\n";
         if(gcd(P,pos)==pos)
         {
             P=P/pos; //cout<<P<<"\n";
             Q=Q/pos;
            while(P!=0){P=P>>1;Pone++;}

            Qone=k;
            ans=Qone-(Pone-1);
         }
         else
         {
             flag=false;
         }
     }
     if(flag) out<<"Case #"<<o<<": "<<ans<<"\n";
     else out<<"Case #"<<o<<": impossible\n";

 }
 return 0;

}
