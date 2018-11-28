#include<iostream>

using namespace std;

int met_one[5][5];
int met_two[5][5];

int main() {
	int T;
	int i,j,k;
	cin>>T;
	int first,second;
	for(k=1; k<=T; k++) {
		cin>>first;
		for(i=1; i<=4; i++) {
			for(j=1; j<=4; j++) {
				cin>>met_one[i][j];
			}
		}

		cin>>second;
		for(i=1; i<=4; i++) {
			for(j=1; j<=4; j++) {
				cin>>met_two[i][j];
			}
		}

		int num = 0;
		int res;
		for(i=1; i<=4; i++) {
			for(j=1; j<=4; j++) {
				if(met_one[first][i] == met_two[second][j]) {
					num ++;
					res = met_one[first][i];
					break;
				}
			}
		}
		freopen("out.txt","a",stdout);
		cout<<"Case #"<<k<<": ";
		if(num == 1) {
			cout<<res<<endl;
		} else if(num >1) {
			cout<<"Bad magician!"<<endl;
		} else {
			cout<<"Volunteer cheated!"<<endl;
		}

	}
    return 0;
}