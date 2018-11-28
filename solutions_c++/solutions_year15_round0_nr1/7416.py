/*
Name:: Vivek Kumar Yadav
Language:: C++
Handle:: vivekjnv93
*/
#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
#include<set>
#include<list>
#include<string>
#include<cstring>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;




typedef long int li;
typedef long long int lli;
typedef long double ld;
/*-------------------------------------
-------------Hello World---------------
--------------------------------------*/

char str[1009];

int main()
{
    FILE *fp = fopen("input.in","r");
    FILE *fw = fopen("out.txt","w");
    int t,n,i,j,ans,stand;
    fscanf(fp,"%d",&t);
   // printf("I am in %d\n",t);
    j = 1;
    while(j<=t)
    {
        fscanf(fp,"%d",&n);
        fscanf(fp,"%s",str);
        ans = 0;
        stand = 0;
        for(i=0;i<=n;i++)
        {
            if(stand>=i)
            {
                stand = stand+str[i]-'0';
            }
            else if(str[i]!='0')
            {
                ans = ans+i-stand;
                stand = i;
                stand = stand+str[i]-'0';
            }
        }
        fprintf(fw,"Case #%d: %d\n",j,ans);
        j++;
    }
    return 0;
}
