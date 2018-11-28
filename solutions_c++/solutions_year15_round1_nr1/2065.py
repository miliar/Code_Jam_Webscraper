#include <iostream>

using namespace std;

void solve(int m[], int n){
	int m1 = 0;
	int m2 = 0;
	int m22 = 0;
	
	int temp;
	
	for(int i=1; i<n; i++){
		temp = m[i-1]-m[i];
		if(temp > 0)
			m1 += temp;
		if(temp > m2)
			m2 = temp;
	}	
	
	for(int i=0; i<n-1; i++){
		if(m[i]>m2)
			m22 += m2;
		else
			m22 += m[i];
	}
	cout << m1 << " " << m22 << endl;	
}

int main(){
	int t;
	int * n;
	int ** m;
	
	cin >> t;
	n = new int[t];
	m = new int*[t];
	for(int i=0; i<t; i++){
		cin >> n[i];
		m[i] = new int[n[i]];
		for(int j=0; j<n[i]; j++)
			cin >> m[i][j];
	}
	
	for(int i=0; i<t; i++){
		cout << "Case #" << i+1 << ": ";
		solve(m[i], n[i]);
	}
	return 0;
}