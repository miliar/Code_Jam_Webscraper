#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
#include <cmath>
#include <map>


using namespace std;



int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T;
	cin>>T;
	for (int t = 0; t<T; t++){
		string mas[102];
		char maslet[102][102] = {0};
		int mascount[102][102] = {0};
		int masaver[102] = {0};
		int n;
		cin>>n;
		int count = 0;
	
		for (int i = 0; i < n; i++) {
			cin>>mas[i];
			int count1 = 0;
			maslet[i][0] = mas[i][0];
			mascount[i][0] = 1;
			for (int j = 1; j < mas[i].length(); j++){
				if (mas[i][j] == mas[i][j-1]){
					mascount[i][count1]++;
				} else {
					count1++;
					maslet[i][count1] = mas[i][j];
					mascount[i][count1] = 1;
				}
			}
			if (i!=0) {
				if (count!=count1) {
					cout<<"Case #"<<t+1<<": Fegla Won"<<endl;
					goto label;
				}
				else {
					for (int j = 0; j <= count; j++) {
						if (maslet[i][j]!= maslet[i-1][j]){
							cout<<"Case #"<<t+1<<": Fegla Won"<<endl;
							goto label;
						}
						masaver[j]+=mascount[i][j];
					}
				}
			} else {
				for (int j = 0; j <= count1; j++) {
					masaver[j] = mascount[i][j];
				}
			}
			count = count1;
		}
		int answer = 0;
		for (int i = 0; i <= count; i++) {
			double aver = double(masaver[i])/n;
			int resav = floor(aver);
			if (aver - floor(aver) > 0.5) resav ++;
			for (int j = 0; j < n; j++){
				answer += abs(resav - mascount[j][i]);
			}
		}
		cout<<"Case #"<<t+1<<": "<<answer<<endl;
		label:;
	}
	return 0;
}