#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;

int main(){
    FILE *fp, *fpo;
    fp = fopen("b.in", "r");
    fpo = fopen("b.out", "w");
    
    int t;
    fscanf(fp, "%d", &t);
    for(int i = 1; i <= t; i++){
        char s[105];
        fscanf(fp, "%s", s);
        int len = strlen(s);
        
        char now = s[0];
        int cnt = 0;
        for(int j = 1; j < len; j++){
            if(s[j] != now){
                cnt++;
                now = s[j];
            }
        }
        
        if(s[len - 1] == '-')
            cnt++;
        fprintf(fpo, "Case #%d: %d\n", i, cnt);
    }
}