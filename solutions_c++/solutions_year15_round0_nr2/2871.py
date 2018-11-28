#include <iostream>
#include <fstream>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define fi "b.inp"
#define fo "b.out"
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int ntest, n, a[100010], maxx;

void input();
void output();

int solve(){
    int i, j;
    int ketqua, temp;
    
    ketqua = maxx;
    
    for(i=1;i<=maxx;i++){
        temp = i;
        for(j=0;j<n;j++){
            if(a[j] > i){
                temp += ((a[j] - 1) / i);
            }
        }
        
        ketqua = min(ketqua, temp);
    }
    
    return ketqua;
}

void input()
{
    int i, j;
    int temp;
    
    scanf("%d",&ntest);
    
    for(i=0;i<ntest;i++){
        scanf("%d",&n);
        
        maxx = -1;
        
        for(j=0;j<n;j++){
            scanf("%d",&a[j]);
            maxx = max(maxx, a[j]);
        }
        
        printf("Case #%d: %d\n",i+1, solve());
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
