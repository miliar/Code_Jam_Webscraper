#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <assert.h>
#include<string>
using namespace std;
int main()
{
    int t, n, k;
	FILE *fp=fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    char s[10][10];
    fscanf(fp, "%d", &n);
    for(int k=1;k<=n;k++) {
       int p[9] = {1,4,9,121,484,1001};
       int a, b, c = 0, d = 0;
       fscanf(fp, "%d%d", &a, &b);
       while(p[c] < a) c++;
       while(p[d] <= b) d++;
       fprintf(ofp, "Case #%d: %d\n", k, d-c);
    }           
    fclose(fp);
    fclose(ofp); 
    system("pause");
    return 0;
}
