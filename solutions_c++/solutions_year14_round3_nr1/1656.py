#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
using namespace std;

int gcd(int a, int b) {

    while (b != 0) {
    int temp = a % b;
    a = b;
    b = temp;
    }

    return abs(a);

}

int main(void)
{
    int i,j,n,cnt;
    double r_x,r_y;
    long x,y;

    FILE *in = fopen("input.txt","r");
    FILE *out = fopen("output.txt","w");

    fscanf(in,"%d",&n);

    for (i=0; i<n; i++){
        fscanf(in,"%ld/%ld",&x,&y);

        r_y = (double)y;
        r_x = (double)x;

        y = y / gcd(x,y);

        while (y>1){
            if (y%2 != 0){
                break;
            }
            y=y/2;
        }

        if (y!=1 || r_x>r_y){
            fprintf(out,"Case #%d: impossible\n",i+1);
            continue;
        }

        if (r_x==r_y){
            fprintf(out,"Case #%d: 0\n",i+1);
            continue;
        }

        cnt = 1;
        while (r_y/r_x > 2.0){
            r_x = r_x * 2.0;
            cnt++;
        }

        fprintf(out,"Case #%d: %d\n",i+1,cnt);
    }

    return 0;
}
