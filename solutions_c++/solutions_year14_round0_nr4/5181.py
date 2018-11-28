#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
#include<deque>
using namespace std;


int main(){
	ifstream cin;
	ofstream cout;
	cin.open("D-large.in");
	cout.open("output.txt");

	int t;
	cin >> t;
	for (int kh = 0; kh < t; kh++){
		int n;
		cin >> n;
		deque<double> girl, boy,girlo,boyo;
		for (int i = 0; i < n; i++){
			double z;
			cin >> z;
			girl.push_back(z);
		}
		for (int i = 0; i < n; i++){
			double z;
			cin >> z;
			boy.push_back(z);
		}
		sort(girl.begin(), girl.end());
		sort(boy.begin(), boy.end());
		girlo = girl;
		boyo = boy;
		int cnt = 0;
		while (!girl.empty()){
			if (girl.back() > boy.back()) {
				cnt++;
				girl.pop_back();
				boy.pop_front();
			}
			else{
				boy.pop_back();
				girl.pop_back();
			}

		}
		
	/*	for (int i = 0; i<n; i++) cout << girlo[i] << " ";
		cout << endl;
		for (int i = 0; i<n; i++) cout << boyo[i] << " ";
		cout << endl;
		cout << cnt << endl;*/
		int cnto = 0;
		while (!girlo.empty()){
			if (girlo.front() > boyo.front()) {
				cnto++;
				girlo.pop_front();
				boyo.pop_front();
			}
			else{
				boyo.pop_back();
				girlo.pop_front();
			}

		}
		cout << "Case #" << kh + 1 << ": " << cnto << " " << cnt << endl;


	}



	return 0;
}