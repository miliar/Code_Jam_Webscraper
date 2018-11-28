#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>
#include <limits.h>
#include <iostream>

using namespace std;

#define rep(i,a,b) for(int i=(a);i<(b);i++)
#define vi vector<int>
#define pb push_back
#define ll long long int
#define gi(x) scanf("%d",&x)
#define ii pair<int,int>
#define CLEAR(x,val) memset(x,val,sizeof(x))
#define SZ(v) (v).size()
#define MOD 1000000007
#define MAXN 1000009

int makePos(string s, int l);
int makeNeg(string s, int l);


void flip(string &str, int i, int j){
	int start = i,last =j;
	while(start<last){
		char ch = str[start];
		str[start] = str[last];
		str[last] = ch;
		start++;
		last--;
	}

	while(i<=j){
		if(str[i]=='+')
			str[i] = '-';
		else
			str[i] = '+';

		i++;
	}
}

int makeNeg(string str, int l){
	if(l<0)	return 0;
	int ret = 0;
	if(str[l] == '+'){
		if(str[0] == '-'){
			ret++;
			str[0] = '+';
		}

		flip(str,0,l);
		ret++;
	}

	return ret + min(makePos(str,l-1)+1, makeNeg(str,l-1));
}

int makePos(string str, int l){
	if(l<0)	return 0;
	int ret = 0;
	if(str[l] == '-'){
		if(str[0] == '+'){
			ret++;
			str[0] = '-';
		}

		flip(str,0,l);
		ret++;
	}

	return ret + min(makePos(str,l-1), makeNeg(str,l-1)+1);
}

int findNum(string s){
	int len = s.length()-1;
	
	return min(makePos(s,len), makeNeg(s,len)+1);
}

int main() {
	int t;	cin>>t;
	rep(test,1,t+1){
		string s;	cin>>s;
		int ans = findNum(s);
		cout<<"Case #"<<test<<": "<<ans<<"\n";
	}
}