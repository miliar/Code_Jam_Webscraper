#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char stk[200],buf[200];
int cs;

void flip(int n)
{
    //char buf[200];
    for(int i=0;i<=n;i++)
    {
        buf[i]=stk[i];
    }
    for(int i=0;i<=n;i++)
    {
        if(buf[n-i]=='+')
        {
            stk[i]='-';
        }
        else
        {
            stk[i]='+';
        }
    }
    //cout<<"flip"<<n<<endl;
}

int main()
{
    //freopen("B-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>cs;
    for(int k=1;k<=cs;k++)
    {
        cin>>stk;
        int ct=0,len=strlen(stk);
        while(1)
        {
            int fn=-1;
            for(int i=len-1;i>=0;i--)
            {
                if(stk[i]=='-')
                {
                    fn=i;
                    break;
                }
            }
            //cout<<"fn="<<fn<<endl;
            if(fn==-1)
            {
                break;
            }
            if(stk[0]=='-')
            {
                flip(fn);
                ct++;
            }
            else
            {
                for(int i=fn-1;i>=0;i--)
                {
                    if(stk[i]=='+')
                    {
                        flip(i);
                        break;
                    }
                }
                flip(fn);
                ct+=2;
            }
        }
        printf("Case #%d: %d\n",k,ct);
    }
    return 0;
}
