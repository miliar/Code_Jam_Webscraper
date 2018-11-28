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

int ntest, n, a[10010];

void input();
void output();

int mot(){
    int i;
    int ketqua;
    
    ketqua = 0;
    
    for(i=0;i<n-1;i++){
        if(a[i]>a[i+1])
            ketqua += (a[i]-a[i+1]);
    }
    
    return ketqua;
}

int check(int gt){
     int i;
     int tong;
     
     tong = 0;
     
     for(i=0;i<n-1;i++){
         if(a[i]-gt*10 > a[i+1])
             return -1;
         tong += min(a[i], gt*10);
     }
     
     return tong;
}

int hai(){
    int i;
    int ketqua, maxx;
    
    maxx = 0;
    ketqua = 0;
    
    for(i=0;i<n-1;i++){
        if(a[i]-a[i+1]>maxx)
            maxx = a[i] - a[i+1];
    }
    
    for(i=0;i<n-1;i++)
            ketqua += min(a[i], maxx);
    
    return ketqua;
}

void input()
{
     int i, j;
     scanf("%d",&ntest);
     
     for(i=0;i<ntest;i++){
         scanf("%d",&n);
         for(j=0;j<n;j++){
             scanf("%d",&a[j]);
         }
         
         printf("Case #%d: %d %d\n",i+1,mot(),hai());
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
