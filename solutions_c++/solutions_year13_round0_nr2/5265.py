
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <bitset>
#include <string>
#include <algorithm>
#include <utility>
#include <functional>
#include <iterator>
#include <complex>
#include <valarray>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cassert>
#include <cstring>

using namespace std;

#define f(i,n) for(int i=0; i <n;i++)
#define fi(i,s,n) for(int i=s; i<n;i++)

typedef long long ll;

int num[100][100];
int rm[100], cm[100];


int main(){
	int tc;
	scanf("%d",&tc);
	f(i,tc){
		printf("Case #%d: ",i+1);
		int h,w;
		scanf("%d %d",&h,&w);
		f(j,h)f(k,w){int a;scanf("%d",&a);num[j][k]=a;}
		
		bool ur[100],uc[100];

		f(j,h){
			ur[j]=true;
			rm[j] =0;
			f(k,w)rm[j]=max(rm[j],num[j][k]);
		}
		f(j,w){
			uc[j]=true;
			cm[j] =0;
			f(k,h)cm[j]=max(cm[j],num[k][j]);
		}

		bool found = true;
		f(j,h)
			f(k,w)
				if(num[j][k]<rm[j] && num[j][k]<cm[k]){found = false;}

		printf("%s",found?"YES\n":"NO\n");
	}
}
