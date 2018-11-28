#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <math.h>

#define MAX 10000000

using namespace std;

int squareFair[10005],s=1;

bool checkPalindrome(long long x){
    int digit[20],s=0;
    while(x!=0){
        digit[s++] = x%10;
        x/=10;
    }
    for(int i=0;i<s;i++){
        if(digit[i]!=digit[s-1-i]){
            return false;
        }
    }
    return true;
}

int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    int zz,tt;
    scanf("%d",&zz);
    int i,j;
    int a,b;
    for(i=1;i<=MAX;i++){
        if(checkPalindrome(i) && checkPalindrome(i*i)){
            squareFair[s++] = i;
        }
    }
    for(int tt=1;tt<=zz;tt++){
        scanf("%d %d",&a,&b);
        int aa = (int)sqrt(a-1)+1,bb = (int)sqrt(b);
        int x = upper_bound(squareFair,squareFair+s+1,bb)-squareFair -1;
        int y = lower_bound(squareFair,squareFair+s+1,aa)-squareFair -1;
        printf("Case #%d: %d\n",tt,x-y);
    }
	return 0;
}
/*
3
1 4
10 120
100 1000
*/
