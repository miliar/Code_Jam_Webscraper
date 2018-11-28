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
    int m,n,k, t;
	FILE *fp=fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    fscanf(fp, "%d", &t);
    for(int k=1;k<=t;k++) {
       fscanf(fp, "%d%d", &m, &n);
       int a[105][105], r[105], c[105];
       for(int i=0;i<m;i++) {
          r[i] = -1;
          for(int j=0;j<n;j++) {
              fscanf(fp, "%d", &a[i][j]);
              if(r[i] < a[i][j]) r[i] = a[i][j];
          }
       }
       for(int j=0;j<n;j++) {
          c[j] = -1;
          for(int i=0;i<m;i++) {
              if(c[j] < a[i][j]) c[j] = a[i][j];
          }
       }
       bool flag = true;
       for(int i=0;i<m;i++) {
          for(int j=0;j<n;j++) {
              if(!(a[i][j] == r[i] || a[i][j] == c[j])) {
                 flag = false;
                 break;
              }
          }
       }
       if(flag)
         fprintf(ofp, "Case #%d: %s\n", k, "YES");
       else
         fprintf(ofp, "Case #%d: %s\n", k, "NO"); 
    }        
    fclose(fp);
    fclose(ofp); 
    system("pause");
    return 0;
}
