#include <bits/stdc++.h>
using namespace std;


int main() {
	int t,l;
	cin >> t;
	l=t;
	while(t--){
	string s;
	cin >> s;
	int k = s.size()-1;
	int count=0;
	while(s[k]=='+')
	k--;
	while(k>=0){
		if(s[0]=='+'){
			int i=0;
			while(s[i]=='+'){
				s[i]='-';
				i++;
			}
			while(s[k]=='+')
			k--;
			
		}
		else{
			int i=0;
			for(i=0;i<=k/2;i++)
			{
				char t = s[i];
				s[i] = s[k-i];
				if(s[i]=='+')
				s[i]='-';
				else
				s[i]='+';
				s[k-i] = t;
				if(s[k-i]=='+')
				s[k-i]='-';
				else
				s[k-i]='+';
			}
			
			
			while(s[k]=='+')
			k--;
		}
		count++;
	}
	cout << "case #" << l-t << ": " << count << endl;
	}
	return 0;
}