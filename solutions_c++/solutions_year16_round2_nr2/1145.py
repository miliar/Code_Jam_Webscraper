#include<iostream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

string s1, s2;
vector <int> v1, v2;
int T, n, r, m, n1, n2;  

bool ok(int x, int y) {
  int z = 1;
  if(n==3) z = 100; 
  if(n==2) z = 10;
  for(int i=0; i<n; i++) {
  	if((s1[i]!='?' && (x/z)%10 != s1[i]-'0')||(s2[i]!='?' && (y/z)%10 != s2[i]-'0')) return false;
  	z/=10;
  }
  return true;
}

int main(){
	cin>>T;
	for(int t=1; t<=T; t++) {
		cin>>s1>>s2;
		n = s1.size();
		m = 9999999;
		if(n==1) r = 10; else
		if(n==2) r = 100; else r = 1000;
		for(int i=0; i<r; i++)
			for(int j=0; j<r; j++) 
				if(ok(i,j))
					if(abs(i-j)<m) m = abs(i-j), n1 = i, n2 = j;
		cout<<"Case #"<<t<<": ";
		if(n==3 && n1<100) cout<<0;
		if(n>1 && n1<10) cout<<0;
		cout<<n1;
		cout<<" ";
		if(n==3 && n2<100) cout<<0;
		if(n>1 && n2<10) cout<<0;
		cout<<n2;
		cout<<endl;
		v1.clear();
		v2.clear();
	}
}