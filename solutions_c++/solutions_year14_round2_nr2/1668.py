#include<iostream>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
int main() {
//	fstream cin("C:\\Users\\swcandy\\Desktop\\B-small-attempt0 (2).in", ios::in);
//	fstream cout("C:\\Users\\swcandy\\Desktop\\B-small-attempt0.out", ios::out);
	int t,times=0;
	cin >> t;
	while (t--){
		int a, b, k;
		cin >> a >> b >> k;
		int ans = 0;
		for (int i = 0; i < a; i++)
			for (int j = 0; j < b; j++) 
				if ((i&j) < k) 
					ans++;
		cout << "Case #" << ++times << ": " << ans << endl;
	}	
}