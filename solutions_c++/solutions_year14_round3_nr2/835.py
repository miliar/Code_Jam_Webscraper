#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
long long p, q, t, n;
int tt[40][40];
string x[101];
bool used[210];
int stack[200];
long long ret;
bool valid(){
	string s="";
	bool letters[40];memset(letters, false, sizeof(letters));
	for (int i = 0; i < n; ++i)
		s+=x[stack[i]];
	//cout << s << endl;
	for (int  i = 0; i < s.size(); ++i) {
//		cout << s[i];
		if (i==0 || s[i]!=s[i-1]) {
			if (letters[s[i]-'a']) return false;
			letters[s[i]-'a']=true;
		};
	};
	//cout << "true" << endl;
	return true;
};

void rek(int nr, int count){
  stack[count-1]=nr;
  used[nr]=true;
  if (count == n && valid())
	  ++ret;
  else {
	  for (int i = 0; i < n; ++i)
		  if (!used[i]) rek(i, count+1);
  };
  used[nr]=false;
};

int main(){
  cin >> t;
  for (int i = 1; i <= t; i++) {
	  long long k = 0;
	  memset(tt, 0, sizeof(tt));
	  cin >> n;
	  string s;
	  for (int j = 0; j < n; ++j) {
		  cin >> s;x[j]=s;
	  };
	  ret=0;
	  for (int j = 0; j < n; ++j) {
	        memset(used, false, sizeof(used));
	  	rek(j,1);
 	   };
      cout << "Case #" << i << ": " << ret%1000000007 << endl;
  };
};
