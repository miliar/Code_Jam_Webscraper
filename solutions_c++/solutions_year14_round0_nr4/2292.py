#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <map>
#include <iomanip>
#define pb push_back
#define mp make_pair
#define ll long long
using namespace std;
//--------------------
double a,b,c,d,f,x,ans;
ll t,i,j,t1,n;
vector <double> mas1, mas2;
//--------------------
int main(){
	freopen("D-large.in", "r", stdin);
	freopen("D.out", "w", stdout);

	scanf ("%d", &t);
	for(t1 = 1; t1 <= t; ++t1){

		printf ("Case #%d: ", t1);
		scanf ("%d", &n);

		mas1.resize(n);
		mas2.resize(n);
		for (i = 0; i < n; ++i) scanf("%lf", &mas1[i]);
		for (i = 0; i < n; ++i) scanf("%lf", &mas2[i]);
		sort(mas1.begin(), mas1.end());
		sort(mas2.begin(), mas2.end());

		j = 0;

		for(i = 0; i < n; ++i){
			if(mas1[i] > mas2[j]) j++;
		}

		printf("%d ",j);

		j = 0;
		for(i = 0; i < n; ++i){
			if(mas2[i] > mas1[j]) j++;
		}
		printf("%d\n", n - j);
	}

	return 0;
}