#include <bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fin = fopen("input.txt","r");
    FILE *fout = fopen("output.txt","w");
    char aud[1005];
    int sum, mx, n;
    int i, j, ans, tt;
    fscanf(fin,"%d",&n);
    for(i=1; i<=n; i++) {
        fscanf(fin,"%d",&mx);
        fscanf(fin,"%s",&aud);
        sum = 0; ans = 0;
        for(j=0; j<=mx; j++) {
            tt = aud[j] - '0';
            if(sum < j && tt > 0) {
                ans += (j-sum);
                sum = j;
            }
            sum += tt;
        }
        fprintf(fout,"Case #%d: %d\n",i,ans);
    }
    fclose(fin);
    fclose(fout);
    return 0;
}
