#include <stdio.h>
//#include <stdlib.h>
#include <algorithm>
using namespace std;

int solve(double * a, double * b, int n){
    int pa = 0, pb = 0, cnt = 0;
    
    while(pa < n && pb < n){
        if(a[pa] > b[pb]){
            //fprintf(pw, "%lf beats %lf\n", a[pa], b[pb]);
            ++cnt;
            ++pa;
            ++pb;
        }
        else ++pa;
    }
    //fprintf(pw, "\n");
    return cnt;
}

FILE * pw = stdout;
FILE * pr = stdin;

int main(){
    int ti, tn;
    int i, n;
    double a[1001], b[1001];

    pw = fopen("out.txt", "w");
    pr = fopen("in.txt", "r");
         
    fscanf(pr, "%d", &tn);
    for(ti = 1; ti <= tn ; ti++){
        fscanf(pr, "%d", &n);
        for(i=0;i<n;i++) fscanf(pr, "%lf", &a[i]);
        for(i=0;i<n;i++) fscanf(pr, "%lf", &b[i]);
        
        sort(a, a+n);
        sort(b, b+n);
    
        fprintf(pw, "Case #%d: %d %d\n", ti, solve(a, b, n), n - solve(b, a, n));
    }
    
    //system("pause");
    return 0;
}
