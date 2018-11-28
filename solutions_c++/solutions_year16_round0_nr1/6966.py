#include<cstdio>
using namespace std;

int main()
{
   int t,i;

   scanf("%d",&t);
      int total=t;
    long int n,test,temp,num,rem;
   for(int j=1;j<=t;j++)
   {
     scanf("%ld",&n);
     int flag=0;
     if(n!=0)    
     {
        int count[10]={0};
        int cnt=0;
        for(i=1;i<=100;i++)
         {
            test=i*n;
            temp=test;
            while(temp)
             {
               rem=temp%10;
               temp=temp/10;
               if(count[rem]==0){ count[rem]=1;cnt++;}
               if(cnt==10){flag=1;num=test;break; }
             }
          if(flag==1){break;}
         } 
     }
     
      if(flag==0)
      printf("Case #%d: INSOMNIA\n",j);
      else
      printf("Case #%d: %ld\n",j,num);
   
      
   }

return 0;
}
