#include <bits/stdc++.h> 

using namespace std;

typedef long long ll;


int main(){
	int tc ; 
	cin>>tc;
	for(int tt = 1;tt<=tc;tt++){
		char arr[1000];
		string in ; 
		cin>>in;
		strcpy(arr, in.c_str());
		vector<string> vv ; 
		string s ,e; 
		s = e = arr[0];

		vv.push_back(s);
		vv.push_back(e);
		for(int i=1;i<in.size();i++){
			vector<string> tt ;
			for(int j=0;j<vv.size();j++){
				e = s = vv[j];
				string t = in[i] + s;
				s = t;
				e +=in[i];
				tt.push_back(s);
				tt.push_back(e);
			}
			vv.clear();
			vv = tt;
		}
		// for(int i=0;i<in.length();i++){
		// 	vv.push_back(arr[i]);
		// }
		// sort(vv.begin(), vv.end());
		// printf("Case #%d: ",tt );
		// for(int i=vv.size()-1;i>=0;i--){
		// 	cout<<vv[i];
		// }
		sort(vv.begin(), vv.end());
		printf("Case #%d: ",tt );
		cout<<vv[vv.size()-1];
		cout<<endl;
	}
}