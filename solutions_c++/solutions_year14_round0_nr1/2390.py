#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void solve(int T1[4], int T2[4]) {
	int c=0, ans;
	for (int i=0; i<4; i++)
		for (int j=0; j<4; j++)
			if (T1[i]==T2[j]) {
				c++;ans=T1[i];
			}
	if (c==0)
		cout << "Volunteer cheated!";
	if (c>1)
		cout << "Bad magician!";
	if (c==1)
		cout << ans;
	
}

int main() {
    freopen("A-small-attempt0.in", "rt", stdin);
    freopen("A.out", "wt", stdout);
   
    int N;
    cin>>N;

    for (int i=1; i<=N; i++) {
        int T1[4], T2[4], g1, g2, t;
		cin>>g1;
        for (int g=0; g<4; g++)
			for (int j=0; j<4; j++)
				if (g==g1-1)
					cin>>T1[j];
				else
					cin>>t;
		cin>>g2;
        for (int g=0; g<4; g++)
			for (int j=0; j<4; j++)
				if (g==g2-1)
					cin>>T2[j];
				else
					cin>>t;
        cout << "Case #" << i << ": ";
		solve(T1, T2);
		cout<< endl;
    }
}