#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <climits>
 
#define MAXSIZE 10000000
#define oo 1000000000
#define WHITE 0
#define GREY 1
#define BLACK 2
#define X first
#define Y second
 
#ifndef MAX
#define MAX(a,b) (a>b)?a:b
#endif
 
#ifndef MIN
#define MIN(a,b) (a>b)?b:a;
#endif
 
using namespace std;
 
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<float> vf;

void getCnt(int a,int &c){
	while(a>0){
		int t = a%10;
		a = a/10;
		c = c|(1<<t);
	}
}

int main() {
	// your code goes here
	int t;
	cin>>t;
	int j = t;
	while(t--){
		int a;
		cin>>a;
		if(a==0){
			cout<<"Case #"<<(j-t)<<": INSOMNIA\n";
			continue;
		}
		int cnt = 0;
		int i = 1;
		int b;
		while(cnt!=1023){
			b = a*i;
			getCnt(b,cnt);
			i++;
		}
		cout<<"Case #"<<(j-t)<<": "<<b<<"\n";
	}
	return 0;
}
