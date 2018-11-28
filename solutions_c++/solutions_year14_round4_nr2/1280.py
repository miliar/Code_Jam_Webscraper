#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <cassert>
#include <fstream>
#include <iomanip>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <string.h>
#include <iostream>
#include <algorithm>
using namespace std;

const int SZ = 1010;
int a[SZ];
int b[SZ];
int c[SZ];

int move(int a[], int from, int to){
	int rez = 0;
	int tmp = a[from];
	if(from>to){
		for(int i=from; i>to; i--){
			a[i] = a[i-1];
			rez++;
		}
		a[to] = tmp;
	}else if(from<to){
		for(int i=from; i<to; i++){
			a[i] = a[i+1];
			rez++;
		}
		a[to] = tmp;
	}
	return rez;
//	cout<<"R: "<<rez<<endl;
//	cout<<"RA: ";
//	for(int i=0; i<n; i++) cout<<a[i]<<' ';
//	cout<<endl;
}

inline int max_el(int a[], int from, int to){
	int maxe = -1;
	int maxv = -1;
	for(int i=from; i<=to; i++){
		if(a[i]>maxe){
			maxe = a[i];
			maxv = i;
		}
	}
	return maxv;
}

int ffind(int a[], int n, int x){
	for(int i=0; i<n; i++)
		if(a[i]==x) return i;
	return -1;
}

int calc(int a[], int b[], int n){
	// from a->b
	int rez = 0;
	for(int i=0; i<n; i++){
		int idx = ffind(a,n,b[i]);
		rez+=move(a,idx,i);
	}
	return rez;
}

bool valid(int a[], int n){
	int i=1;
	while(i<n && a[i]>a[i-1]) i++;
	while(i<n && a[i]<a[i-1]) i++;
	return i>=n;
}

void println(int a[], int n){
	for(int i=0; i<n; i++) cout<<a[i]<<' ';
	cout<<endl;
}

int main(){
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int ntests;
	cin>>ntests;
	for(int testnum=0; testnum<ntests; testnum++){
		int n;
		cin>>n;
		for(int i=0; i<n; i++){ cin>>a[i]; b[i] = a[i]; }
		sort(&b[0],&b[n]);
		int min_rez = 1000000000;
		do{
			if(valid(b,n)){
				for(int i=0; i<n; i++) c[i] = a[i];
				int rez = calc(c,b,n);
				min_rez = min(min_rez,rez);
//				println(b,n);
//				cout<<"R: "<<rez<<endl;
			}
		}while(next_permutation(&b[0],&b[n]));
		cout<<"Case #"<<testnum+1<<": "<<min_rez<<endl;
	}
	return 0;
}
