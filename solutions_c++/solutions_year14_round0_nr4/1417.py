#include <string>
#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <list>
#include <set>
#include <numeric>
#include <queue>
#include <stack>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
using namespace std;
typedef long long LL;
typedef pair<double, char> P;
void run(int Case)
{
	vector<double> a;
	vector<double> b;
	vector<P> c;
	int N;
	cin >> N;
	for(int i=0;i<N;i++){
		double v;
		cin >> v;
		a.push_back(v);
		c.push_back(P(v,'a'));
	}
	for(int i=0;i<N;i++){
		double v;
		cin >> v;
		b.push_back(v);
		c.push_back(P(v,'b'));
	}
	sort(a.begin(),a.end());
	sort(b.begin(),b.end());
	sort(c.begin(),c.end());
#if 0
	for(int i=0;i<N;i++){
		cout << a[i] << " ";
	}
	cout << endl;
	for(int i=0;i<N;i++){
		cout << b[i] << " ";
	}
	cout << endl;
	for(int i=0;i<2*N;i++){
		cout << c[i].second << " ";
	}
	cout << endl;
#endif
	int p=0;
	for(int i=0;i<N;i++){
		if(a[i]>b[p]){
			p++;
		}
	}
	int q=0;
	for(int i=0;i<N;i++){
		while(i<N&&a[q]>b[i]){
			i++;
		}
		if(i>=N){
			break;
		}
		q++;
	}
	
	cout << "Case #" << Case << ": " << p << " " << N-q << endl;
}

int main() {
	int T;
	cin >> T;
	for (int t=1;t<=T;t++) {
		run(t);
	}
}
