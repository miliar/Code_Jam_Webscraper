#include<iostream>
#include<algorithm>
using namespace std;


void f(int a){
	string s;
	int n;
	cin >> n;
	cin >> s;
	int l=0,p=0;
	for(int i=0;i<=n;i++){
		if(l<i){
			p+=i-l;
			l+=i-l;
		}
		l+=s[i]-'0';
	}
	cout << "Case #" << a << ": " << p << endl;
}

main(){
	ios_base::sync_with_stdio(0);
	int a;
	cin >> a;
	for(int i=1;i<=a;i++)f(i);
}
