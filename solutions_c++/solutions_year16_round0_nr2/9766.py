#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

#if 1
int check(string s){
	if(s.size() == 0 )
		return 0;
	if(s.size() == 1 ){
		return 1;
	}
	int res = 1;
	int start;
	for(start=0;start<s.size();start++) if(s[start] == '-') break;

	if(start == s.size())
		return 0;
	reverse(s.begin(),s.begin()+start);
	if(start != 0){
		res++;

		for(int i=0;i<start;i++){
			if(s[i] == '+')
				s[i] = '-';
			else
				s[i] = '+';
			
		}
	}	

	reverse(s.begin(),s.end());
	for(int i=0;i<s.size();i++){
		if(s[i] == '+')
			s[i] = '-';
		else
			s[i] = '+';
		
	}

	int end;
	for(end=s.size()-1;end>=0;end--) if(s[end] == '-') break;
	return res+check(s.substr(0,end+1));
}

int main(){
	ifstream fin("B-large.in");
	ofstream fout("result.txt");

	int T;
	fin>>T;
	for(int t=1;t<=T;t++){
		string s;
		fin>>s;
		int end;
		for(end=s.size()-1;end>=0;end--) if(s[end] == '-') break;
		
		fout<<"Case #"<<t<<": "<<check(s.substr(0,end+1))<<endl;

		
	}

	return 0;
}
#endif