#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int T;
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	cin>>T;
	for(int x = 1; x <= T; x++){
		int N;
		cin>>N;
		string S;
		cin>>S;

		int count = 0, people = 0;

		for(int i = 0; i <= N; i++){
			int num = S[i] - '0';
		//	cout<<people<<" "<<i<<endl;
			if(people < i && num != 0) {
				count += (i-people);
				people += (i-people+num);
			} else people += num;
		}

		cout<<"Case #"<<x<<": "<<count<<endl;
	}
	return 0;
}
