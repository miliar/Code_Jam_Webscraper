#include<bits/stdc++.h>
using namespace std;
#define sz 105
#define sf scanf
#define pf printf

char arr[sz],arr_c[sz],cover,take;
int main()
{
    int i,j,k,l,temp,tc,res;
    bool key1,key2;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    sf("%d",&tc);
    for(k=1; k<=tc; k++)
    {
        sf("%s",arr);
        res=0;
        key1=true;
        key2=false;
        if(strcmp(arr,"+")==0)
        {
            pf("Case #%d: %d\n",k,res);
            continue;
        }
        while(key1)
        {
            key1=key2=false;
            for(i=1; arr[i]; i++)
            {
                if(arr[i-1]!=arr[i])
                {
                    key1=true;
                    res++;
                    break;
                }
                if(arr[i]=='+') key2=true;
            }
            if(key1)
                for(j=0; j<i; j++)
                {
                    if(arr[j]=='+') arr[j]='-';
                    else arr[j]='+';
                }
            //pf("chk %s\n",arr);
        }
        if(!key2) res++;
        pf("Case #%d: %d\n",k,res);
    }
    return 0;
}

