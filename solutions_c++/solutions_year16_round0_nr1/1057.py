#include<iostream>
using namespace std;

bool a[10];
int N = 2000;

int find(int n){
	for(int i = 0; i < 10; i++)a[i] = false;
	int count = 0, t = 0;
	for(int i = 1; i < N; i++){
		t += n;
		int tt = t;
		while(t > 0){
			int b = t % 10;
			if(a[b] == false){
				count++;
				a[b] = true;
			}
			t /= 10;
		}
		if(count == 10){
			return tt;
		}
		t = tt;
	}
	return -1;
}

int main(){
	int m, n;
	cin >> m;
	for(int i = 0; i < m; i++){
		cin >> n;
		if(n == 0)cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		else
		 cout << "Case #" << i+1 << ": " << find(n) << endl;
	}
	//system("pause");
	return 0;
}
