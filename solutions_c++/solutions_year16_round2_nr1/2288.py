#include<bits/stdc++.h>
using namespace std;
int main()
{
    int has[26];
    char ar[100100];
    int so[10];
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int fu=1;fu<=t;fu++)
    {

        memset(has,0,sizeof(has));
        memset(so,0,sizeof(so));
        cin>>ar;
        for(int i=0;i<strlen(ar);i++)
        {
            has[ar[i]-'A']++;
        }
        printf("Case #%d: ",fu);
        while(has[22]>0)
        {
            has[22]--;
            has[19]--;
            has[14]--;
            so[2]++;
        }
        while(has[20]>0)
        {
            has[20]--;
            has[5]--;
            has[14]--;
            has[17]--;
            so[4]++;
        }
        while(has[25]>0)
        {

            has[25]--;
            has[4]--;
            has[17]--;
            has[14]--;
            so[0]++;
        }
        while(has[6]>0)
        {

            has[6]--;
            has[4]--;
            has[8]--;
            has[7]--;
            has[19]--;
            so[8]++;

        }
        while(has[23]>0)
        {

            has[23]--;
            has[18]--;
            has[8]--;
            so[6]++;
        }
        while(has[14]>0)
        {

            has[14]--;
            so[1]++;
            has[13]--;
            has[4]--;
        }
        while(has[19]>0)
        {

            has[19]--;
            so[3]++;
            has[7]--;
            has[17]--;
            has[4]--;
            has[4]--;
        }
        while(has[5]>0)
        {
            has[5]--;
            has[8]--;
            so[5]++;
            has[21]--;
            has[4]--;
        }
        while(has[18]>0)
        {

            has[18]--;
            so[7]++;
            has[4]--;
            has[4]--;
            has[21]--;
            has[13]--;
        }
        while(has[8]>0)
        {
            has[8]--;
            so[9]++;
            has[13]--;
            has[13]--;
            has[4]--;
        }
        for(int i=0;i<10;i++)
        {
            for(int j=0;j<so[i];j++)
                printf("%d",i);
        }
        printf("\n");





    }

}
