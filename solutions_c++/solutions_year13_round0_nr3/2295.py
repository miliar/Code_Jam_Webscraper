#include<iostream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

int palin(long long n)
{
 long long a,b,c;
 
 a=n;b=0;c=0;
 
 while(a)
 {
  c=a%10;
  b=b*10+c;
  a=a-c;
  a=a/10;        
 }   
 
 if(b==n)
 return 1;
 
 else
 return 0;    
}

int main()
{
 int t,z,j,ch,c=0;
 long long i,a,b;
 vector<long long>num;
 
 for(i=1;i<=10000000;i++)
 {
  if(palin(i))
  if(palin(i*i))            
  { c++; num.push_back(i*i); }
 }
 
 sort(num.begin(), num.end());
 
 freopen("C-large-1.in", "r", stdin);
 freopen("output.txt", "w", stdout);
 
 scanf("%d",&t);
 
 for(z=0;z<t;z++)
 {
  scanf("%lld%lld",&a,&b);
  
  ch=0; i=0;
  
  while((num[i]<a)&&(i<c))
  i++;
  
  while((num[i]<=b)&&(i<c))
  { i++; ch++; }
  
  printf("Case #%d: %d\n",z+1,ch);
 }
 
 cin>>i;   
 return 0;   
}
