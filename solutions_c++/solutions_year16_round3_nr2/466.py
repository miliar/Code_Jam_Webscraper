#include<map> 
#include<set>
#include<string>
#include<vector>
#include<sstream>
#include<iostream>
#include<algorithm>

using namespace std;

#define		MAX		51

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	unsigned long long p2[MAX],b,m;

	p2[0] = 1;
	for (int i=1;i<MAX;i++) p2[i] = p2[i-1]*2;

	int ntc;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){

		cin >> b >> m;
		unsigned long long k = p2[b-2];
		if (m>k){
			cout << "Case #" << tc << ": IMPOSSIBLE" << endl;
			continue;
		}
		k = m;
		k--;		
		cout << "Case #" << tc << ": POSSIBLE" << endl;
		cout << 0;
		for (int j=1;j<b;j++) cout << 1;
		cout << endl;
		for (int i=1;i<b-1;i++){
			for (int j=0;j<=i;j++) cout << 0;
			for (int j=i+1;j<b-1;j++)
				cout << 1;
			if (k%2)
				cout << 1 << endl;
			else
				cout << 0 << endl;
			k/=2;
		}
		for (int j=0;j<b;j++) cout << 0;
		cout << endl;
	}

	return 0;
}