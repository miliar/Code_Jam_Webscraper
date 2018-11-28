#include <iostream>
#include <cstdio>

using namespace std;

int  main()
{
   freopen("A-small-attempt3.in","r",stdin);
   freopen("out.txt","w",stdout);

   int test;
   cin>>test;
   long long int p,q,count,temp;
   int test_count=0;
   while(test--)
   {
      test_count++;
      count=0;
      int flag=0;
      scanf("%lld/%lld",&p,&q);
      temp=q;
       if(q%2==0 && p%2!=0 && p<q)
      {
          while(p<q)
        {
            if(q%2!=0)
            {
                flag++;
                break;
            }
            count++;
            q=q/2;
        }
        while(temp!=2)
        {
              if(temp%2!=0)
            {
                flag++;
                break;
            }
            temp=temp/2;
        }
        if(flag==0)
            printf("Case #%d: %lld\n",test_count,count);
        else
            printf("Case #%d: impossible\n",test_count);
      }
      else
          printf("Case #%d: impossible\n",test_count);

   }

   return 0;
}
