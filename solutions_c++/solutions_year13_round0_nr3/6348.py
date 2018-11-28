#include<cstdio>
using namespace std;
int main()
{
      freopen("abc.txt","r",stdin);
      int t,test=1,a,b;
      int arr[]={1,4,9,121,484};
      scanf("%d",&t);
      while(t--)
      {
            int counts=0,i;
            scanf("%d%d",&a,&b);
            for(i=a;i<=b;++i)
            {
                  if(i==1||i==4||i==9||i==121||i==484)
                        counts++;
            }
            printf("Case #%d: %d\n",test,counts);
            ++test;

}
}
