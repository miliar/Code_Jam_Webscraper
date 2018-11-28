#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;
int ans[105][13];
int num_al[200];

void clr()
{
    for(int i=0;i<190;i++)
        num_al[i]=0;
}

main()
{
    int cas;
    freopen("output.txt","w",stdout);
    scanf("%d",&cas);
    for(int i=0;i<cas;i++)
    {
        char temp[2005];
        int o=0;
        clr();
        scanf("%s",temp);
        for(int m=0;m<strlen(temp);m++)
            num_al[temp[m]]++;
        while(num_al['Z']>0)
        {
            ans[i][0]++;
            o++;
            num_al['Z']--;
            num_al['E']--;
            num_al['R']--;
            num_al['O']--;
        }
        while(num_al['X']>0)
        {
            ans[i][6]++;
            o++;
            num_al['S']--;
            num_al['I']--;
            num_al['X']--;
        }
        while(num_al['S']>0)
        {
            ans[i][7]++;o++;
            num_al['S']--;
            num_al['E']--;
            num_al['V']--;
            num_al['E']--;
            num_al['N']--;
        }
        while(num_al['U']>0)
        {
            ans[i][4]++;o++;
            num_al['F']--;
            num_al['O']--;
            num_al['U']--;
            num_al['R']--;
        }
        while(num_al['W']>0)
        {
            ans[i][2]++;o++;
            num_al['T']--;
            num_al['W']--;
            num_al['O']--;
        }
        while(num_al['O']>0)
        {
            ans[i][1]++;o++;
            num_al['O']--;
            num_al['N']--;
            num_al['E']--;
        }
        while(num_al['F']>0)
        {
            ans[i][5]++;o++;
            num_al['F']--;
            num_al['I']--;
            num_al['V']--;
            num_al['E']--;
        }
        while(num_al['N']>1)
        {
            ans[i][9]++;o++;
            num_al['N']--;
            num_al['I']--;
            num_al['N']--;
            num_al['E']--;
        }
        while(num_al['G']>0)
        {
            ans[i][8]++;o++;
            num_al['E']--;
            num_al['I']--;
            num_al['G']--;
            num_al['H']--;
            num_al['T']--;
        }
        while(num_al['T']>0)
        {
            ans[i][3]++;o++;
            num_al['T']--;
            num_al['H']--;
            num_al['R']--;
            num_al['E']--;
            num_al['E']--;
        }
    }
    for(int i=0;i<cas;i++)
    {
        printf("Case #%d: ",i+1);
        for(int m=0;m<=9;m++)
        {
            while(ans[i][m]>0)
            {
                printf("%d",m);
                ans[i][m]--;
            }
        }
        printf("\n");
    }
}
