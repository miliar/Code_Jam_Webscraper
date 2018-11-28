#include<fstream>
#include<string>
#include<vector>

using namespace std;

int minInvite(string &s){
	int c = 0, all=0;
	for (int i = 0; i < s.size(); i++){
		if (all < i){
			int k = i - all;
			all += k;
			c+=k;
			//s[i] = '1';
		}
		all += s[i] - '0';
	}
	return c;
}

int main(){
	ifstream in("A-large.in");
	ofstream out("ans.txt");
	int T;
	in >> T;
	for (int t = 1; t <= T; t++){
		int n;
		string s;
		in >> n;
		while (s.size() == 0){
			in >> s;
		}
		int ans = minInvite(s);
		out << "Case #" << t << ": " << ans << endl;
	}
	in.close();
	out.close();
}