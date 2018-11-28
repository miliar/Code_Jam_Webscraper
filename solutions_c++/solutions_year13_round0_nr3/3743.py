//Bismillahir Rahmanir Rahim
//#pragma warning(disable:4786)
//#pragma comment(linker,"/STACK:514850816")
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <climits>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <algorithm>
using namespace std;
#define LL long long
#define eps 1e-15

LL A2L(char* p){
	LL result = 0;
    unsigned digit;
    while ((digit = *p++ - '0') < 10)
    {
        result = result * 10 + digit;
    }    
    return result;
}

void L2A(LL n, char *p){
	int k = (int)ceil(log((double)(n+1))/log(10.0));
	p[k--] = 0;
	while(n){
		p[k--] = (n%10) + '0';
		n/=10;
	}
}

bool ispalin(char *p){
	int i,j;
	for(i=0;p[i];i++);
	for(j=i-1,i=0;i<j;i++,j--)if(p[i]!=p[j])return false;
	return true;
}

inline bool grt(char *a, char *b){
	return (A2L(a)<A2L(b));
}

inline bool grte(char *a, char *b){
	return (A2L(a)<=A2L(b));
}

inline bool eq(char *a, char *b){
	return (A2L(a)==A2L(b));
}

void nextpalin(char *a, char *p){
	int i, j, sz, mid;
	for(i=0;a[i];i++);
	sz = i;
	if(sz&1){
		mid = sz>>1;
		i = mid - 1;j = mid + 1;
		if(a[i] > a[j]){
			while(i>=0){
				p[i] = a[i];
				p[j++] = p[i--];
			}
		}
		else if(a[mid]=='9'){
			p[mid] = '0';
			while(a[i]=='9' && i>=0){
				p[i--] = p[j++] = '0';
			}
			if(i<0){
				p[j+1] = 0;
				j--;
				while(j>=0){p[j+1] = p[j];j--;}
				p[0] = '1';
			}
			else{
				p[i] = a[i]+1;p[j++] = p[i--];
				while(i>=0){
					p[i] = a[i];
					p[j++] = p[i--];
				}
				p[j] = 0;
			}
		}
		else{
			p[mid] = a[mid] + 1;
			while(i>=0){
				p[i] = a[i];
				p[j++] = p[i--];
			}
		}
	}
	else{
		j = sz>>1;
		i = j-1;
		if(a[i]>a[j]){
			while(i>=0){
				p[i] = a[i];
				p[j++] = p[i--];
			}
		}
		else{
			if(a[i]==a[j] && a[i]=='9'){
				while(a[i]=='9' && i>=0){
					p[i] = p[j] = '0';
					i--;j++;
				}
				if(i<0){
					p[j+1] = 0;
					j--;
					while(j>=0){p[j+1] = p[j];j--;}
					p[0] = '1';
				}
				else{
					p[i] = a[i]+1;p[j++] = p[i--];
					while(i>=0){
						p[i] = a[i];
						p[j++] = p[i--];
					}
					p[j] = 0;
				}
			}
			else{
				p[i] = a[i] + 1;
				p[j++] = a[i--];
				while(i>=0){
					p[i] = a[i];
					p[j++] = a[i--];
				}
			}
		}
	}
}

inline double Labs(double a){
	if(a < 0.0) a *= -1.0;
	return a;
}

LL calc(LL A, LL B){
	char p1[20], p2[20], tp[20];
	L2A(A, p1);
	L2A(B, p2);
	LL cnt = 0;
	while(grte(p1,p2)){
		if(ispalin(p1)){
			double t = sqrt((double)A2L(p1));
			if(floor(t) == t){
				LL T = (LL)floor(t);
				L2A(T, tp);
				if(ispalin(tp))cnt++;
			}
		}
		copy(&p1[0], &p1[19], tp);
		nextpalin(tp, p1);
	}
	return cnt;
}

int main(){
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\C-small-attempt0.in","r",stdin);
	freopen("G:\\Coding\ 4\ Contest\\contests\\codejam13\\C-small-attempt0.out","w",stdout);
	int t, cas;
	LL a, b;
	scanf("%d",&t);
	for(cas=1;cas<=t;cas++){
		scanf("%lld %lld",&a,&b);
		printf("Case #%d: %lld\n",cas,calc(a,b));
	}
	return 0;
}