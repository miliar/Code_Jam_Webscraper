#include<stdio.h>
#include<iostream>
#include<vector>
#include<stack>
#include<utility>//pair
#include<functional>//greater
#include<queue>
#include<string.h>
#include<algorithm>
#include<math.h>
#define mod 1000000007//10^9+7
#define pp(a,b) make_pair(a,b)
/*#include<fstream>
ifstream fin("in.txt");
ofstream fout("out.txt");*/
using namespace std;

int main()
{
    int cd[10]={0},cc[26]={0};
    int t,c=1,l;
    char s[2004];
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",s);
        l=strlen(s);
        for(int i=0;i<10;i++)
            cd[i]=0;
        for(int i=0;i<26;i++)
            cc[i]=0;
        for(int i=0;i<l;i++)
            cc[s[i]-65]++;
        cd[0]=cc[25];
        cd[2]=cc[22];
        cd[4]=cc[20];
        cd[6]=cc[23];
        cd[8]=cc[6];
        cd[1]=cc[14]-cd[2]-cd[4]-cd[0];
        cd[3]=cc[7]-cd[8];
        cd[5]=cc[5]-cd[4];
        cd[7]=cc[18]-cd[6];
        cd[9]=cc[8]-cd[8]-cd[6]-cd[5];
        printf("Case #%d: ",c);
        for(int i=0;i<10;i++)
            while(cd[i]>0)
            {
                printf("%d",i);
                cd[i]--;
            }
        printf("\n");
        c++;
    }
    return 0;
}

