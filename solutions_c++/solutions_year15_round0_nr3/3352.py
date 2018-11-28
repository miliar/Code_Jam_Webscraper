#include<bits/stdc++.h>
char st[10001];
int str[10001];
int n;
int pb(int i,int ch)
{
    //printf("new %d %d\n",i,ch);
    int flag=0,last;
    while(i<n)
    {
        if(flag==0)
        {
            last = str[i];
            flag=1;
        }
        else
        {
           if(last==1)
            last=str[i];
           else if(last==2)
           {
               if(str[i]==2)
                last=-1;
               else if(str[i]==3)
                last = 4;
               else last =6;
           }
           else if(last==3)
           {
               if(str[i]==2)
                last=7;
               else if(str[i]==3)
                last = -1;
               else last =2;
           }
           else if(last==4)
           {
               if(str[i]==2)
                last=3;
               else if(str[i]==3)
                last = 5;
               else last =-1;
           }
           else if(last==-1)
           {
               if(str[i]==2)
                last=5;
               else if(str[i]==3)
                last = 6;
               else last =7;
           }
           else if(last==5)
           {
               if(str[i]==2)
                last=1;
               else if(str[i]==3)
                last = 7;
               else last =3;
           }
           else if(last==6)
           {
               if(str[i]==2)
                last=4;
               else if(str[i]==3)
                last = 1;
               else last =5;
           }
           else if(last==7)
           {
               if(str[i]==2)
                last=6;
               else if(str[i]==3)
                last = 2;
               else last =1;
           }
        }
        //printf("%d %d\n",last,i);
        i++;
        if(ch!=4&&last==ch)
        {

            if(pb(i,ch+1))
                return 1;
            return 0;
        }
        else if(ch==4&&last==ch&&i==n)
                    return 1;
    }
    return 0;
}


int main()
{
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,l,x=0,y=0;
    scanf("%d",&t);
    while(t--)
    {
        y++;
        int i=0,j;
        scanf("%d%d",&l,&x);
        scanf("%s",&st);
        for(i=0;i<l;i++)
            str[i] = st[i]-'g';
        i=l;
        while(--x)
        {
            for(j=0;j<l;j++,i++)
                str[i]=str[j];
        }

        n=i;
        /*for(i=0;i<n;i++)
            printf("%d ",str[i]);
        printf("\n");*/
        if(pb(0,2))
            printf("Case #%d: YES\n",y);
        else printf("Case #%d: NO\n",y);
    }
}
