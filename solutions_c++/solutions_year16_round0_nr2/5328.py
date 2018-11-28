#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;
	cin >> n;
	string s;
	for (int i=0;i<n;i++){
		cin >> s;
		int j=0;
		int ans=0;
		if (s[0]=='-'){
			ans++;
			while(s[j]=='-')
				j++;
		}
		while(j<s.size()){
			if (s[j]=='-'){
				ans+=2;
				while(s[j]=='-')
					j++;
			}
			j++;	 
		}
		cout << "Case #" << i+1 << ": "<< ans << endl;;
	}
}