#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <sstream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>

using namespace std;

int pos[26];

int getZERO()
{
    if(pos['Z'-65]&&pos['E'-65]&&pos['R'-65]&&pos['O'-65])
    {
        pos['Z'-65]--;
        pos['E'-65]--;
        pos['R'-65]--;
        pos['O'-65]--;
        return 1;
    }
    return 0;
}

int getONE()
{
    if(pos['O'-65]&&pos['N'-65]&&pos['E'-65])
    {
        pos['O'-65]--;
        pos['N'-65]--;
        pos['E'-65]--;
        return 1;
    }
    return 0;
}

int getTWO()
{
    if(pos['T'-65]&&pos['W'-65]&&pos['O'-65])
    {
        pos['T'-65]--;
        pos['W'-65]--;
        pos['O'-65]--;
        return 1;
    }
    return 0;
}

int getTHREE()
{
    if(pos['T'-65]&&pos['H'-65]&&pos['R'-65]&&(pos['E'-65]>1))
    {
        pos['T'-65]--;
        pos['H'-65]--;
        pos['R'-65]--;
        pos['E'-65]-=2;
        return 1;
    }
    return 0;
}

int getFOUR()
{
    if(pos['F'-65]&&pos['O'-65]&&pos['U'-65]&&pos['R'-65])
    {
        pos['F'-65]--;
        pos['O'-65]--;
        pos['U'-65]--;
        pos['R'-65]--;
        return 1;
    }
    return 0;
}

int getFIVE()
{
    if(pos['F'-65]&&pos['I'-65]&&pos['V'-65]&&pos['E'-65])
    {
        pos['F'-65]--;
        pos['I'-65]--;
        pos['V'-65]--;
        pos['E'-65]--;
        return 1;
    }
    return 0;
}

int getSIX()
{
    if(pos['S'-65]&&pos['I'-65]&&pos['X'-65])
    {
        pos['S'-65]--;
        pos['I'-65]--;
        pos['X'-65]--;
        return 1;
    }
    return 0;
}
int getSEVEN()
{
    if(pos['S'-65]&&(pos['E'-65]>1)&&pos['V'-65]&&pos['N'-65])
    {
        pos['S'-65]--;
        pos['E'-65]-=2;
        pos['V'-65]--;
        pos['N'-65]--;
        return 1;
    }
    return 0;
}

int getEIGHT()
{
    if(pos['E'-65]&&pos['I'-65]&&pos['G'-65]&&pos['H'-65]&&pos['T'-65])
    {
        pos['E'-65]--;
        pos['I'-65]--;
        pos['G'-65]--;
        pos['H'-65]--;
        pos['T'-65]--;
        return 1;
    }
    return 0;
}

int getNINE()
{
    if((pos['N'-65]>1)&&pos['I'-65]&&pos['E'-65])
    {
        pos['N'-65]-=2;
        pos['I'-65]--;
        pos['E'-65]--;
        return 1;
    }
    return 0;
}

int main()
{
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    int t,i,j;
    scanf("%d",&t);
    getchar();
    for(i=0;i<t;i++)
    {
        string s;
        getline(cin,s);
        memset(pos,0,sizeof(pos));
        for(j=0;j<s.length();j++)
        {
            pos[s[j]-65]++;
        }
        vector<int> num;
        while(getZERO())
        {
            num.push_back(0);
        }
        while(getEIGHT())
        {
            num.push_back(8);
        }
        while(getSIX())
        {
            num.push_back(6);
        }
        while(getSEVEN())
        {
            num.push_back(7);
        }
        while(getTWO())
        {
            num.push_back(2);
        }
        while(getFIVE())
        {
            num.push_back(5);
        }
        while(getFOUR())
        {
            num.push_back(4);
        }
        while(getONE())
        {
            num.push_back(1);
        }
        while(getTHREE())
        {
            num.push_back(3);
        }
        while(getNINE())
        {
            num.push_back(9);
        }
        /*for(j=0;j<26;j++)
        {
            if(pos[j]>0)
            {
                printf("FUCK\n");
                break;
            }
        }*/
        printf("Case #%d: ",i+1);
        sort(num.begin(),num.end());
        for(j=0;j<num.size();j++)
        {
            printf("%d",num[j]);
        }
        printf("\n");

    }
}
