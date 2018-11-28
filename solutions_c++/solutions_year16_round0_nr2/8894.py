#include<bits/stdc++.h>
using namespace std;
int add(int l,char c[])
{
    char str[105],s;
    int j=0,i;
    for(i=0;i<105;i++)
        str[i]='\0';
    for(i=0;i<l;)
    {
        s=c[i];
        while(s==c[i])
            i++;
        str[j]=s;
        j++;
    }
    int len=strlen(str);
    for(i=0;i<105;i++)
        c[i]='\0';
    for(i=0;i<len;i++)
        c[i]=str[i];
    l=strlen(c);
    return l;

}


int main()
{
    int t,i,j,k;
    scanf("%d",&t);
    int cnt=1;
    while(t--)
    {
      char ch[105];
      scanf("%s",&ch);
      int l=strlen(ch);
      l= add(l,ch);
      if(l==1)
      {
          if(ch[0]=='+')
            printf("Case #%d: 0\n",cnt);
          else
            printf("Case #%d: 1\n",cnt);
      }
      else
      {
          if(l%2==0)
          {
              if(ch[0]=='+')
                k=l;
              else
                k=l-1;
          }
          else
          {
              if(ch[0]=='+')
                k=l-1;
              else
                k=l;
          }
          printf("Case #%d: %d\n",cnt,k);
      }
      cnt++;

    }
    return 0;
}
