#include<fstream>
#include<iostream>
#include<vector>

using namespace std;

int T, N;
vector<int> check(10);

int main() {
	ifstream fin("input.txt");
	if(!fin.is_open()) {
		cout<<"Error"<<endl;
	}
	ofstream fout("output.txt");
	if(!fout.is_open()) {
		cout<<"Error"<<endl;
	}
	fin>>N;
	int k = 1;
	for(int i =0; i < N; i++) {
		fin>>T;
		if(T == 0) {
			fout<<"Case #"<<k++<<": INSOMNIA"<<endl;
			continue;
		}
		int j = 1, temp, res = 10, counter;
		for(int t = 0; t < 10; t++)
			check[t] = 0;
		while(res != 0) {
			temp = j*T;
			counter = temp;
			j++;
			while(temp != 0) {
				if(check[temp % 10] == 0){
					res --;
					check[temp % 10]++;
				}
				temp /= 10;
			}
			
		}
		fout<<"Case #"<<k++<<": "<<counter<<endl;
	}
	
}