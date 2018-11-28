#include<iostream>
#include<map>
#include<string>
#include<fstream>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>
#include<stdio.h>
#include<math.h>
#include<cmath>
#include<string>

using namespace std;

int main(){

	int t;
	cin>>t;
	string s;
	int in = 0;
	while(t--){
		in++;
		cin>>s;
		vector <pair <int, char> > v;
		v.push_back(make_pair(0,s[0]));
		int l=-1,r=1;
		char last = s[0];
		for(int i=1;i<s.size();i++){
			if(s[i] >= last){
				v.push_back(make_pair(l,s[i]));
				last = s[i];
				l--;
			}
			else{
				v.push_back(make_pair(r,s[i]));
				r++;
			}
		}
		
		sort(v.begin(),v.end());
		string rr = "";
		for(int i=0;i<v.size();i++){
			rr+=v[i].second;
		}
		
		cout<<"Case #"<<in<<": "<<rr<<endl;
	}
	
	
	return 0;
}
