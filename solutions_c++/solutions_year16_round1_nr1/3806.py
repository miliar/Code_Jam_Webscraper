#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("Tasnim.txt","r",stdin);
    freopen("Tasnim_.txt","w",stdout);
   char fine[1001];
   list<char>nfine;
   list<char>::iterator it;
   int i,j,ts,length;
   char tm;
   cin>>ts;
   for(i=1; i<=ts; i++)
   {
       cin>>fine;
       cout << "Case #" << i <<": ";
       length=strlen(fine);
       nfine.push_back(fine[0]);
       tm=fine[0];
       for(j=1; j<length; j++)
       {
           if(fine[j]>=tm)
           {
               nfine.push_front(fine[j]);
               tm=fine[j];
           }
           else
           {
               nfine.push_back(fine[j]);
           }

       }
       for(it=nfine.begin();it!=nfine.end();it++)
       {
           cout<<*it;
       }
       cout<<endl;
       nfine.clear();
   }
   return 0;
}
