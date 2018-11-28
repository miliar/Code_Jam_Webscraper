#include<iostream>
#include<cstdio>
#include<cmath>
#include<vector>
#include<string>
#include<algorithm>

#define pb push_back
#define ll long long
#define REP(a,b) for(int(a)=0;(a)<(b); (a)++)
using namespace std;

string cel(string s){
	string novy = "";
	bool bylo = false;
	for(int a = s.size()-1; a >= 0; a--){
		if(s[a] == '+' && !bylo){
			continue;
		}
		if(s[a] == '+'){
			novy+='-';
		}
		if(s[a] == '-'){
			novy+='+';
			bylo = true;
		}
	}
	return novy;
}

bool is_ok(string s){
	bool dob = true;
	REP(a,s.size()){
		if(s[a] == '-'){
			dob = false;
			break;
		}
	}
	return dob;
}
void solve(int test){
	string s;
	cin>>s;
	bool dob = is_ok(s);
	if(dob){
		printf("Case #%i: 0\n",test);
		return;
	}
	int i = 0;
	while(s.size()){
		if(s[0] == '+'){
			i++;
			int a = 0;
			while(s[a] == '+'){
				s[a] = '-';
				a++;
			}
		}
		s= cel(s);
		i++;
		if(is_ok(s)){
			break;
		}
	}
	printf("Case #%i: %i\n",test,i);
}

int main(){
	int t;
	scanf("%i",&t);
	REP(a,t) solve(a+1);
	return 0;
}
