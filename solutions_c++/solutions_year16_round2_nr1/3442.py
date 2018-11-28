#include<bits/stdc++.h>
#define MAX 10005
using namespace std;
int main()
{
    FILE *fr , *fw;
    fr=fopen("in.txt","a+");
    fw=fopen("out.txt","w+");
    int t,n;
    fscanf(fr,"%d",&t);
    for(int k=1;k<=t;k++)
    {
        char s[2005];
        int i,j;
        int a[26]={0,0,0};
        fscanf(fr,"%s",&s);
        for(i=0;i<s[i];i++)
            a[s[i]-'A']++;
        vector<int> v;
        if(a[25])
        {
            j=a[25];
            for(i=0;i<j;i++)
                v.push_back(0),a[25]--,a[4]--,a[17]--,a[14]--;
        }

        if( a[4] && a[8] && a[6] && a[7] && a[19])
        {
            j=min(min(a[8],a[6]),min(a[7],a[19]));
            j=min(a[4],j);
            for(i=0;i<j;i++)
                v.push_back(8),a[8]--,a[6]--,a[7]--,a[4]--,a[19]--;
        }


        if(a[19] && a[7] && a[17] && a[4]/2)
        {
            j=min(min(a[17],a[19]),min(a[7],a[4]/2));
            for(i=0;i<j;i++)
                v.push_back(3),a[17]--,a[19]--,a[7]--,a[4]-=2;
        }

        if(a[19] && a[22] && a[14])
        {
            j=min(a[14],min(a[19],a[22]));
            for(i=0;i<j;i++)
                v.push_back(2),a[14]--,a[19]--,a[22]--;
        }


        if(a[5] && a[14] && a[20] && a[17])
        {
            j=min(min(a[5],a[14]),min(a[20],a[17]));
            for(i=0;i<j;i++)
                v.push_back(4),a[5]--,a[14]--,a[20]--,a[17]-=1;
        }

        if(a[14] && a[13] && a[4])
        {
            j=min(a[14],min(a[13],a[4]));
            for(i=0;i<j;i++)
                v.push_back(1),a[14]--,a[4]--,a[13]--;
        }


        if(a[5] && a[8] && a[21] && a[4])
        {
            j=min(min(a[5],a[8]),min(a[21],a[4]));
            for(i=0;i<j;i++)
                v.push_back(5),a[5]--,a[8]--,a[21]--,a[4]-=1;
        }

        if( a[18] && a[8] && a[23])
        {
            j=min(a[18],min(a[23],a[8]));
            for(i=0;i<j;i++)
                v.push_back(6),a[18]--,a[23]--,a[8]--;
        }

        if( a[18] && a[4]/2 && a[21] && a[13])
        {
            j=min(min(a[18],a[4]/2),min(a[21],a[13]));
            for(i=0;i<j;i++)
                v.push_back(7),a[18]--,a[13]--,a[21]--,a[4]-=2;
        }



        if( a[13]/2 && a[8] && a[4])
        {
            j=min(min(a[13]/2,a[8]),a[4]);
            for(i=0;i<j;i++)
                v.push_back(9),a[13]-=2,a[8]--,a[4]--;
        }


        sort(v.begin(),v.end());
        fprintf(fw,"Case #%d: ",k);
        for(i=0;i<v.size();i++)
            fprintf(fw,"%d",v[i]);
        fprintf(fw,"\n");

    }
    fclose(fw);
    fclose(fr);
    return 0;
}
