#include<iostream>
#include<vector>
using namespace std;

int check(vector<double> a, vector<double> b, int n1, int n2) {
	if (n1>=a.size() || n2>=b.size()) return 0;
	if (a[n1]>b[n2]) { return (1 + check(a, b, n1+1, n2+1)); }
	else return check(a, b, n1+1, n2);
}
int main() {
	int cases;
	cin>>cases;
	for (int i=0;i<cases;i++) {
		int x=0, y=0;
		vector<double> a, b;
		int num; cin>>num;
		for (int j=0;j<num;j++) {
			double temp;
			cin>>temp;
			a.push_back(temp);
		}
		for (int j=0;j<num;j++) {
			double temp;
			cin>>temp;
			b.push_back(temp);
		}
		sort(a.begin(), a.end()); sort(b.begin(), b.end());
		int count=0;
		for(int j=num-1;j>=0;j--) {
			if(b[j]>a[num-1]) count++;
			else break;
		}
		x = check(a, b, count, 0);
		bool ab[num];
		for (int j=0;j<num;j++) { ab[j]=true;}
		for (int j=0;j<num;j++) {
			for (int k=0;k<num;k++) {
				if(b[k]>a[j] && ab[k]) { y++; ab[k]=false; break; }
			}
		}
		cout<<"Case #"<<i+1<<": "<<x<<" "<<(num-y)<<endl;
	}
}