#include <stdio.h>
#include <string>
#include <set>
#include <iostream>
using namespace std;
int t;
set<long long> st;
bool palin(long long a)
{
long long A = a, B = 0;
do {
B = B * 10 + (a % 10);
a/=10;
}while(a);
return A == B;
}
long long mas[1000];
int main()
{
int r = 0;
for(long long i=1;i<=10000000;i++)
   if(palin(i) && palin(i * i))
      {
      st.insert(i*i);
      mas[r++] = i*i;
      }
freopen("C-large-1.in","r",stdin);
freopen("C-large-1.out","w",stdout);
scanf("%d",&t);
for(int it=1;it<=t;it++)
   {
   long long a, b, rd = 0;
   cin>>a>>b;
   for(int i=0;i<r;i++)
      if(mas[i] >= a && mas[i] <= b)
         rd++;
   cout<<"Case #"<<it<<": "<<rd<<endl;
   }
return 0;
}
