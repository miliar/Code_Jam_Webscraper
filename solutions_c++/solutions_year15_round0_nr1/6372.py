#include<iostream>
#include<cstring>
#include<stdlib.h>
#include<fstream>

using namespace std;

int frndReq(int smax,char *shyness)
{
    int frnd_count=0;
    int i,len=strlen(shyness);
    int standing=shyness[0]-'0';
    for(i=1;i<len;i++)
    {
        if(i-standing-frnd_count>0)
        {
            frnd_count++;
        }
        standing=standing+(shyness[i]-'0');
    }
    return frnd_count;
}

int main(void)
{
    freopen("standing_ovation_large.txt", "r", stdin);
    freopen("Question_1_large.txt", "w", stdout);
    int i,t,smax;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>smax;
        char shyness[smax+2];
        cin>>shyness;
        int req=frndReq(smax,shyness);
        cout<<"Case #"<<i<<": "<<req<<endl;
    }
    return 0;
}
