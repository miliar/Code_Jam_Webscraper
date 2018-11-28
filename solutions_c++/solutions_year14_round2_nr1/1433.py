#include <iostream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

void solve(vector <string> s) {
	int nr[110][110];
	char cr[110];
	for (int i=0; i<110; i++)
		for (int j=0; j<110; j++)
			nr[i][j]=0;
	for (int i=0; i<110; i++)
		cr[i]=' ';
	string s1="!";
	for (int i=0; i<s.size(); i++) {
		char prev=' ';
		int cnt=-1, cnt1=-1;
		string s2="!";
		for (int j=0; j<s[i].size(); j++){
			if (s[i][j]!=prev) {
				cnt++;
				s2+=s[i][j];
			}
			nr[i][cnt]++;
			prev=s[i][j];
			if (i>0 && cr[cnt]!=s[i][j]) {
				cout << "Fegla Won";
				return;
			}
			cr[cnt]=s[i][j];
		}
		//cout << "1 " << s1 << " " << s2 << endl;
		if (i==0)
			s1=s2;
		else
			if (s2!=s1) {
				cout << "Fegla Won ";// << s1 << " " << s2;
				return;
			}
		//cout << "2 " << s1 << " " << s2 << endl;
	}
	int ans=0;
	for (int j=0; j<110; j++) {
		vector <int> nrs;
		if (nr[0][j]==0) {
			cout << ans;
			return;
		}
		for (int i=0; i<s.size(); i++)
			nrs.push_back(nr[i][j]);
		sort(nrs.begin(), nrs.end());
		int ans1=1<<30;

		for (int a=1; a<110; a++) {
			int ans2=0;
			for (int b=0; b<nrs.size(); b++)
				ans2+=abs(a-nrs[b]);
			ans1=min(ans2,ans1);
		}
		ans+=ans1;
	}
}

int main() {
    freopen("A-large.in", "rt", stdin);
    //freopen("test.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
   
    int T;
    cin>>T;

    for (int i=1; i<=T; i++) {
        int N;
		string ts;
		vector <string> s;
		cin>>N;
	//	cout << endl; // BOO
		for (int j=0; j<N; j++) {
            cin>>ts;
			s.push_back(ts);
//			cout << ts << endl; // BOO
		}
        cout << "Case #" << i << ": ";
		solve(s);
		cout << endl;
    }
}