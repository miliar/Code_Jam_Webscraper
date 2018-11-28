#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
using namespace std;

string tos(int n, int len) {
	string s;
	for (int i=0;i<len;i++) {
		if ((n>>i) & 1) {
			s+='1';
		} else s+='0';
	}
	reverse(s.begin(),s.end());
	return s;
}

vector <long long> p;


int f(long long n) {
	for (int i=0;i<p.size() && p[i]*p[i]<n;i++) {
		if (n % p[i] == 0)return p[i];
	}
	return -1;
}
int v[34801021];
int main() {
	freopen("test.txt", "r", stdin);
	freopen("test.out.txt", "w", stdout);
	
	memset(v, 0, sizeof(v));
	//int x = sqrt(1211111111111111);
	//cout << x << endl;
	for (int i=2;i<34801021;i++) {
		if (!v[i]) {
			p.push_back(i);
			for(int j=i+i;j<34801021;j+=i)
				v[j]=1;
		}
	}
	//cout << p.size() << endl;

	int t;
	cin>>t;

	for (int cas = 1; cas <= t; cas++) {
		int n, j;
		cin>>n>>j;
		int cnt = 0;
		cout << "Case #"<< cas << ":" << endl;
		for (int i=0;i<(1<<(n-2));i++) {
			long long cur;
			string s = "1" + tos(i, n-2) + "1";
			int flag  = 0;
			for (int base=2;base<=10;base++) {
				cur = 0;
				for (int j=0;j<s.size();j++) {
					cur = cur * base + s[j]-'0';
					//cout << "??x " << cur << endl;
				}
				//cout << cur << endl;
				if (f(cur) == -1) {
					flag = 1;
					break;
				}	
				//cout << cur << " ";			
			}
			//cout << endl;
			if (flag == 1) continue;

			cout << s << " ";
			// for (int base=2;base<=10;base++) {
			// 	cur = 0;
			// 	for (int j=0;j<s.size();j++) {
			// 		cur = cur * base + s[j]-'0';
			// 		//cout << "??x " << cur << endl;
			// 	}

			// 	cout << cur << " ";
					
			// }
			// cout << endl;
			for (int base=2;base<=10;base++) {
				cur = 0;
				for (int j=0;j<s.size();j++) {
					cur = cur * base + s[j]-'0';
					//cout << "??x " << cur << endl;
				}

				if (base == 10)
					cout << f(cur) << endl;
				else 
					cout << f(cur) << " ";
					
			}
			cnt++;
			if (cnt==j)break;
 		}

		//cout << "Case #" << cas << ": " << cnt * 2 + num << endl;
	}
	return 0;
}