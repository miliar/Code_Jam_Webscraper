#include<bits/stdc++.h>
using namespace std;
int test, res;
char cad[200];
int main(){
    freopen("B-large.out", "w", stdout);
    freopen("B-large.in", "r", stdin);
    ios::sync_with_stdio(false);
    scanf("%d", &test);
    for(int testCase = 1; testCase <= test; testCase++){
        scanf("%s", cad);
        int l = strlen(cad);
        res = 0;
        for(int j = 1; j < l; j++)
            if(cad[j] != cad[j - 1]) res++;
        res += (cad[l - 1] == '-');
        printf("Case #%d: %d\n", testCase, res);
    }
    fclose(stdout);
}
