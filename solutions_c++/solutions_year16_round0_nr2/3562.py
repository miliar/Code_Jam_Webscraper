typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>

using namespace std;

int main()
{
    ll t,l,c,i,j,w=1,flip,eflip,flag;
    string x;
    char val,val1;
    scanf("%lld",&t);
    while(t--)
    {
        cin>>x;
        l=x.length();
        eflip=flag=0;
        for(i=0;i<l;i++)
        {
            if(x[i]=='-')
            {
                flag=1;
            break;
            }
            else
            {
                x[i]='-';
                eflip=1;
            }
        }
        if(flag==0)
        c=0;
        else
        {
        flip=0;
        for(i=l-1;i>=0;i--)
        {
            if(flip>=1)
            val=(x[i]=='+'?'-':'+');
            else
            val=x[i];
            if(i>0)
            {
                if(flip>=1)
            val1=(x[i-1]=='+'?'-':'+');
            else
            val1=x[i-1];
            }
            if(val=='-')
            {
            if(i>0 && val1=='-')
            continue;
            else
            {
            flip++;
            if(flip>1)
            eflip+=2;
            }
            }
        }
        if(flip==0)
        c=0;
        else
        c=eflip+1;
        }
        printf("Case #%lld: %lld\n",w++,c);
        
    }
	return 0;
}