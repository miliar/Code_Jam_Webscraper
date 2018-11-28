#include<stdio.h>
#include<map>
int a[1000001];
int r,f;
int cnt, cnt2;
using namespace std;

long long int minimum(long long int a,long long int b){
	if(a == 0) return b;
	if(b == 0) return a;
	if(a>b)
		return b;
	return a;
}

long long int reverse(long long int n){
	long long int result = 0;
	int chk = 0;
	while(n){
		result = result * 10 + n%10;
		n/=10;
		chk = 1;
	}
	return result;
}

int main() {
	FILE *fi=fopen("input.txt","r");
	FILE *fo=fopen("output.txt","w");
	int test,p,temp, temp2, temp3;
	long long int n,i,x;

	fscanf(fi,"%d",&test);

	for(p=1;p<=test;p++){
		fscanf(fi,"%lld",&n);

		map<long long int, int> map;
		r = f= 0;
		a[r++] = 1;
		map[1] = 1;
		while(1){
			if(r == f) break;
			x = a[f++];
			if(x == n)
				break;
			temp = map[x];
			temp2 = map[x+1];
			if(temp2 == 0 || temp2 > temp+1){
				map[x+1] = temp + 1;
				a[r++] = x+1;
				if(x+1 == n)
					break;
			}
			temp3 = reverse(x);
			temp2 = map[temp3];
			if(temp2 == 0 || temp2 > temp + 1){
				map[temp3] = temp+1;
				a[r++] = temp3;
				if(temp3 == n)
					break;
			}
		}
		fprintf(fo,"Case #%d: %lld\n",p,map[n]);
	}
	return 0;
}
//10000 0000 0000 00
