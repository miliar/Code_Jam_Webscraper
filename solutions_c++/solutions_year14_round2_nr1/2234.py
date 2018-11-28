#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("A-small-attempt0.in","r", stdin);
	freopen("outputA.out","w",stdout);
	int T, N;
	string s1, s2;
	cin >> T;
	for (int i = 1; i <= T; i++){
		cin >> N;
		cin >> s1 >> s2;
		
		int t1 = 1;
		int l1 = 1;
		int dem1 = 0;
		int d1[105];
		string c1 = "";
		c1 += s1[0];
		
		while(t1 < s1.length()){
			if (s1[t1] == s1[t1-1]) l1 ++;
			else{
				c1 += s1[t1];
				d1[++dem1] = l1;
				l1 = 1; 
			} 
			t1++;
		}
		d1[++dem1] = l1;
		
		int t2 = 1;
		int l2 = 1;
		int dem2 = 0;
		int d2[105];
		string c2 = "";
		c2 += s2[0];
		
		while(t2 < s2.length()){
			if (s2[t2] == s2[t2-1]) l2 ++;
			else{
				c2 += s2[t2];
				d2[++dem2] = l2;
				l2 = 1; 
			} 
			t2++;
		}
		d2[++dem2] = l2;
		cout << "Case #" << i << ": "; 
		if (c1 != c2) cout << "Fegla Won" << endl;
		else{
			int res = 0;
			for (int t = 1; t <= dem1; t++)
				res += abs(d1[t] - d2[t]);
			cout << res << endl;
		}
	}
}
