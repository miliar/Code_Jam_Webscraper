#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <math.h>
using namespace std;

int num[100];
bool judge(int n)
{
    int t=0;
    while(n)
    {
        num[t++]=n%10;
        n/=10;
    }
    bool flag=true;
    for(int i=0;i<t/2;i++)
      if(num[i]!=num[t-1-i])
      {
          flag=false;
          break;
      }
    return flag;
}
bool real(int n)
{
    int t=(int)sqrt(1.0*n);
    if(t*t!=n)return false;
    if(judge(t)&&judge(n))return true;
    else return false;
}
int main()
{
    //freopen("C-small-attempt2.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int T;
    int A,B;
    scanf("%d",&T);
    int iCase=0;
    real(121);
    while(T--)
    {
        iCase++;
        scanf("%d%d",&A,&B);
        int ans=0;
        for(int i=A;i<=B;i++)
          if(real(i))
            ans++;
        printf("Case #%d: %d\n",iCase,ans);
    }
    return 0;
}


