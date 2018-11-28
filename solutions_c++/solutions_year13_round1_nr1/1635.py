#include<iostream>
#include<cstdio>

using namespace std;
int main()
{
    //freopen("C:\\Users\\DELL\\Desktop\\input.txt","r",stdin); 
//freopen("C:\\Users\\DELL\\Desktop\\output.txt","w",stdout);
  unsigned long long int r,t,count,r1,r2;
  int T,i;
  scanf("%d",&T);
  for(i=1;i<=T;i++)
  {
            count=0;
            scanf("%llu %llu",&r,&t);
            r1=r;
            r2=r1+1;
            while((r2*r2-r1*r1)<=t)
            {
             count++;
             t=t-(r2*r2-r1*r1);
             r1=r2+1;
             r2=r1+1;
             //printf("%llu %llu %llu\n",t,r1,r2);
             }
             printf("Case #%d: %llu\n",i,count);
             }
             return 0;
             }
             
                               
