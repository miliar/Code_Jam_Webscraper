#include <iostream>
#include <sstream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <string>
#include <cmath>
#define f(a,b,c) for(int a=b;a<=c;a++)
#define F(a,b,c) for(int a=b;a<c;a++)
#define ff(a,b,c) for(int a=b;a>=c;a--)
#define FF(a,b,c) for(int a=b;a>c;a--)
#define pb push_back
#define mp make_pair

using namespace std;

bool isPerfectSquare(long x){
	if(x < 0) return false;

	long tst = (long)(sqrt(x) + 0.5);
	return tst*tst == x;
}

string toString(long x){
	string result;
	
	stringstream convert;
	convert << x;
	result = convert.str();

	return result;
}

bool isPalindrome(string s){
	int st = s.length()/2, en = s.length()-1;

	for(int i=0;i < st;i++, en--){
		if (s[i]!=s[en]) return false;
	}

	return true;
}

int main(){

	int t, count=0;
	string s, tmp;
	long a,b;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("o.txt","w",stdout);

	cin >> t;
	while(t--){

		int cnt=0;
		count++;
		cin >> a >> b;
		f(i,a,b){
			tmp = toString(i);
			if(isPerfectSquare(i)){
				long temp = (long)sqrt(i);
				s = toString(temp);

				if(isPalindrome(s) && isPalindrome(tmp)) cnt++;
			}
		}
		cout << "Case #" << count << ": "<< cnt << endl;
	}
}