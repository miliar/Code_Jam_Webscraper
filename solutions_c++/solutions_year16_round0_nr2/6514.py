#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int GetLeastTimes();
bool Success();
char S[105];
int main()
{
        freopen("B-large.in","r",stdin);
        freopen("output.out","w",stdout);
        int T,rnd=0,leastTimes;
        cin>>T;
        while(T--)
        {
                ++rnd;
                cin>>S;
                leastTimes=GetLeastTimes();
                printf("Case #%d: %d\n",rnd,leastTimes);
        }
        return 0;
}

int GetLeastTimes()
{
        int length=strlen(S),times=0,i;
        while(1)
        {
                if(Success())
                        return times;
                else if(S[0]=='+')
                {
                        for(i=0;i!=length&&S[i]!='-';++i);
                        for(;i!=length&&S[i]!='+';++i)
                                S[i]='+';
                        times+=2;
                        if(i==length)
                                return times;
                }
                else  if(S[0]=='-')
                {
                        for(i=0;i!=length&&S[i]!='+';++i)
                                S[i]='+';
                        for(;i!=length&&S[i]!='-';++i);
                        if(i==length)
                                return ++times;
                        else{
                                for(;i!=length&&S[i]!='+';++i)
                                        S[i]='+';
                                times+=3;
                                if(i==length)
                                        return times;
                        }
                }
        }
}

bool Success()
{
        int length=strlen(S);
        int i;
        for(i=0;i!=length;++i)
        {
                if(S[i]=='-')
                        break;
        }
        if(i==length)
                return true;
        return false;
}
