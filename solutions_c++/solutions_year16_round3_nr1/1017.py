#include<iostream>
#include<vector>
using namespace std;

int count(vector<int> &a){
	int c = 0;
	for(int i = 0; i < a.size(); i++){
		if(a[i] != 0)c++;
	}
	return c;
}

void display(vector<int> &a){
	if(count(a) == 2){
		int p, q;
		for(int i = 0; i < a.size(); i++){
			if(a[i] != 0){
				p = i;
				break;
			}
		}
		for(int i = p + 1; i < a.size(); i++){
			if(a[i] != 0)q = i;
		}
		//cout << p << " " << q << endl;
		if(a[p] > a[q]){
			for(int i = 0; i < a[p] - a[q]; i++)cout << (char)('A' + p) << " ";
			for(int i = 0; i < a[q]; i++)cout << (char)('A' + p) << (char)('A' + q) << " ";
			return;
		}
		else{
			for(int i = 0; i < a[q] - a[p]; i++)cout << (char)('A' + q) << " ";
			for(int i = 0; i < a[p]; i++)cout << (char)('A' + q) << (char)('A' + p) << " ";
			return;
		}
	}
	else{
		int p;
		int max = 0;
		for(int i = 0; i < a.size(); i++){
			if(a[i] > max){
				max = a[i];
				p = i;
			}
		}
		cout << (char)('A' + p) << " ";
		a[p]--;
		display(a);
		return;
	}
}


int main(){
	
	int t;
	cin >> t;
	
	
	for(int iter = 0; iter < t; iter++){
		int n;
		cin >> n;
		vector<int> a(n);
		for(int i = 0; i < n; i++)cin >> a[i];
		
		cout << "Case #" << iter + 1 << ": ";
		display(a);
		cout << endl;
	}

	
	return 0;
}
