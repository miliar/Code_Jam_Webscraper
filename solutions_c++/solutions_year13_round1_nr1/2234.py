#include<cstdio>

 using namespace std;

 int calculate(long int r,long int t)
 {
     long int cnt=0, remain=t,n=1,next;
     while(remain>0)
     {
         cnt++;
         remain=remain- (2*r+4*n-3); n++;
         if(remain < (2*r+4*n-3)) break;
     }
     return cnt;
 }




 int main()
 {
     long int T,r,t,i,y;
     scanf("%d",&T);
     for(i=0;i<T;i++)
     {
         scanf("%d %d",&r,&t);
         y=calculate(r,t);
         printf("Case #%d: %d\n",i+1,y);
     }
     return 0;
 }
