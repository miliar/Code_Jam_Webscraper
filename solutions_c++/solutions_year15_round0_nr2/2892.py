#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> p;
int dp[1234];

bool compare(int a, int b){
    return a>=b;
}

int main(){
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");
    int test;
    fscanf(fin, "%d",&test);
    for(int z=1;z<=test;z++){
        int platenum, tmp, cnt;
        fscanf(fin, "%d",&platenum);
        p.resize(1002);
        for(int i=0;i<platenum;i++){
            fscanf(fin, "%d",&tmp);
            p[tmp]++;
        }
        int nowmax, nextmax;
        int minnum=1005;

        nowmax=1001;

        while(p[--nowmax]==0);
        nextmax = nowmax;
        //while(p[--nextmax]==0);
        for(int i=1;i<=1000;i++){
            cnt = 0;
            int j=0;
            if(i>nowmax) break;
            while(j<=nowmax){
                if(p[j]==0){
                    j++;
                    continue;
                }
                cnt +=p[j]*((j-1)/i);
                j++;
            }
            minnum = (minnum>cnt+i) ? cnt+i : minnum;
        }
        fprintf(fout, "Case #%d: %d\n", z, minnum);
        p.resize(0);
    }
}
