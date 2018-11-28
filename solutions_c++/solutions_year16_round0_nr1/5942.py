#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>

using namespace std;

bool num[10];
int cs,n;
char str[100];

void tryn(int w)
{
    sprintf(str,"%d",w);
    for(int i=0;i<strlen(str);i++)
    {
        num[str[i]-'0']=true;
    }
}

int main()
{
    //freopen("A-large.in","r",stdin);
    //freopen("output.txt","w",stdout);
    cin>>cs;
    for(int css=0; css<cs; css++)
    {
        cin>>n;
        for(int i=0; i<10; i++)
        {
            num[i]=false;
        }
        for(int i=1; i<1000; i++)
        {
            tryn(n*i);
            bool flag=true;
            for(int j=0; j<10; j++)
            {
                if(num[j]==false)
                {
                    flag=false;
                }
            }
            if(flag)
            {
                cout<<"Case #"<<css+1<<": "<<n*i<<endl;
                break;
            }
        }
        bool flagg=true;
        for(int j=0; j<10; j++)
        {
            if(num[j]==false)
            {
                flagg=false;
            }
        }
        if(flagg==false)
        {
            cout<<"Case #"<<css+1<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
