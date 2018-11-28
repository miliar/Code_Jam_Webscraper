#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int T;
	cin>>T;
	for(int t = 1;t <= T;t++){
		string str = "";
		int l,x;
		cin>>l>>x;
		cin>>str;
		string s = "";

		cout<<"Case #"<<t<<": ";
		for(int i = 0;i < x;i++){
			s += str;
		}
		while(true){
			string t = "";
			//cout<<s<<endl;
			int ok = 0;
			if(s[0] == 'i'){
				t += s[0];
				ok = 1;
				if(s[1] == 'j'){
					t += s[1];
					ok = 2;
					if(s[2] == 'k'){
						t += s[2];
						ok = 3;
						cout<<"YES"<<endl;
						break;
					}
				}
			}
			if(s.size() <= 3){
				cout<<"NO"<<endl;
				//cout<<s<<endl;
				break;
			}
			int a = ok;
			bool cf = false, df = false;
			char c = s[a];
			if(c == '-')cf = true,c = s[a + 1];
			char d = s[a + cf + 1];
			if(d == '-')df = true,d = s[a + cf + 2];
			if(cf^df)t += '-';
			if(c == 'i' && d == 'j')t += "k";
			if(c == 'i' && d == 'k')t += "-j";
			if(c == 'j' && d == 'i')t += "-k";
			if(c == 'j' && d == 'k')t += "i";
			if(c == 'k' && d == 'i')t += "j";
			if(c == 'k' && d == 'j')t += "-i";
			if(c == 'i' && d == 'i')t += "-";
			if(c == 'j' && d == 'j')t += "-";
			if(c == 'k' && d == 'k')t += "-";
			for(int i = a + cf + df + 2;i < s.size();i++){
				t += s[i];
			}
			//cout<<"~"<<t<<endl;
			s = "";
			int num = 0;
			for(int i = 0;i < t.size();i++){
				if(t[i] == '-'){
					num++;
				}
				else s += t[i];
			}
			if(num%2){
				t = "";
				for(int i = 0;i < s.size() - 1;i++)t += s[i];
				t += "-";
				t += s[s.size()-1];
				s = t;
			}
		}
		


	}
}