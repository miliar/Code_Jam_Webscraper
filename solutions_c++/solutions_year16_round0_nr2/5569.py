#include<iostream>

using namespace std;

int main()
{
   freopen ("B-large.in", "r", stdin);
   freopen ("B-large.out", "w" , stdout);
   int n,t,tt,i,j,a[1<<4],c,cc,fl;
   string s;
   cin>>t;
   for(tt=1;tt<=t;tt++)
   {
      cin>>s;
      s+="+";
      //n=tt;
      c=0;
      for(i=s.length()-1;i>=1;i--)
      {
         if(s[i]!=s[i-1])
         {
            c++;
         }
      }
      cout<<"Case #"<<tt<<": "<<c<<endl;
   }
   //system("pause");
   return 0;
}
