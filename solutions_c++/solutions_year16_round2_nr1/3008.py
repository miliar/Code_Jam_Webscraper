#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int chr[30];
int ans[30];
int main()
{
    freopen("A2A.in","r",stdin);
    freopen("A2A.out","w",stdout);
    int T;
    scanf("%d",&T);
    for(int I=1;I<=T;I++)
    {
        for(int i=0;i<26;i++)
            chr[i]=0;

        string s;
        cin>>s;
        for(int i=0;i<s.size();i++)
            chr[s[i]-'A']++;

        // 0
        ans[0]+=chr['Z'-'A'];
        chr['O'-'A']-=chr['Z'-'A'];
        chr['R'-'A']-=chr['Z'-'A'];
        chr['E'-'A']-=chr['Z'-'A'];
        chr['Z'-'A']-=chr['Z'-'A'];

        // 2
        ans[2]+=chr['W'-'A'];
        chr['O'-'A']-=chr['W'-'A'];
        chr['T'-'A']-=chr['W'-'A'];
        chr['W'-'A']-=chr['W'-'A'];

        // 4
        ans[4]+=chr['U'-'A'];
        chr['F'-'A']-=chr['U'-'A'];
        chr['R'-'A']-=chr['U'-'A'];
        chr['O'-'A']-=chr['U'-'A'];
        chr['U'-'A']-=chr['U'-'A'];

        // 1
        ans[1]+=chr['O'-'A'];
        chr['E'-'A']-=chr['O'-'A'];
        chr['N'-'A']-=chr['O'-'A'];
        chr['O'-'A']-=chr['O'-'A'];

        // 5
        ans[5]+=chr['F'-'A'];
        chr['E'-'A']-=chr['F'-'A'];
        chr['V'-'A']-=chr['F'-'A'];
        chr['I'-'A']-=chr['F'-'A'];
        chr['F'-'A']-=chr['F'-'A'];

        // 3
        ans[3]+=chr['R'-'A'];
        chr['T'-'A']-=chr['R'-'A'];
        chr['H'-'A']-=chr['R'-'A'];
        chr['E'-'A']-=chr['R'-'A'];
        chr['E'-'A']-=chr['R'-'A'];
        chr['R'-'A']-=chr['R'-'A'];

        // 6
        ans[6]+=chr['X'-'A'];
        chr['S'-'A']-=chr['X'-'A'];
        chr['I'-'A']-=chr['X'-'A'];
        chr['X'-'A']-=chr['X'-'A'];

        // 7
        ans[7]+=chr['V'-'A'];
        chr['S'-'A']-=chr['V'-'A'];
        chr['N'-'A']-=chr['V'-'A'];
        chr['E'-'A']-=chr['V'-'A'];
        chr['E'-'A']-=chr['V'-'A'];
        chr['V'-'A']-=chr['V'-'A'];

        // 8
        ans[8]+=chr['G'-'A'];
        chr['I'-'A']-=chr['G'-'A'];
        chr['E'-'A']-=chr['G'-'A'];
        chr['T'-'A']-=chr['G'-'A'];
        chr['H'-'A']-=chr['G'-'A'];
        chr['G'-'A']-=chr['G'-'A'];

        // 9
        ans[9]+=chr['I'-'A'];
        chr['E'-'A']-=chr['I'-'A'];
        chr['N'-'A']-=chr['I'-'A'];
        chr['N'-'A']-=chr['I'-'A'];
        chr['I'-'A']-=chr['I'-'A'];

        printf("Case #%d: ",I);
        for(int i=0;i<10;i++)
            while(ans[i]>0)
            {
                printf("%d",i);
                ans[i]--;
            }
        printf("\n");
    }

}
