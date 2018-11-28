#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<map>
#include<string.h>
#include<fcntl.h>
#include<unistd.h>>

using namespace std ;

char str[5][5] ;

int read_inp()
{

    for(int i=1;i<=4;i++)
        scanf("%s",&str[i][1]) ;

}



int logic_x()
{
    for(int i=1;i<=4;i++)
    {
        int cnt = 0 ;
        for(int j=1;j<=4;j++)
        {
            if(str[i][j]=='X'|| str[i][j]=='T' )
            cnt++ ;

        }
        if(cnt==4)
            return 1 ;
    }
    for(int i=1;i<=4;i++)
    {
        int cnt = 0 ;
        for(int j=1;j<=4;j++)
        {
            if(str[j][i]=='X'|| str[j][i]=='T' )
            cnt++ ;

        }
        if(cnt==4)
            return 1 ;
    }
     int cnt=0 ;
    for(int i=1;i<=4;i++)
    {
        if(str[i][i]=='X' || str[i][i]=='T' )
            cnt++ ;
    }
    if(cnt==4)
           return 1 ;
    cnt=0 ;
     for(int i=1;i<=4;i++)
    {
        if(str[i][5-i]=='X' || str[i][5-i]=='T' )
            cnt++ ;
    }
        if(cnt==4)
           return 1 ;


    return 0 ;
}


int logic_o()
{
    for(int i=1;i<=4;i++)
    {
        int cnt = 0 ;
        for(int j=1;j<=4;j++)
        {
            if(str[i][j]=='O'|| str[i][j]=='T' )
            cnt++ ;

        }
        if(cnt==4)
            return 1 ;
    }
    for(int i=1;i<=4;i++)
    {
        int cnt = 0 ;
        for(int j=1;j<=4;j++)
        {
            if(str[j][i]=='O'|| str[j][i]=='T' )
            cnt++ ;

        }
        if(cnt==4)
            return 1 ;
    }
    int cnt=0 ;
    for(int i=1;i<=4;i++)
    {
        if(str[i][i]=='O' || str[i][i]=='T' )
            cnt++ ;
    }
    if(cnt==4)
           return 1 ;
    cnt=0 ;
     for(int i=1;i<=4;i++)
    {
        if(str[i][5-i]=='O' || str[i][5-i]=='T' )
            cnt++ ;
    }
        if(cnt==4)
           return 1 ;

    return 0 ;
}


int logic_empty()
{
    for(int i=1;i<=4;i++)
    {
        for(int j=1;j<=4;j++)
        {
            if(str[i][j]=='.')
                return 1 ;
        }
    }
    return 0 ;
}



int main()
{
    FILE *fp = freopen("A-large.in","r",stdin) ;
    FILE *fp1 = freopen("A-large.out","w",stdout) ;
    int test ;
    scanf("%d",&test) ;
    for(int i=1;i<=test;i++)
    {
        read_inp() ;
        int x1 = logic_x() ;
        int x2 = logic_o() ;
        if(!x1 && !x2)
        {
            if(logic_empty())
            {
                printf("Case #%d: Game has not completed\n",i) ;

            }
            else
            {
                printf("Case #%d: Draw\n",i) ;
            }

        }
        else
        {
            if(x1)
            printf("Case #%d: X won\n",i) ;
            if(x2)
            printf("Case #%d: O won\n",i) ;
        }
    }
}
