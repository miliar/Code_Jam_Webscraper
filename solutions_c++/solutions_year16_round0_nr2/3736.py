#include<string>
#include<bits/stdc++.h>
using namespace std;
void con(int t,string s)
{
    int n=s.length(),flag1=0,cx=0;
    while(1)
    {
        int cou=0;
        int j=0,maa=0;
        while(j<n&&flag1==0&&s[j]=='+')
        {
            maa=1;
            cou++;
            s[j]='-';
            j++;
        }
        if(cou==n)
            break;
        if(maa==1)
            cx++;
        maa=0;
        while(j<n&&flag1==1&&s[j]=='-')
        {
            maa=1;
            s[j]='+';
            j++;
        }

        if(maa==1)
            cx++;
        if(flag1==0)
            flag1=1;
        else
            flag1=0;

    }
    printf("Case #%d: %d\n",t,cx);
}

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-largeHai.out","w",stdout);
   int t,cnn=0;
   scanf("%d",&t);
   while(t--)
   {
       string str;
       cin>>str;
       cnn++;
       con(cnn,str);
   }
return 0;
}
