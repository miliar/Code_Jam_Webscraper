#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		string s, ans;
		in >> s;
		ans += s[0];
		for (int j = 1; j != s.size(); ++j){
			if(s[j] >= ans[0])
				ans.insert(ans.begin(), s[j]);
			else
				ans += s[j];
		}
		out << "Case #" << i << ": " << ans << endl;
	}
}
