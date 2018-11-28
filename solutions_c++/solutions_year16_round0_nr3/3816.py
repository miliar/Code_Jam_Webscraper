#include<iostream>
#include<algorithm>
#include<cmath>
#define lld long long
using namespace std;

FILE *fin = fopen("C-small-attempt1.in", "r");
FILE *fout = fopen("C-small-attempt1.out", "w");

int digitlen(lld num) {
	int ret=0;
	while( num ) {
		ret+=1;
		num/=2;
	}
	return ret;
}
lld fastpower(lld a, lld p, lld mod) {
	int len = digitlen(p);
	long long bit, res=1;
	for ( int i=0; i<len; ++i ) {
		res = (res*res)%mod;
		bit = 1ll<<(len-i-1);
		if (p&bit) {
			res = (res*a)%mod;
		}
	}
	return res;
}
//fermat
bool isprime(lld p) {
	//2^(p-1)%p==1
	if ( fastpower(2,p-1,p)==1 ) {
		return true;
	}
	else {
		return false;
	}
}

lld array2lld(int *d, int N, int hex) {
	lld ret=0;
	for (int i=0; i<N; ++i) {
		ret = ret*hex;
		if (d[i]) {
			ret+=d[i];
		}
	}
	return ret;
}

lld getfactor(lld num) {
	for(lld i=2; i<10000; i++){
		if(num%i==0) {
			return i;
		}
	}
	return 0;
}

bool checkvalid(int *data, int N) {
	for ( int hex=2; hex<=10; ++hex) {
		lld num = array2lld(data, N, hex);
		if ( isprime(num) || getfactor(num)==0 ) {
			return false;
		}
	}
	return true;
}

void work(int N, int J) {
	int data[33], anscnt=0;
	data[0] = data[N-1] = 1;
	for ( int i=0; i<pow(2,N-2); ++i ) {
		//printf("test %d:\n", i);
		for ( int bit=0; bit<N-2; ++bit ) {
			if ( i&(1<<bit) ) {
				data[bit+1] = 1;
			}
			else {
				data[bit+1] = 0;
			}
		}
		if ( checkvalid(data, N) ) {
			//printf("%d ", anscnt+1);
			for ( int i=0; i<N; ++i ) {
				fprintf(fout, "%d", data[i]);
				//printf("%d", data[i]);
			}
			bool flag=1;
			for ( int hex=2; hex<=10; ++hex ) {
				lld num = array2lld(data, N, hex);
				lld factor = getfactor(num);
				//printf("HEX:%d %lld\n", hex, num);
				fprintf(fout, " %d", factor);
				//printf(" %lld", factor);
			}
			fprintf(fout, "\n");
			//printf("\n");
			anscnt+=1;
		}
		if (anscnt>=J) {
			return;
		}
	}
	return ;
}

int main() {
	int Cases, N, J;
	//printf("%d", fastpower(2, 550725931008, 550725931009));
	fscanf(fin, "%d", &Cases);
	for( int cases=1; cases<=Cases; ++cases) {
		fscanf(fin, "%d %d", &N, &J);
		fprintf(fout, "Case #%d:\n", cases);
		work(N, J);
	}
	return 0;
}
