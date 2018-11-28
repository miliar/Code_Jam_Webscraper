#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

string g_ans = "";

vector<int> f(int n){
	string s1 = "";
	if(n==0)
		s1 = "ZERO";
	else if(n==1)
		s1 = "ONE";
	else if( n==2)
		s1 = "TWO";
	else if( n==3)
		s1 = "THREE";
	else if( n==4)
		s1 = "FOUR";
	else if( n==5)
		s1 = "FIVE";
	else if  ( n==6)
		s1 = "SIX";
	else if( n==7)
		s1 = "SEVEN";
	else if( n==8)
		s1 = "EIGHT";
	else if (n==9)
		s1 = "NINE";
	vector<int> g(26,0);
	for(int i=0;i<s1.length();i++)
		g[s1[i]-'A']++;
	return g;
}

bool check(vector<int> m, vector<int>  g){
	for(int i=0; i<26;i++)
		if(g[i]>m[i])
			return false;
	return true;
}

string toString(int n){
	stringstream ss;
	ss<<n;
	return ss.str();
}

bool solve(vector<int> &m, int num,string ans){
	//cout<<"ans "<<ans<<endl;
	//cout<<"num "<<num<<endl;
	bool all_zero = true;
	for(int i=0;i<26;i++){
		if(m[i]!=0){
			all_zero=false;
			break;
		}
	}

	if(all_zero){
		g_ans = ans;
		return true;
	}
	string temp_ans;
	for(int i=num;i<=9;i++){
		vector<int> g = f(i);
		if(check(m,g) ){
			//cout<<"CHECK "<<i<<endl;
			for(int j=0;j<26;j++)
				m[j]-= g[j];
			if(solve(m,i,ans+toString(i)))
				return true;
			else{
				for(int j=0;j<26;j++)
					m[j]+=g[j];
			}	
		}
	}
	return false;
}

int main(){
	int t;
	cin>>t;
	for(int case_num=1; case_num<=t;case_num++){
		string s;
		cin>>s;
		vector<int> m(26,0);
		for(int i=0;i<s.length();i++)
			m[s[i]-'A']++;
		cout<<"Case #"<<case_num<<": ";
		g_ans = "";
		solve(m,0,"");
		cout<<g_ans<<endl;

	}
	return 0;
}
