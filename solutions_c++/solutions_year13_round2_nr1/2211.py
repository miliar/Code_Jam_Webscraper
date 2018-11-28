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
    int a[105], s;
    fscanf(fp, "%d", &t);
    for(int k=1;k<=t;k++) {
       int r = 0, res = 0;
       fscanf(fp, "%d%d", &s, &n);
       for(int i=0;i<n;i++) fscanf(fp, "%d", &a[i]);
       sort(a, a+n);
       r = s;
       if(s < 2) res = n;
       else
       for(int i=0;i<n;i++) {
           if(a[i] < r) {
               r += a[i];
           } else {
                int r1 = r, c = 0;
                while(r1 <= a[i]) {c++, r1 = 2*r1 - 1;}
                if(c < n-i) {
                   res += c;
                   r = r1 + a[i];
                } else {
                   res += n-i;
                   break;
                }
           }
       }
       fprintf(ofp, "Case #%d: %d\n", k, res);
    }           
    fclose(fp);
    fclose(ofp); 
    system("pause");
    return 0;
}
