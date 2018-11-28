#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

#define dig 110
#define nh 100000
int full[dig];
int tc;
int range[10010][2][dig];
int ans[10010];

int check(){
	int r = dig-1;
	while(full[r]==0)r--;
	int l;
	for(l = 0; l <= r && full[l] == full[r]; l++,r--);
	if(l>r){
		// long long x = 0;
		// for(int i = dig-1; i >= 0; i--)x =  x*10 + full[i];
		// cout << x << endl;
		for(int ti = 0; ti < tc; ti++){
			int res1 = 0;
			for(int i = dig-1; i >= 0; i--){
				res1 = full[i] - range[ti][0][i];
				if(res1 != 0)break;
			}
			int res2 = 0;
			for(int i = dig-1; i >= 0; i--){
				res2 = range[ti][1][i] - full[i];
				if(res2 != 0)break;
			}
			// printf("%d %d\n", res1, res2);
			if(res1 >= 0 && res2 >= 0)ans[ti]++;
		}
		return true;
	}
	return false;
}

void add(long long a, int l){
	while(a>0){
		full[l] += a%10;
		a/=10;
		while(full[l] > 10){
			full[l+1]++;
			full[l]-=10;
		}
		l++;
	}
}

int gen(long long a, int b){
	for(int i = 0; i < dig; i++)
		full[i] = 0;
	int l = 0;
	long long a2 = 0;
	long long t = a;
	while(t>0){a2*=10; a2+=t%10; t/=10; l++;}
	if(a<=0){
		add(b*b,   0);
	}
	else if(b>=0){
		add(a*a,   0);
		add(a*b*2, l);
		add(a*a2*2,l+1);
		add(b*b,   l+l);
		add(a2*b*2,l+l+1);
		add(a2*a2, l+l+2);
	}else{
		add(a*a, 0);
		add(a*a2*2, l);
		add(a2*a2, l+l);
	}
	if(check()){
		// printf("%d %d %d %d:", a2,b,a,l);
		// long long x;
		// x = a2;
		// if(b>=0)x = x*10+b;
		// while(l>0){x*=10;l--;}
		// x+=a;
		// cout << x << " " << (x*x) << endl;
	}
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	scanf("%d", &tc);

	for(int i = 0; i < tc; i++){
		ans[i] = 0;
		for(int j = 0; j < dig; j++)
			range[i][0][j] = range[i][1][j] = 0;
	}

	for(int ti = 0; ti < tc; ti++){
		char in[dig];
		scanf("%s", in);
		int len = strlen(in);
		for(int i = 0; i < len; i++){
			range[ti][0][i] = in[len-1-i]-'0';
		}
		scanf("%s", in);
		len = strlen(in);
		for(int i = 0; i < len; i++){
			range[ti][1][i] = in[len-1-i]-'0';
		}
	}

	for(int b = 1; b < 10; b++)
		gen(0,b);
	for(long long i = 1; i < nh; i++){
		if(i%10 == 0)continue;
		gen(i, -1);
		for(int b = 0; b < 10; b++)
			gen(i,b);
	}

	for(int ti = 0; ti < tc; ti++){
		printf("Case #%d: %d\n", ti+1, ans[ti]);
	}
	return 0;
}