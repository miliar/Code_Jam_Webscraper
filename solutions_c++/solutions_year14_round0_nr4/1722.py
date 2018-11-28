#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define Max 1024
double nao[Max],ken[Max] ;

double comp(double a , double b)
{
   return a > b ;
}

int main()
{

freopen("D-large.in","r",stdin);
freopen("output","w",stdout);


int t , a , b , c , d , n,war,dec,temp;
scanf("%d",&t);
for(a=1;a<=t;a++)
{
  scanf("%d",&n);

  for(b=0;b<n;b++)
  scanf("%lf",&nao[b]);

  for(b=0;b<n;b++)
  scanf("%lf",&ken[b]);

  sort(nao,nao+n,comp);
  sort(ken,ken+n,comp);
 /*
  cout<<endl;
  for(b=0;b<n;b++)
  printf("%lf ",nao[b]);
  cout<<endl;
  for(b=0;b<n;b++)
  printf("%lf ",ken[b]);
  cout<<endl;
  */

  // war
  war = temp = dec =  0;
  c = 0;
  for(b=0;b<n;b++)
  {
    if(ken[c]>nao[b])
    {
    temp++ ;
    c++ ;
    }
  }
  war = n - temp;

  // Deceitful War
  sort(nao,nao+n,comp);
  sort(ken,ken+n,comp);
  c = 0;
  d = n;
  for(b=0;d>b;)
  {
     if(nao[b]>ken[c])
     {
     b++;
     c++;
     dec++ ;
     }
     else if(nao[b]<ken[c])
     {
       d--;
       c++;
     }
  }

  printf("Case #%d: %d %d\n",a,dec,war);

}
return 0;
}
