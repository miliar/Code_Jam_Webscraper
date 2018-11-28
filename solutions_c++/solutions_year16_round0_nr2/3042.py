#include <bits/stdc++.h>
#include <windows.h>
using namespace std;
typedef long long LL;
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#define lson l, m, rt<<1
#define rson m+1, r, rt<<1|1

int main()
{
    FILE *fp1=fopen("out2.txt", "r");
    FILE *fp2=fopen("out.txt", "r");
    char s1[1000005], s2[1000005];
    int d=1;
    while(fgets(s1, sizeof(s1),  fp1))
    {
        fgets(s2, sizeof(s2), fp2);
        int len1=strlen(s1);
        int len2=strlen(s2);
        if(len1!=len2)
        {
            printf("%d\n", d);
            puts(s1), puts(s2);
			sleep(1000000);
            return 0;
        }
        for(int i=0, j=0;i<len1;i++, j++)
            if(s1[i]!=s2[j])
            {
                printf("%d\n", d);
                puts(s1), puts(s2);
				sleep(1000000);
                return 0;
            }
        d++;
    }
    puts("ok!");
    return 0;
}

