#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define fi "A-large.in"
#define fo "a.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int ntest, maxn;
char s[1010];

void input();
void output();

int solve(){
    int i;
    int ketqua, sum;
    
    ketqua = 0;
    sum = 0;
    
    for(i=0;i<=maxn;i++){
        if(i != 0 && s[i] != '0'){
            ketqua += sum >= i ? 0 : i - sum;
            sum += sum >= i ? 0 : i - sum;
        }
        sum += (s[i] -'0');
    }
    
    return ketqua;
}

void input()
{
     int i;
     scanf("%d",&ntest);
     for(i=0;i<ntest;i++){
         scanf("%d %s",&maxn, &s);
         printf("Case #%d: %d\n", i+1, solve());
     }
}

void output()
{
}

int main() {
	
	//freopen(fi,"r",stdin);
	//freopen(fo,"w",stdout);
	
	input();
	
	return 0;
}
