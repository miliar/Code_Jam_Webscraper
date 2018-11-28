#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main(){
	int t,n;
	vector<vector <int> > count;
	vector<vector <char> > str;
	vector<int> c_dum;
	vector<char> s_dum;  
	char c;
	int cont;
	bool ans;
	string s;
	cin>>t;
	for(int i=0;i<t;i++){
		cin>>n;
		ans =true;
		for(int j=0;j<n;j++){
			cin>>s;
			c = s[0];
			c_dum.push_back(1);
			s_dum.push_back(c);
			if(j != 0 && str[0][0] != c)ans = false;
			for(int k=1;k<s.size();k++){
				if(s[k] == s[k-1]){
					c_dum[c_dum.size()-1]++;
				}
				else{
					c_dum.push_back(1);
					s_dum.push_back(s[k]);
					if(j != 0 && str[0][s_dum.size()-1] != s[k])ans = false;
				}
			}
			if(j != 0 && s_dum.size() != str[0].size())ans = false;
			count.push_back(c_dum);
			str.push_back(s_dum);
			c_dum.clear();
			s_dum.clear();
		}
		cout<<"Case #"<<i+1<<": ";
		if(!ans)cout<<"Fegla Won\n";
		else{
			int a=0,sum;
			vector<int> dum;
			for(int j=0;j<str[0].size();j++){
				sum = 0;
				for(int k=0;k<n;k++){
				//	cout<<count[k][j]<<" ";
					sum = sum + count[k][j];
					dum.push_back(count[k][j]);
				}
				float avg = sum/n;
				int b = sum/n;
				//cout<<"b "<<b<<"\n";
				if(avg - b > 0.5)b++;
				for(int k=0;k<n;k++){
					a = a + abs(b - count[k][j]);
				}
				dum.clear();
			}
				//cout<<"size "<<dum.size();
				/*sort(dum.begin(),dum.end());
				int first=dum[0],b=1,final=0;
				for(int m=1;m<n;m++){
					if(dum[m] == dum[m-1])b++;
					else{
						final = max(final,b);
						b = 1;
					}
				}
				final = max(final,b);
				a = a + n - final;
				dum.clear();
			}*/
			cout<<a<<"\n";
		}
		count.clear();
		str.clear();
		/*for(int j=0;j<str[0].size();j++)
			cout<<str[0][j]<<" "; */
	}
}
