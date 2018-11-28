#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;

char s[2010];
int freq[256];
map<char,int> mp;
vector<int> ans;

void init()
{
    memset(freq,0,sizeof(freq));
    ans.clear();
    mp.clear();
}

int main()
{
    int i,l,t,ansl,count,T;
    scanf("%d",&T);
    for (t=1;t<=T;t++)
    {
        init();
        printf("Case #%d: ",t);
        scanf("%s",s);
        l=strlen(s);
        for (i=0;i<l;i++)
            mp[s[i]]++;
        count=mp['Z'];
        for (i=0;i<count;i++)
            ans.push_back(0);
        mp['Z']-=count;
        mp['E']-=count;
        mp['R']-=count;
        mp['O']-=count;

        count=mp['W'];
        for (i=0;i<count;i++)
            ans.push_back(2);
        mp['T']-=count;
        mp['W']-=count;
        mp['O']-=count;

        count=mp['X'];
        for (i=0;i<count;i++)
            ans.push_back(6);
        mp['S']-=count;
        mp['I']-=count;
        mp['X']-=count;

        count=mp['S'];
        for (i=0;i<count;i++)
            ans.push_back(7);
        mp['S']-=count;
        mp['E']-=count;
        mp['V']-=count;
        mp['E']-=count;
        mp['N']-=count;

        count=mp['V'];
        for (i=0;i<count;i++)
            ans.push_back(5);
        mp['F']-=count;
        mp['I']-=count;
        mp['E']-=count;
        mp['V']-=count;

        count=mp['F'];
        for (i=0;i<count;i++)
            ans.push_back(4);
        mp['F']-=count;
        mp['U']-=count;
        mp['R']-=count;
        mp['O']-=count;
        
        count=mp['O'];
        for (i=0;i<count;i++)
            ans.push_back(1);
        mp['O']-=count;
        mp['N']-=count;
        mp['E']-=count;

        count=mp['N'];
        count=count/2;
        for (i=0;i<count;i++)
            ans.push_back(9);
        mp['N']-=2*count;
        mp['I']-=count;
        mp['E']-=count;

        count=mp['G'];
        count=count;
        for (i=0;i<count;i++)
            ans.push_back(8);
        mp['E']-=count;
        mp['I']-=count;
        mp['G']-=count;
        mp['H']-=count;
        mp['T']-=count;

        count=mp['T'];
        count=count;
        for (i=0;i<count;i++)
            ans.push_back(3);
        mp['H']-=count;
        mp['R']-=count;
        mp['E']-=count;
        mp['E']-=count;
        mp['T']-=count;

        sort(ans.begin(),ans.end());
        for (i=0;i<ans.size();i++)
            printf("%d",ans[i]);
        printf("\n");
    }
}
