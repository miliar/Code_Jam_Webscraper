#include <iostream>
#include <cstdio>
using namespace std;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("answer.out", "w", stdout);
	
	int t;
	cin>>t;
	int z = 1;
	while(t--) {
		int row;
		
		int cnt[17] = {0};
		for(int k = 0 ; k < 2 ; k++) {
			cin>>row;
			for(int i = 1 ; i <= 4 ; i++) {
				for(int j = 0 ; j < 4 ; j++) {
					int tmp;
					cin>>tmp;

					if( row == i ) cnt[tmp]++;
				}
			}
		}
		
		int cnt_two = 0;
		int ans = 0;
		for(int i = 1 ; i <= 16 ; i++) {
			if( cnt[i] == 2 ) {
				cnt_two++;
				ans = i;
			}
		}

		cout<<"Case #"<<z++<<": ";
		if( cnt_two == 0 ) {
			cout<<"Volunteer cheated!"<<endl;
		}
		else if( cnt_two == 1 ) {
			cout<<ans<<endl;
		}
		else {
			cout<<"Bad magician!"<<endl;
		}
	}
}