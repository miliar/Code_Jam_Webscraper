#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void f(){
	int h;
	cin >> h;
	string a,b;
	cin >> a >> b;
	vector<int> A,B;
	A.push_back(1);
	B.push_back(1);
	for(int i=1;i<a.size();i++)
		if(a[i]==a[i-1]){
			A[A.size()-1]++;
			a.erase(a.begin()+i);
			i--;
		}
		else A.push_back(1);
	for(int i=1;i<b.size();i++)
		if(b[i]==b[i-1]){
			B[B.size()-1]++;
			b.erase(b.begin()+i);
			i--;
		}
		else B.push_back(1);
//	cout << a << endl << b << endl;
	if(a!=b){
		cout << "Fegla Won\n";
		return;
	}
//	for(int i=0;i<A.size();i++)cout << A[i] << " ";
//	cout << endl;
//	for(int i=0;i<B.size();i++)cout << B[i] << " ";
//	cout << endl;
	int l=0;
	for(int i=0;i<A.size();i++)l+=abs(A[i]-B[i]);
	cout << l << endl;
}

int main(){
	ios_base::sync_with_stdio(0);
	int a;
	cin >> a;
	for(int i=1;i<=a;i++){
		cout << "Case #" << i << ": ";
		f();
	}
}
