#include<cstdio>
#include<string.h>
//#include<conio.h>
int main()
{
    freopen("C:\\Users\\dell\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\dell\\Desktop\\output.txt","w",stdout);
    char s[102];
    int c,i,j,k,flag,x,l,ans,t,cas;
    scanf("%d",&t);
    cas=1;
    while(t--)
    {
    scanf("%s %d",s,&c);
    l=strlen(s);
    ans=0;
    for(i=0;i<l; i++)
    {
       for(j=i;j<l;j++)
       {
          x=0; 
          flag=0;            
          for(k=i; k<=j;k++)
          {
            if(s[k]!='a' && s[k]!='e' && s[k]!='i' && s[k]!='o' && s[k]!='u')
             x++; 
             else
             x=0;
             
             if(x==c)
             {
               flag=1;
               break;
             }
          }
          if(flag==1)
          ans++;
       }
    }
    printf("Case #%d: %d\n",cas++,ans);
    }
    //getch();
    return 0;
}
             
                                                
