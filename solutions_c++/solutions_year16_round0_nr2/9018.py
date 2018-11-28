#include <bits/stdc++.h>

using namespace std;


int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T, i, t;
	cin>>T;
	for(t=1; t<=T; t++) {
		char str[102];
		cin>>str;
		int count=0, n = strlen(str), i =0, j;
		if(str[i]=='-' && !i) {
			while(str[i++]=='-') {}
			count++;
		}
		while(i<n) {
			
			if(str[i]=='-') {
				while(str[i++]=='-') {}
				count+=2;
			} else {
				i++;
			}			
		
		}

		cout<<"Case #"<<t<<": "<<count<<endl;

	}

}

/*



#include <bits/stdc++.h>

using namespace std;

bool allplus(char str[]) {
	int n = strlen(str);
	for(int i=0; i<n; i++) {
		if(str[i] == '-') {
			return false;
		}
	}
	return true;
}

int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int T, i, t;
	cin>>T;
	for(t=1; t<=T; t++) {
		char str[102];
		cin>>str;
		int count=0, n = strlen(str), i =0, j;
		while(i<n) {
			if(i<n && allplus(str)) {
				break;
			} else if(str[i]=='-' && !i) {
				j=i;
				while(str[j]=='-' && str[j]) {
					str[j]='+';
					j++;
				}
				count++;
				i=j;
			} else {
				while(str[i++]!='-' && str[i]) {}
				j=i;
				while(str[j]=='-' && str[j]) {
					str[j++]='+';
				}
				count+=2;
			}

		}

		cout<<"Case #"<<t<<": "<<count<<endl;

	}

}

*/