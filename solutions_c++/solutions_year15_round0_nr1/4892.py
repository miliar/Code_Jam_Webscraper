#include<bits/stdc++.h>
using namespace std;
int main(){
	ios_base::sync_with_stdio(0);
	ifstream fin;
	fin.open("large.in");
	ofstream fout;
	fout.open("outputlarge.o");
	int tc; fin >> tc;
	for(int j = 1; j <= tc; j++){
		int num; fin >> num;
		int arr[num + 1];
		for(int i = 0; i <= num; i++){
			char temp; fin >> temp;
			arr[i] = temp - '0';
		}
		int total = 0;
		int friendsRequired = 0;
		for(int i = 0; i <= num; i++){
			if(i == 0){
				total += arr[i];
				continue;
			}
			if(total < i){
				friendsRequired += i - total;
				total = i;
				
			}
			total += arr[i];
			cout << arr[i] << endl;
		}
		fout << "Case #" << j << ": " << friendsRequired << "\n";

	}
	fin.close();
	fout.close();
}
/*
1
4 00001
5 10101
*/
