#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <set>
#include <algorithm>
#include <map>
#include <stack>
using namespace std;

typedef long long ll;

ll gcd(ll x, ll y){
	if(y%x == 0){
		return x;
	}
	return gcd(y%x, x);
}

bool ispower(ll n){
	while(n != 1){
		if(n%2)return 0;
		n >>= 1;
	}
	return true;
}
int generation(ll x, ll y){
	ll g = gcd(x, y);
	ll newx = x / g;
	ll newy = y / g;
	int count = 1;
	if(!ispower(newy))return -1;
	while(newy > 2*newx){
		count++;
		if(newy%2)return -1;
		newy >>= 1;
	}
	return count;
}

ll atoi(const string &s){
	ll ret = 0;
	for(int i = 0; i < s.length(); ++i){
		ret *= 10;
		ret += s[i]-'0';
	}
	return ret;
}

int main()
{
	ifstream in;
	in.open("A-small-attempt1.in");
	//in.open("in.txt");
	ofstream out;
	out.open("out.txt");
	int test;
	in>>test;
	for(int t = 1; t <= test; ++t){
		string s;
		in>>s;
		int i = 0;
		while(s[i] != '/')++i;
		string sx = s.substr(0, i);
		string sy = s.substr(i+1);
		int ans = generation(atoi(sx), atoi(sy));
		out<<"Case #"<<t<<": ";
		if(ans == -1)out<<"impossible"<<endl;
		else
			out<<ans<<endl;
	}
	return 0;
}