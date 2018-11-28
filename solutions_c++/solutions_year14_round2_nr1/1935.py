#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <assert.h>
#include<string>
#include <cmath>
#include <algorithm>
using namespace std;
char s[105][105];
int main()
{
    int t, n;
	FILE *fp = fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    fscanf(fp, "%d", &t);
    for(int k = 1;k <= t; k++) {
       fscanf(fp, "%d", &n);
       for(int i = 0; i < n ; i++)
           fscanf(fp, "%s", &s[i]);
       int c = 1, c1 = 1, res = -1;
       if(s[0][0] != s[1][0])
            goto prr;
       res = 0;
       while(true) {
            if(s[0][c] == s[1][c1] && s[0][c] == '\0')
                break;
            if(s[0][c] == s[1][c1]) {
                c++;
                c1++;
                continue;
            }
            if((s[0][c - 1] == s[1][c1 - 1]) && (s[1][c1] == s[1][c1 - 1])) {
                res++;
                c1++;
                continue;
            }
            if(s[0][c - 1] == s[1][c1 - 1] && (s[0][c] == s[0][c - 1])) {
                res++;
                c++;
                continue;
            }   
            res = -1;
            break;
       }
prr:
       if(res == -1)
           fprintf(ofp, "Case #%d: Fegla Won\n", k);
        else fprintf(ofp, "Case #%d: %d\n", k, res);
    }           
    fclose(fp);
    fclose(ofp); 
    system("pause");
    return 0;
}
