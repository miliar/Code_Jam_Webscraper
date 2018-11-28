#include<fstream> 
using namespace std;

int main(){
	int t;
	ifstream in("A-large.in");
	ofstream out("word.out");
	in >> t;
	for (int tt = 0; tt < t;tt++){
		string s,ans;
		char first;
		int index = 0;
		ans = "";
		in >> s;
		first = s[0];
		ans = ans + first;
		for (int i = 1; i < s.length(); i++){
			index = 0;
			while (s[i] == ans[index] && index < ans.length()-1) index++;
			if (s[i] > ans[index]){
				ans = s[i] + ans;
				first = s[i];
			}else{
				ans = ans + s[i];
			}
		}
		out << "Case #" << tt+1 << ": " << ans << endl;
	}
	in.close();
	out.close();
	return 0;
}
