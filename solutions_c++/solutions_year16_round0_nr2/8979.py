#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <unordered_map>
using namespace std;

bool allPlus(string &s){
	int len = s.size();
	for(int i = 0; i < len; i ++){
		if(s[i] == '-')
			return false;
	}
	return true;
}

string flip(int start, int end, string s){
	int len = s.size();
	vector<char> tmp;
	for(int i = end; i >= start; i--){
		tmp.push_back(s[i] == '+' ? '-' : '+');
	}
	for(int i = start; i <= end; i++)
		s[i] = tmp[i];
	return s;
}

int compute(int start, int end, string s,int step, int &min, set<string> &st, set<string> &m){
	string tmp = s;	
	//st.insert(s);
	for(int i = start; i <= end; i++){
		tmp = flip(0,i,s);		
		if( allPlus(tmp)){
			if (step < min){
				min = step;	
				return step;
			}
		} 
		else		
			if( m.find(tmp) == m.end() && st.find(tmp) == st.end()){
				if(step == 1){
					m.insert(tmp);
				}
				//cout<<"Added : "<<tmp<<endl;					
				st.insert(tmp);		
				compute(i,end,tmp, step+1, min,st,m);
				//cout<<"Removed : "<<tmp<<endl;					
				st.erase(tmp);
			}

		//st.erase(tmp);
	}
	//st.erase(s);
	return step;
	
}

int main(){
	int c=1,t;
	cin>>t;
	while(c <= t){
		string s;			
		cin>>s;
		if(allPlus(s))
			cout<<"Case #"<<c<<": "<<0<<endl;
		else {
			int ans = 9999999;
			set<string> st;	
			set<string> m;
			//st.insert(s);
			compute(0, s.size()-1,s,1,ans,st,m);			
			cout<<"Case #"<<c<<": "<<ans<<endl;	
		}
		c++;
	}
	return 0;
}
