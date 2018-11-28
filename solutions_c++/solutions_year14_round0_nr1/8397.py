#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;



int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int T;
	cin>>T;
	for (int t = 0; t < T; t++){
		int mas1[4][4] = {0};
		int mas2[4][4] = {0};
		int r1,r2;
		cin>>r1;
		r1--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>mas1[i][j];
		cin>>r2;
		r2--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
				cin>>mas2[i][j];
		int count = 0;
		int num = -1;
		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++){
				if (mas1[r1][i] == mas2[r2][j]){
					count++;
					num = mas1[r1][i];
				}
			}
		}
		cout<<"Case #"<<t+1<<": ";
		if (count == 0){
			cout<<"Volunteer cheated!"<<endl;
		} else if (count > 1){
			cout<<"Bad magician!"<<endl;
		} else cout<<num<<endl;
	}
	return 0;
}
