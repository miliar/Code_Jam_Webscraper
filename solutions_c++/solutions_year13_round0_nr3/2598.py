#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <math.h>

using namespace std;

typedef long long int llint;

#define TAM 124

llint A,B;

bool is_palindromo(llint x){
    char xc[TAM];
    int k = 0;
    while(x > 0){
            xc[k++] = x%10;
            x/=10;
    }

    for(int i = 0 ; i < k ; i ++) if(xc[i] != xc[k-i-1]) return false;

    return true;
}


llint conta(llint inf, llint sup){
    llint ans = 0;
    for(llint i = inf ; i <= sup ;i++){
        llint i2 = i*i;
        if(is_palindromo(i) && is_palindromo(i2) && i2 >= A && i2 <= B) ans++;
    }
    return ans;
}

int main(){
	int nt;
	FILE *in = fopen("C.in","r");
	FILE *out = fopen("C.out","w");

	fscanf(in," %d",&nt);
	for(int t = 1 ; t <= nt ; t++){
		fscanf(in," %lld %lld",&A,&B);
        long long int inf = sqrt(A);
        long long int sup = sqrt(B);

		fprintf(out,"Case #%d: %lld\n",t,conta(inf,sup));
	}

	return 0;


}
