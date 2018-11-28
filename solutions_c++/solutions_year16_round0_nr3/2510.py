#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <queue>
#include <math.h>
#define MP make_pair

using namespace std;
typedef long long LL;
typedef unsigned int uint;
typedef pair<int,int> pii;
const double pi = atan (1.0) * 4;

int N, J;
int a[40];

LL get (LL base){
	LL res = 0, add = 1;
	for (int i=N-1;i>=0;i--){
		if (a[i] == 1)	res += add;
		add *= base;
	}
	return res;
}
LL get_fact (LL num){
	for (LL f=2;f*f<=num;f++){
		if (num % f == 0){
			return f;
		}
	}
	return 1;
}
void add_1 (){
	a[N-2]++;
	for (int i=N-2;i>=1;i--){
		if (a[i] == 2){
			a[i] = 0;
			a[i-1]++;
		}
		else
			break;
	}
}

void go (){
	vector<LL> fac;
	for (;;){
		fac.clear ();
		for (int base=2;base<=10;base++){
			LL num = get (base);
			LL ff = get_fact (num);
			if (ff == 1)
				break;
			else
				fac.push_back (ff);
		}
		if (fac.size () == 9){
			for (int i=0;i<N;i++)	printf ("%d", a[i]);
			for (int i=0;i<fac.size ();i++)
				printf (" %lld", fac[i]);
			printf ("\n");
			add_1 ();
			break;
		}
		add_1 ();
	}
}

int main (){
	freopen ("F:\\C++\\C-small-attempt0.in", "r", stdin);
	freopen ("F:\\C++\\C-small-attempt0.out", "w", stdout);
	
	int T; scanf ("%d",&T);
	int cas = 1;
	while (T--){
		printf ("Case #%d:\n",cas++);
		scanf ("%d%d",&N,&J);
		memset (a, 0, sizeof(a));
		a[0] = a[N-1] = 1;
		for (int i=0;i<J;i++){
			go ();
		}
	}
	return 0;
}