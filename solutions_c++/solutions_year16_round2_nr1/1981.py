#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t,i,j,k;

    scanf("%d",&t);
    k=0;

    while(t--)
    {
        k++;
        char str[2010];
        scanf("%s",str);
        int hash[26]= {0};

        for(i=0; i<strlen(str); i++)
            hash[str[i]-'A']++;

        int num[10]= {0};

        if(hash['Z'-'A'] > 0)
        {
            num[0]=hash['Z'-'A'];
            hash['E'-'A']-=num[0];
            hash['R'-'A']-=num[0];
            hash['O'-'A']-=num[0];
            hash['Z'-'A']-=num[0];

        }

        if(hash['W'-'A'] > 0)
        {
            num[2]=hash['W'-'A'];
            hash['T'-'A']-=num[2];
            hash['O'-'A']-=num[2];
            hash['W'-'A']-=num[2];

        }

        if(hash['U'-'A'] > 0)
        {
            num[4]=hash['U'-'A'];
            hash['F'-'A']-=num[4];
            hash['O'-'A']-=num[4];
            hash['R'-'A']-=num[4];
            hash['U'-'A']-=num[4];

        }

        if(hash['X'-'A'] > 0)
        {
            num[6]=hash['X'-'A'];
            hash['S'-'A']-=num[6];
            hash['I'-'A']-=num[6];
            hash['X'-'A']-=num[6];

        }

        if(hash['G'-'A'] > 0)
        {
            num[8]=hash['G'-'A'];
            hash['E'-'A']-=num[8];
            hash['I'-'A']-=num[8];
            hash['H'-'A']-=num[8];
            hash['T'-'A']-=num[8];
            hash['G'-'A']-=num[8];

        }

        if(hash['F'-'A'] > 0)
        {
            num[5]=hash['F'-'A'];
            hash['I'-'A']-=num[5];
            hash['V'-'A']-=num[5];
            hash['E'-'A']-=num[5];
            hash['F'-'A']-=num[5];

        }

        if(hash['V'-'A'] > 0)
        {
            num[7]=hash['V'-'A'];
            hash['S'-'A']-=num[7];
            hash['N'-'A']-=num[7];
            hash['E'-'A']-=(2*num[7]);
            hash['V'-'A']-=num[7];

        }

        if(hash['H'-'A'] > 0)
        {
            num[3]=hash['H'-'A'];
            hash['T'-'A']-=num[3];
            hash['R'-'A']-=num[3];
            hash['E'-'A']-=(2*num[3]);
            hash['H'-'A']-=num[3];

        }

        if(hash['O'-'A'] > 0)
        {
            num[1]=hash['O'-'A'];
            hash['N'-'A']-=num[1];
            hash['E'-'A']-=(num[1]);
            hash['O'-'A']-=num[1];

        }

        if(hash['I'-'A'] > 0)
        {
            num[9]=hash['I'-'A'];
            hash['E'-'A']-=num[7];
            hash['N'-'A']-=(2*num[7]);
            hash['I'-'A']-=num[7];

        }

        printf("Case #%d: ",k);
        for(i=0;i<10;i++)
            for(j=0;j<num[i];j++)
                printf("%d",i);
        printf("\n");
    }

    return 0;
}
