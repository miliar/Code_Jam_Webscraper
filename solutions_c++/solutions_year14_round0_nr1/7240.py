#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

int a[4][4];

int main(){
	freopen("A-small.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	int test;
	cin>>test;
	getchar();

	for (int t=1;t<=test;++t){
		int row1, row2;
		int pocket[16];
		int x;
		for (int i=0;i<16;++i){
			pocket[i] = 0;
		}

		cin>>row1;
		for (int i = 0;i<4; ++i){
			for (int j=0;j<4;++j){
				cin>>x;
				if (i == row1-1) pocket[x-1]++;
			}
		}
		cin>>row2;
		for (int i = 0;i<4; ++i){
			for (int j=0;j<4;++j){
				cin>>x;
				if (i == row2-1) pocket[x-1]++;
			}
		}

		int num = 0;
		int ansX = 0;
		for (int i = 0;i<16; ++i){
			if (pocket[i] == 2){
				num++;
				ansX = i+1;
			}
		}

		if (num == 1) cout<<"Case #"<<t<<": "<<ansX<<'\n';
		else if (num>1) cout<<"Case #"<<t<<": "<<"Bad magician!"<<'\n';
		else cout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<'\n';

		//cout<<"Case #"<<t<<": "<<ans<<'\n';
	}

	return 0;
}
