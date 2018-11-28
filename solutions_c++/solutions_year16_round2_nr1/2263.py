#include <cstdio>
#include<string.h>
using namespace std;
#define li long long int
int main() 
{
    int test;
    char c[2005];
    scanf("%d",&test);
    int iter;
        int i,a[26]={0};
    for(iter=1;iter<=test;iter++)
    {
        int l;
        scanf("%s",&c);
        l=strlen(c);
        printf("Case #%d: ",iter);
        for(i=0;i<l;i++)
        {
            a[c[i]-'A']++;
        }
        while(a['Z'-'A']!=0)
        {
            printf("0");
            a['E'-'A']--;
            a['Z'-'A']--;
            a['R'-'A']--;
            a['O'-'A']--;
        }
        int ans[11]={0};
        while(a['X'-'A']!=0)
        {
            ans[6]++;
            a['S'-'A']--;
            a['I'-'A']--;
            a['X'-'A']--;
        }
        while(a['S'-'A']!=0)
        {
            ans[7]++;
            a['S'-'A']--;
            a['E'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            a['N'-'A']--;
        }
        
        while(a['U'-'A']!=0)
        {
            ans[4]++;
            a['F'-'A']--;
            a['O'-'A']--;
            a['U'-'A']--;
            a['R'-'A']--;
            
        }
        while(a['W'-'A']!=0)
        {
            ans[2]++;
            a['T'-'A']--;
            a['W'-'A']--;
            a['O'-'A']--;
        }
        while(a['G'-'A']!=0)
        {
            ans[8]++;
            a['E'-'A']--;
            a['I'-'A']--;
            a['G'-'A']--;
            a['H'-'A']--;
            a['T'-'A']--;
            
        }
        
        
        while(a['T'-'A']!=0)
        {
            ans[3]++;
            a['T'-'A']--;
            a['H'-'A']--;
            a['R'-'A']--;
            a['E'-'A']--;
            a['E'-'A']--;
            
        }
        
        while(a['V'-'A']!=0)
        {
            ans[5]++;
            a['F'-'A']--;
            a['I'-'A']--;
            a['V'-'A']--;
            a['E'-'A']--;
            
        }
        while(a['O'-'A']!=0)
        {
            ans[1]++;
            a['O'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
            
        }
        while(a['N'-'A']!=0)
        {
            ans[9]++;
            a['N'-'A']--;
            a['I'-'A']--;
            a['N'-'A']--;
            a['E'-'A']--;
            
        }
        for(i=1;i<=10;i++)
        {
            while(ans[i]!=0)
            {
                printf("%d",i);
                ans[i]--;
            }
        }
        printf("\n");
    }
}
