#include<iostream>
using namespace std;
int N,M,T,map[12][12],Case,flag1,flag2;
int main()
{
 //freopen("2.in","r",stdin);
 //freopen("2.out","w",stdout);
  cin>>T;Case=0;
  while(T--)
  {
   cin>>N>>M; flag1=1,flag2=1;
   for(int i=1;i<=N;i++)
     for(int j=1;j<=M;j++)
       cin>>map[i][j];
       if(N==1) {cout<<"Case #"<<++Case<<": "<<"YES"<<endl;continue;}
   for(int i=1;i<=N;i++)
   {
      flag1=1,flag2=1; 
     for(int j=1;j<=M;j++)
     {
       if(map[i][j]==1)
       {
         int sum1=0,sum2=0;
         for(int k=1;k<=M;k++)//行和 
          sum1+=map[i][k];
         if(sum1>M) flag1=0;
         for(int k=1;k<=N;k++)//列和 
          sum2+=map[k][j];
         if(sum2>N) flag2=0;                         
       } 
       if(!flag1&&!flag2) break;      
     } 
     if(!flag1&&!flag2) break;
   } 
   if(!flag1&&!flag2) cout<<"Case #"<<++Case<<": "<<"NO"<<endl;
   else cout<<"Case #"<<++Case<<": "<<"YES"<<endl;   
  }  
} 
