#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
   freopen("D-small-attempt2.in","r",stdin);
   freopen("OUTPUT.out","w",stdout);
   int T,x,r,c;
   cin>>T;
   for(int t = 1; t <= T; t++)
   {
      cin>>x>>r>>c;
      int temp=max(r,c);
      c=min(r,c);
      r=temp;
      cout<<"Case #"<<t<<": ";
      if(x>=7)
      {
         cout << "RICHARD";
      }
     else if((r*c)%x!=0)
      {
         cout << "RICHARD";
      }
      else if(x>max(r,c))
      {
         cout << "RICHARD";
      }
     else if((x/2)>min(r,c))
      {
         cout << "RICHARD";
      }
      else if(x==1)
      {
         cout << "GABRIEL";
      }
      else if(x==4) //only for small
      {
         if(c==2)
            cout << "RICHARD";
         else if(r%4==0||c%4==0)
            cout << "GABRIEL";
         else
            cout << "RICHARD";
      }
      else if(x==2)
      {
         if(r%2==1&&c%2==1)
            cout << "RICHARD";
         else
            cout << "GABRIEL";
      }
     else if(x==3)
      {
         if(c==1)
            cout << "RICHARD";
         else if(r%3==0||c%3==0)
            cout << "GABRIEL";
         else
            cout << "RICHARD";
      }
      cout<<"\n";
   }
   return 0;
}
