#include <stdio.h>
#include <math.h>

int tc, n, cases, i, temp, res, maxi;
int a[15];

int rec(int v, int a2[15]) {
    /*
    for(i=0; i<15; i++) {
        printf("%d ", a2[i]);
    }
    printf("\n");
    */
    int i, temp, sqr, mini = v;
    int a3[15];
    bool b = true;
    sqr = 2;
    while(sqr<=v/2) {
        b = true;
        for(i=0; i<15; i++) {
            a3[i] = a2[i];
        }
        a3[sqr] += a3[v];
        a3[v-sqr] += a3[v];
        temp = a3[v];
        a3[v] = 0;
        for(i=v; i>0; i--) {
            if(a3[i]>0) {
                b = false;
                temp += rec(i, a3);
                break;
            }
        }
        if(!b && temp < v && mini > temp) mini = temp;
        sqr++;
    }
    return mini;
    /*
    sqr = sqrt(v);
    while(v%sqr!=0) sqr--;
    if(sqr==1) {
        a3[v/2] += a3[v];
        a3[v/2+1] += a3[v];
    } else {
        temp = v/sqr;
        a3[temp] += a3[v];
        a3[v-temp] += a3[v];
    }
    temp = a3[v];
    a3[v] = 0;
    for(i=v; i>0; i--) {
        if(a3[i]>0) {
            b = false;
            temp += rec(i, a3);
            break;
        }
    }
    if(!b && temp < v) return temp;
    else return v;
    */
}

int main() {
    scanf("%d\n", &tc);
    cases = 1;
    while(tc--) {
        scanf("%d\n", &n);
        for(i=0; i<15; i++) {
            a[i] = 0;
        }
        maxi = 0;
        for(i=0; i<n; i++) {
            scanf("%d \n", &temp);
            a[temp]++;
            if(temp>maxi) maxi = temp;
        }
        res = rec(maxi, a);
        printf("Case #%d: %d\n", cases++, res);
    }
    return 0;
}
