#include<iostream>
#include<map>
#include<string>
#include<fstream>
#include<vector>
#include<queue>
#include<set>
#include<algorithm>

using namespace std;

int arr[30];
vector <vector <int> > v;
string r = "";
string s;

bool solve(int q){
	//cout<<"!"<<q;
	if(q == 10){
		for(int i=0;i<26;i++){
			if(arr[i] > 0){
				//cout<<" False"<<endl;
				return false;
			}
		}
		//cout<<" T"<<endl;
		return true;
	}
	
	bool is = true;
	for(int j=0;j<v[q].size();j++){
		if(arr[j] < v[q][j]){
			is = false;
		}
	}
	if(is){
		for(int j=0;j<v[q].size();j++){
			arr[j] -= v[q][j];
		}
		bool is2 = false;
		for(int i=q;i<=10;i++){
			if(solve(i)){
				is2 = true;
				r = char(q+'0') + r;
				//cout<<"r is "<<r<<endl;
				return true;
				i--;
			}
		}
		if(!is2){
			for(int j=0;j<v[q].size();j++){
			arr[j] += v[q][j];
			}
		}
	}
}


int main(){

	int t;
	cin>>t;
	int in = 1;
	string s;
	
	string ss[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	vector <int> tt;
	for(int i=0;i<10;i++){
		v.push_back(tt);
		for(int j=0;j<26;j++){
			v[i].push_back(0);
		}
		for(int j=0;j<ss[i].size();j++){
			v[i][ss[i][j]-'A']++;
		}
	}
	while(t--){
		cin>>s;
		r = "";
		for(int i=0;i<30;i++){
			arr[i]=0;
		}
		for(int i=0;i<s.size();i++){
			arr[int(s[i]-'A')]++;
		} 
		
		for(int i=0;i<10;i++){
			if(solve(i)){
				break;
			}
		}
		
		cout<<"Case #"<<in<<": "<<r<<endl;;
		in++;
	}
	
	return 0;
}