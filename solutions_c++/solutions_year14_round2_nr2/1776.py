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
int main()
{
    int t, n, a, b, k, res, k1;
	FILE *fp = fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    fscanf(fp, "%d", &t);
    for(int k = 1;k <= t; k++) {
       fscanf(fp, "%d%d%d", &a, &b, &k1);
       res = 0;
       for(int i = 0; i < a; i++)
            for(int j = 0; j < b; j++)
                if((i & j) < k1) res++; 
       fprintf(ofp, "Case #%d: %d\n", k, res);
    }           
    fclose(fp);
    fclose(ofp); 
    system("pause");
    return 0;
}
