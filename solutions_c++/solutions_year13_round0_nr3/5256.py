#include<iostream>
#include<cstdio>
using namespace std;
int p[6]={1,4,9,121,484};
int get(int k)
{
    for(int i=0;i<5;i++)
     if(k<p[i])
      return i;
      return 5;
}
int main()
{
    //freopen("in.txt","r",stdin);
   // freopen("out.txt","w",stdout);
    int T,test=1;
   scanf("%d",&T);
   int a,b;
   while(T--)
   {
       scanf("%d%d",&a,&b);
       printf("Case #%d: %d\n",test++,get(b)-get(a-1));
   }
   return 0;
}
