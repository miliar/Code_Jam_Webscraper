#include<iostream>
#include<fstream>
using namespace std;
int a[100000];
int b[100000];

void exchange(int x){
	int tmp = a[x];
	a[x] = a[x+1];
	a[x+1] = tmp;
}
int main(){
	ifstream fin("2.in");
	ofstream fout("2.out");
	int n, x;
	int testSum;
	fin >> testSum;
	for (int test = 1; test <= testSum; test++){
		fout << "Case #" << test << ":" << ' ';
		fin >> n;
		int now = 1;
		bool flag = false;
		for (int i = 1; i <= n; i++) {
			fin >> x;
			while ((now != 1) && (a[now - 1] < x)){
				if (a[now - 1] < x){
					if (! flag){
						flag = true;
						break;
					}
				}
				else {
					break;
				}
				exchange(now - 1);
				now--;
			}
			a[now] = x;
			now = i+1;
			for (int j = 1; j <= i; j++)
				cout << a[j] << ' ';
			cout << endl;
		}
	}
}

