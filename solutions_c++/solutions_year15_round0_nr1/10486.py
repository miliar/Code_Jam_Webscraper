#include<iostream>
#include<stdio.h>


using namespace std;
int T,s_level;
char buf[2000];


int  alGorithm(void)
{

        if(s_level==0)
                return 0;
        int num,number,needNumber=0;
        for(int i=0;i<=s_level;++i)
        {

                if(i==0)
                {
                        number=buf[0]-'0';
                        continue;
                }
                if(buf[i]=='0')
                        continue;

                num=buf[i]-'0';
                if((number-i)>=0)
                        number=number+num;
                else
                {
                        needNumber=needNumber+(i-number);
                        number=number+needNumber+num;
                }
        }
        return needNumber;
}
void input(char*fileName)
{
        freopen(fileName,"r",stdin);
        char ch;
        scanf("%d\n",&T);

        for(int i=0;i<T;++i)
        {
                int start=0;
                scanf("%d",&s_level);
                while((ch=getchar())!=10)
                {
                        if(ch!=' ')
                                buf[start++]=ch;
                }
                buf[start]='\0';
                printf("Case #%d: %d\n",i+1,alGorithm());
        }
}
int main(int argc,char*argv[])
{
        input(argv[1]);
}
