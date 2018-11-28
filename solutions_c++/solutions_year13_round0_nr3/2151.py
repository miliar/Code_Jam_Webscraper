#include<iostream>
#include<string.h>
#include<math.h>
using namespace std;
char ans[100];
int f(int k)
{
    int i=0;
    while(k)
    {
            ans[i++]='0'+k%10;
            k/=10;
    }
    ans[i]='\0';
    i--;
    for(int j=0;j<=i/2;j++)
    if(ans[j]!=ans[i-j]) return 0;
    return 1;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int i,j;
    int a,b,sum;
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
                     sum=0;
                     scanf("%d%d",&a,&b);
                     if((int)sqrt(a)*(int)sqrt(a)==a) j=(int)sqrt(a);
                     else j=(int)sqrt(a)+1;
                     while(j*j<=b)
                     {
                                  if(f(j)&&f(j*j)) {sum++;}
                                  j++;
                     }
                     printf("Case #%d: %d\n",i,sum);
    }
    return 0;
}

