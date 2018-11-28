#include<string>
#include<vector>
#include<map>
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<sstream>
#include<set>
#include<cstdlib>
using namespace std;
int main()
{
  int t,sm,p=0;
  scanf("%d",&t);
  while(t--)
  {p++;
   scanf("%d",&sm);
   string s;
   cin>>s;
   int sum=0,k=0;
   char c=s[0];
   int temp=c-'0';
   if(temp==0)
   {sum++;k++;}
   if(temp>0)
   k=k+temp;
   for(int i=1;i<=sm;i++)
   {char f=s[i];
    int t=f-'0';
    if(t==0)
    continue;
     if(i>k)
     {sum=sum+(i-k);k=k+t+(i-k);continue;}
     if(i<=k)
     {k=k+t;}
   } 
cout<<"case #"<<p<<": "<<sum<<endl;
}
return 0;
} 
           
                      
