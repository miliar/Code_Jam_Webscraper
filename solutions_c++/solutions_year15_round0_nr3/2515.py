#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <climits>
#include <numeric>
#include <stdlib.h> 
#include <time.h> 
#include <math.h>
#include <string>
using namespace std;
int mult1[5][5]={{},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};
int mult(int a, int b){
	return a / abs(a) * b / abs(b) * mult1[abs(a)][abs(b)];
}
string str1;
int main(){
	//freopen("C-small-attempt0.in", "r", stdin);
	//freopen("C-small-attempt0.out", "w", stdout);
	long l, T, i, j, f1, f2, f, m;
	long long x, cir;
	char ch;
	int t, a[20000];
	cin>>T;
	for(int I=1; I<=T; I++){
		cin>>l>>x;
		t = 1;
		for(i=0; i<l; i++)	{
			cin>>ch;
			a[i] = ch - 'i' +2;
			t = mult(t, a[i]);
		}
		cout<<"Case #"<<I<<": ";
		if (t == 1|| (t != -1 && x % 4 != 2 )|| (t == -1 && x % 2 != 1 ) )
		{
			cout<<"NO"<<endl;
			continue;
		}
		cir = 0;
		if (t == 1) cir = 1;
		else if (t == -1) cir = 2;
		else cir = 4;
		if (cir > x) cir = x;
		cir =cir*l;
		f1 = 0;
 		m = 1;
		for(i=0; i<cir; i++)
		{
			m = mult(m, a[i%l]);
			if (m == 2) {f1 = i + 1; break;}			
		}
 		f2 = 0;
		m = 1;
		for(i=cir-1; i>=0; i--)
		{
			m = mult(a[i%l], m);
			if (m == 4) {f2 = l * x - cir + i + 1; break;}			
		}
		f = 1;
		if (f1+1 >= f2) f = 0;
		if (f1 == 0 || f2 == 0) f = 0;
		if (f) {cout<<"YES"<<endl;} else {cout<<"NO"<<endl;}
	}
		//fclose(stdin);
		//fclose(stdout);
			return 0;
}