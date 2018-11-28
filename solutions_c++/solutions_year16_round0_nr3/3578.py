
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <vector> 
#include <string>     // std::string, std::stoi
#include <unordered_set>
#include <stdlib.h>
#include <algorithm>
#include <vector> 
using namespace std;

bool isprime(long long number){

    if(number < 2) return false;
    if(number == 2) return true;
    if(number % 2 == 0) return false;
    for(long long i=3; (i*i)<=number; i+=2){
        if(number % i == 0 ) return false;
    }
    return true;

}

int base(string s,int n,string& divs){
	long long ans = 0;
	long long d = 2;
	for(int i=s.size()-1;i>=0;i--){
		long long cur = pow(n,s.size()-1-i)*(s[i]-'0');
		ans = ans + cur;
	}
	if(isprime(ans))return -1;
	// cout<<s<<endl;
	// cout<<ans<<endl;
	while(ans%d!=0){
		d++;
		if(d == ans)d++;
		//cout<<d<<endl;
	}
	
	// cout<<d<<endl;
	// cout<<endl;
	divs = divs + " " + to_string(d);
	return ans;
}


vector<vector<string> > generate(vector<int>test){
	vector<vector<string> > ans;
	vector<string>cur;
	string divs;
	int i;
	int j;
	long long num;
	int sz = test[0]-2;
		
	long long max = pow(2,sz);
	//cout<<max<<endl;
	for(int i=0;i<max;i++){
		string tmp(sz,'0');
		int n = sz;
		long long val = i;
		while(val>0){
			//if(i==0)break;
			tmp[sz-n] = val%2+'0';
			val = val/2;
			//cout<<val<<endl;
			n--;
		}
		tmp.push_back('1');
		tmp.insert(0,"1");
		//cout<<tmp<<endl;
		for(j=2;j<=10;j++){	
				
			num = base(tmp,j,divs);
			// cout<<comb[i]<<endl;
			// cout<<num<<endl;
			// cout<<j<<endl;
			// cout<<endl;
			if(num == -1){
				divs.clear();
				break;
			}
			
		}
		if(j>10){//all prime
			cur.push_back(tmp);
			cur.push_back(divs);
			ans.push_back(cur);
			// cout<<tmp<<endl;
			// cout<<divs<<endl;
			cur.clear();
			divs.clear();
			//cout<<ans.size()<<endl;
			if(ans.size()==test[1])return ans;
		}

	}
	return ans;

}





vector<vector<string> > check(vector<int>test){
	vector<string>comb;
	vector<vector<string> > ans;
	vector<string>cur;
	string divs;
	ans = generate(test);
	
	return ans;

}

void parsefile(char* infile,vector<vector<int> >&test){
	ifstream input;
	input.open(infile,ifstream::in);
	string tmp;
	int row_cnt = 0;
	while(getline(input,tmp)){
		
		//cout<<tmp<<endl;
		if(row_cnt >0){
			vector<int>t;
			test.push_back(t);
			for(int i=0;i<tmp.size();i++){
				if(tmp[i]==' '){
					string num(tmp.begin(),tmp.begin()+i);
					//cout<<"num "<<num<<endl;
					tmp.erase(tmp.begin(),tmp.begin()+i+1);
					// cout<<"tmp "<<tmp<<endl;
					i = 0;
					test[row_cnt-1].push_back(stoi(num));
				}
			}
			string num(tmp.begin(),tmp.end());
			// cout<<"num "<<num<<endl;
			test[row_cnt-1].push_back(stoi(num));
		}
		row_cnt++;
	}
}



int main(int argc,char* argv[]){
	// vector<int>test(2,0);
	// test[0] = 3;
	// test [1] = 2;
	// vector<string>comb;
	// generate(test,comb);
	// cout<<comb.size()<<endl;
	// for(int i=0;i<comb.size();i++){
	// 	cout<<comb[i]<<endl;
	// }

	char* infile = argv[1];
	vector<vector<int> >test;
	parsefile(infile,test);
	for(int i=0;i<test.size();i++){
		vector<vector<string > >curr;
		curr = check(test[i]);
		//cout<<curr.size()<<endl;
		cout<<"Case #"<<i+1<<": "<<endl;
		for(int j=0;j<curr.size();j++){
			for(int k = 0;k<curr[j].size();k = k+2){
				cout<<curr[j][k]<<curr[j][k+1]<<endl;
			}
		}

	}
	return 1;

}