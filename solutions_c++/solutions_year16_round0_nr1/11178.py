#include "iostream"
#include "cmath"
#include "cstdio"

using namespace std;
int t, n, len, cur, *check = new int[10], index, done = 0;
void reset(){
	for(int i = 0; i < 10; i++)check[i] = 0;
}
bool find(){
	for(int i = 0; i < (int)ceil(log10(cur + 0.5)); i++){
		index = (cur / (int)pow(10, i)) % 10;
		if(!check[index]){
			check[index] = 1;
			done++;
		}
	}
	return done == 10;
}
int main(){
	freopen("A-large.in","r",stdin);
	scanf("%d", &t);
	for(int i = 0; i < t; i++){
		done = 0;
		scanf("%d", &n);
		len = (int)pow(10,ceil(log10(n) + 1));
		for(int j = 1; j <= len; j++){
			cur  = n * j;
			if(find()){reset(); printf("Case #%d: %d\n", i+1, cur); break;}	
		}
		if(done != 10)printf("Case #%d: INSOMNIA\n", i+1);
	}

	return 0;
}