#include<iostream>
#include<cmath>
#include<string>
#include<vector>
#include<algorithm>
#include<utility>
#include<memory.h>
#include<cstring>
#include<fstream>

using namespace std;

const long long MOD = 1e9 + 7;

const double eps = 1e-8;

double m1[1111], m2[1111];
int u1[1111], u2[1111];

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin >> T;
	for (int q = 1; q <= T; q++){
		int n;
		cin >> n;
		for (int i = 0; i < n; i++) cin >> m1[i];
		for (int i = 0; i < n; i++) cin >> m2[i];
		sort(m1, m1 + n);
		sort(m2, m2 + n);
		int s1 = 0, s2 = 0;
		for (int i = 0, j = 0; i < n && j < n;){
			if (m1[i]>m2[j]) j++;
			else{
				i++, j++, s2++;
			}
		}
		s2 = n - s2;
		memset(u1, 0, sizeof(u1));
		memset(u2, 0, sizeof(u2));
		int u = 0;
		while (u < n){
			int min_id1 = -1, min_id2 = -1, max_id1 = -1, max_id2 = -1;
			for (int i = 0; i < n; i++){
				if (!u1[i]){
					max_id1 = i;
					if (min_id1 < 0) min_id1 = i;
				}
				if (!u2[i]){
					max_id2 = i;
					if (min_id2 < 0) min_id2 = i;
				}
			}
			if (m1[max_id1] < m2[max_id2]){
				u1[min_id1] = 1;
				u2[max_id2] = 1;
			}
			else{
				for (int i = min_id1; i <= max_id1; i++){
					if (!u1[i] && m1[i]>m2[min_id2]){
						u1[i] = 1;
						break;
					}
				}
				s1++;
				u2[min_id2] = 1;
			}
			u++;
		}
		cout << "Case #" << q << ": " << s1 << " " << s2 << endl;
	}
}