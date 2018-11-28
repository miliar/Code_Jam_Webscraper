#include <iostream>
#include <string>
#include <string.h>
#include <math.h>
#include <time.h>
#include <stdio.h>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <vector>
#include <map>
#include <list>
#include <Windows.h>

#define FORST(X,S,T) for(int X=S; X<=T; X++)  
#define RFORST(X,S,T) for(int X=S; X>=T; X--)  
#define FOR(X,XB) for(int X=0; X<XB; X++)
#define RFOR(X,XB) for(int X=(XB)-1; X>=0; X--)
#define FORSTL(X,C) for(X=C.begin();X!=C.end();X++)
#define SQR(X) ((X)*(X))
#define MID(X,Y) (((X)+(Y))/2)
#define FILL(X,V) memset(X,V,sizeof(X))
#define FILE_R(X) freopen(X, "r", stdin)  
#define FILE_W(X) freopen(X, "w", stdout)  
#define ERREQ(X,Y) (fabs((X)-(Y))<EPS)
#define DBGL cout << "here" << endl;
#define SZ(X) sizeof(X)
const double PI = acos(-1.0);
const double EPS = 1E-9;
const int INF = (int)1E9;
using namespace std;


class bigint{
public:
	int cn[26];
	char c[110];
	static const int szn = 26;
	static const int step = 4;
	static const int divd = (int)1E4;
	bigint(){ 
		FILL(c, 0);
		FILL(cn, 0);
	}
	bigint(char *_c, bool rev){
		FILL(c, 0);
		FILL(cn, 0);
		int l = strlen(_c);
		if(rev){
			for(int i=l-1;i>=0;i--){
				c[i] = _c[l-1-i];
			}
		}else{
			for(int i=0;i<l;i++){
				c[i] = _c[i];
			}
		}
		c[l] = 0;
		int i=0;
		while(step*i<l){
			int x = str2int(c+i*step);
			cn[i++] = x;
		}
	}
	bigint(int num){
		FILL(c, 0);
		FILL(cn, 0);
		for(int i=0;;i++){
			c[i] = '0'+num%10;
			num/=10;
			if(num==0){
				c[i+1] = 0;
				break;
			}
		}
		
		int l = strlen(c);
		int i=0;
		while(step*i<l){
			int x = str2int(c+i*step);
			cn[i++] = x;
		}
	}
	bigint operator +(int num2){
		*this += bigint(num2);
	}
	int *internalAddInt(int *p1, int *p2){
		int carry = 0;
		int tmp[szn];
		FILL(tmp, 0);
		for(int i=0;i<szn;i++){
			int s = carry + p1[i]+p2[i];
			tmp[i] = s%divd;
			carry = s/divd;
		}
		return tmp;
	}
	int *internalMulInt(int *p1, int *p2){
		int carry;
		int tmp[szn];
		FILL(tmp, 0);
		FOR(i, szn){
			carry = 0;
			FOR(j, szn){
				if(i+j>=szn) break;
				int s = carry+p1[i]*p2[j];
				tmp[i+j] += s;
				carry = tmp[i+j]/divd;
				tmp[i+j] %= divd;
			}
		}
		return tmp;
	}
	/*
	char *internalAdd(char *p1, char *p2){
		int i=0, j=0, k=0, carry = 0;
		int num1, num2;
		int l1 = strlen(p1), l2 = strlen(p2);

		char tmp[110];
		while(1){
			if(i>=l1&&j>=l2){
				if(carry){
					tmp[k] = '1';
					tmp[k+1] = 0;
				}else tmp[k] = 0;
				break;
			}
			if(i>=l1) num1 = 0;
			else num1 = str2int(p1+i);
			if(j>=l2) num2 = 0;
			else num2 = str2int(p2+j);
			int s = num1+num2+carry;
			carry = s/divd;
			int2str(s, tmp+k);
			i+=step;
			j+=step;
			k+=step;
		}
		cleanhead(tmp);
		return tmp;
	}
	char *internalMul(char *p1, char *p2){
		int i=0, j=0, k=0, carry = 0;
		int num1, num2;
		int l1 = strlen(p1), l2 = strlen(p2);
		char tmp[110];
		bigint nx = 0;
		while(1){
			if(i>=l1){
				break;
			}
			j = 0;
			while(1){
				FILL(tmp, 0);
				num1 = str2int(p1+i);
				if(j>=l2){
					if(carry){
						int2str(carry, tmp+i+j);
						FOR(ii, i+j) tmp[ii] = '0';
						bigint t(tmp, 0);
						nx += t;
						carry=0;
					}
					break;
				}
				else num2 = str2int(p2+j);
				int s = num1*num2+carry;
				carry = s/divd;
				int2str(s, tmp+i+j);
				FOR(ii, i+j) tmp[ii] = '0';
				cleanhead(tmp);
				bigint tx(tmp, 0);
				nx += tx;
				j += step;
			}
			i+=step;
		}
		return nx.c;
	}
	
	
	bigint operator *(bigint &num){
		int *tmp = internalMulInt(cn, num.cn);
		char tmpc[110];
		intBack2Str(tmp, tmpc);
		return bigint(tmpc, 0);
	}

	bigint operator +(bigint &num){
		int *tmp = internalAddInt(cn, num.cn);
		char tmpc[110];
		intBack2Str(tmp, tmpc);
		return bigint(tmpc, 0);
	}
	*/
	void operator +=(bigint num){
		int *tmp = internalAddInt(cn, num.cn);
		FOR(i, szn) cn[i] = tmp[i];
	}
	void operator *=(bigint num){
		int *tmp = internalMulInt(cn, num.cn);
		FOR(i, szn) cn[i] = tmp[i];
	}
	
	void intBack2Str(int *tmp, char *tmpc){
		FOR(i, szn){
			int x = tmp[i];
			int2str(x, tmpc+i*step);
		}
		cleanhead(tmpc);
	}
	
	int str2int(char *p){
		int ans = 0;
		int base = 1;
		for(int i=0;i<step && p[i]!=0;i++){
			ans += base*(p[i]-'0');
			base *= 10;
		}
		return ans;
	}
	
	void int2str(int num, char *p){
		for(int i=0;i<step;i++){
			p[i] = '0'+(num%10);
			num /= 10;
		}
	}
	void cleanhead(char *p){
		int l = strlen(p);
		for(int i=l-1;i>=1;i--){
			if(p[i]=='0') p[i] = 0;
			else break;
		}
	}
	void print(){
		char tmp[110];
		intBack2Str(cn, c);
		
		int l = strlen(c);
		for(int i=l-1;i>=0;i--){
			tmp[i] = c[l-1-i];
		}
		tmp[l] = 0;
		printf("%s", tmp);
	}

	bool operator < (const bigint &num) const {
		int l1 = strlen(c);
		int l2 = strlen(num.c);
		if(l1<l2) return true;
		if(l1>l2) return false;

		for(int i=l1-1; i>=0; i--){
			if(c[i]>num.c[i]) return false;
			else if(c[i]<num.c[i]) return true;
		}
		return false;
	}
	bool operator <= (const bigint &num) const {
		int l1 = strlen(c);
		int l2 = strlen(num.c);
		if(l1<l2) return true;
		if(l1>l2) return false;

		for(int i=l1-1; i>=0; i--){
			if(c[i]>num.c[i]) return false;
			else if(c[i]<num.c[i]) return true;
		}
		return true;
	}
	bool operator == (const bigint &num) const {
		int l1 = strlen(c);
		int l2 = strlen(num.c);
		if(l1!=l2) return false;

		for(int i=l1-1; i>=0; i--){
			if(c[i]!=num.c[i]) return false;
		}
		return true;
	}
};

bool checkp(char p[105]){
	int len = strlen(p);
	FOR(i, len/2){
		if(p[i]!=p[len-1-i]) return false;
	}
	return true;
}

char numnow[105];
set<bigint> pset;

void enumNum(int len, int idx){
	if(idx>len/2){
		numnow[len] = 0;
		bigint num(numnow, 1);
		num *= num;
		num.intBack2Str(num.cn, num.c);
		if(checkp(num.c)){
			if(pset.find(num)==pset.end()){
				pset.insert(num);
				num.print();
				printf("\n");
			}
		}
		return;
	}
	if(idx==0){
		numnow[idx] = '1';
		numnow[len-idx-1] = '1';
		enumNum(len, idx+1);
		numnow[idx] = '2';
		numnow[len-idx-1] = '2';
		enumNum(len, idx+1);
	}else if(idx==len/2){
		numnow[idx] = '0';
		numnow[len-idx-1] = '0';
		enumNum(len, idx+1);
		numnow[idx] = '1';
		numnow[len-idx-1] = '1';
		enumNum(len, idx+1);
		numnow[idx] = '2';
		numnow[len-idx-1] = '2';
		enumNum(len, idx+1);
	}else{
		numnow[idx] = '0';
		numnow[len-idx-1] = '0';
		enumNum(len, idx+1);
		numnow[idx] = '1';
		numnow[len-idx-1] = '1';
		enumNum(len, idx+1);
	}
}

char A[105], B[105];
bigint iA, iB;

int main(){
	
	
	int cs;
	/*
	FILE_R("number1-45");
	while(scanf("%s", A)!=EOF){
		bigint a(A, 1);
		pset.insert(a);
	}
	FILE_R("number45-50");
	while(scanf("%s", A)!=EOF){
		bigint a(A, 1);
		pset.insert(a);
	}
	*/
	FILE_R("number1-50");
	while(scanf("%s", A)!=EOF){
		bigint a(A, 1);
		pset.insert(a);
	}
	FILE_R("input");
	FILE_W("output");
	cin>>cs;
	for(int csn=1;csn<=cs;csn++){
		printf("Case #%d: ", csn);
		scanf("%s%s", A, B);
		iA = bigint(A, 1);
		iB = bigint(B, 1);
		long long ans = 0;
		set<bigint>::iterator r;
		FORSTL(r, pset){
			if(iA<=(*r) && (*r)<=iB){
				ans++;
			}
			if(iB<(*r)) break;
		}
		cout << ans << endl;
	}
	return 0;


	/*
	FILE_W("testintR");
	FORST(i, 99999, 100200){
		FORST(j, 99999, 100200){
			bigint a = i;
			bigint b = j;
			a*=b;
			//a.print();
			printf("%lld\n", (long long)i*j);
		}
	}
	*/
	/*
	FILE_W("number45");

	char tt[5];
	tt[1] = 0;
	tt[0] = '1';
	pset.insert(bigint(tt, 0));
	tt[0] = '4';
	pset.insert(bigint(tt, 0));
	tt[0] = '9';
	pset.insert(bigint(tt, 0));

	FORST(len, 45, 45){
		cerr << len << endl;
		enumNum(len, 0);
	}

	cout << pset.size();
	return 0;

	
	int cs;
	cin>>cs;
	for(int csn=1;csn<=cs;csn++){
		printf("Case #%d: ", csn);
		scanf("%s%s", A, B);
		iA = bigint(A, 1);
		iB = bigint(B, 1);
		long long ans = 0;
		set<bigint>::iterator r;
		FORSTL(r, pset){
			if(iA<=(*r) && (*r)<=iB) ans++;
		}
		cout << ans << endl;

	}
	return 0;
	*/
}