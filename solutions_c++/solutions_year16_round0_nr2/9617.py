#include <stdio.h>
#include <iostream>

using namespace std;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin>>test;

	for(int t=1; t<=test; t++) {
		string str;
		cin>>str;
		int end = str.size()-1,ans = 0;
		while(end>=0 && str[end]=='+')
			end--;

		while(end>=0) {
			char ch = str[end];
			ans++;
			while(end>=0 && str[end]==ch)
				end--; 
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}	
}