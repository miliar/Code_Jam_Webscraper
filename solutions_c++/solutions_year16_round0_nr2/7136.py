#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<cstring>
#include<vector>
#include <cmath>

using namespace std;
#define Fill(a, b) memset(a, b, sizeof(a))
#define Debug(x) cout<<#x<<"="<<(x)<<endl;
typedef long long LL;


int main()
{
    int i = 0, j = 0, kase = 0;
    int t, ans;
    char str[150];
    int arr[150];
    FILE *fp = fopen("out.txt", "w");
    FILE *fp2 = fopen("in.txt", "r");
    fscanf(fp2, "%d", &t);
    while(t--)
    {
        fscanf(fp2, "%s", str);
        int len = strlen(str);
        for(i = 0; i < len; i++)
        {
            if(str[i] == '-')
                arr[i] = 0;
            else
                arr[i] = 1;
        }
        int start = 0;
        while(arr[start] == 0)
            start++;
        if(start)
            ans = 1;
        else
            ans = 0;
        for( ; start < len; start++)
        {
            if(arr[start] == 0 && arr[start-1]==1)
                ans += 2;
        }
        fprintf(fp, "Case #%d: %d\n", ++kase, ans);
    }

    return 0;
}






















