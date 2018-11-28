#include <iostream>
#include <cstdio>
#include <algorithm>
#include <complex>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cstdlib>
#include <memory.h>
#include <iostream>
#include<list>
using namespace std;

#define pb push_back
#define sz size()
#define mp make_pair
#define mset(ar,val) memset(ar,val,sizeof ar)
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))


void scan(int* i) {int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}
void scan(long long int* i) {long long int t = 0;char c;bool negative = false;c = getchar_unlocked();while (c < '0' || c > '9') {if (c == '-')negative = true;c = getchar_unlocked();}while (c >= '0' && c <= '9') {t = (t << 3) + (t << 1) + c - '0';c = getchar_unlocked();}if (negative)t = ~(t - 1);*i = t;}

int main() {
	int t,T,A,N,temp,tempmoatsize;
	int i,j,curmotesize,res;
	vector<int>motes;
	scan(&T);
	for(t=1;t<=T;++t){
		motes.clear();
		scan(&A);
		curmotesize=A;
		res=0;
		scan(&N);
		for(i=0;i<N;++i){
			scan(&j);
			motes.pb(j);
		}
		std::sort(motes.begin(),motes.end());
		i=0;
		while(1){

		for(;i<N;++i){
			if(motes[i]<curmotesize)
				curmotesize+=motes[i];
			else
				break;
		}
		if(i==N) break;
		if(curmotesize==1 || curmotesize==0){
			res+=N;
			i=N;
			break;
		}
		temp=0;
		tempmoatsize=curmotesize;
		while(tempmoatsize<=motes[i]){
			++temp;
			tempmoatsize+=(tempmoatsize-1);
		}
		if(temp>=N-i){
			res+=(N-i);
			break;
		}else{
			res+=temp;
			curmotesize=tempmoatsize;
		}
		}
			printf("Case #%d: %d\n",t,res);
	}
	return 0;
}

