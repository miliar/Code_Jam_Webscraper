#include<fstream>
#include<vector>
#include<string>
#include<algorithm>
#include<iterator>
using namespace std;


void delNum(string&, string);
int main(){
	ofstream fout("out.txt");
	ifstream fin("in.txt");
	int T;
	int i=0;
	fin>>T;
	while(T--){
		string s;
		fin>>s;
		vector<int> res;
		while(find(s.begin(),s.end(),'Z')!=s.end()) { delNum(s,"ZERO"); res.push_back(0);}
		while(find(s.begin(),s.end(),'W')!=s.end()) { delNum(s,"TWO"); res.push_back(2);}
		while(find(s.begin(),s.end(),'U')!=s.end()) { delNum(s,"FOUR"); res.push_back(4);}
		while(find(s.begin(),s.end(),'X')!=s.end()) { delNum(s,"SIX"); res.push_back(6);}
		while(find(s.begin(),s.end(),'G')!=s.end()) { delNum(s,"EIGHT"); res.push_back(8);}
		while(find(s.begin(),s.end(),'O')!=s.end()) { delNum(s,"ONE"); res.push_back(1);}
		while(find(s.begin(),s.end(),'S')!=s.end()) { delNum(s,"SEVEN"); res.push_back(7);}
		while(find(s.begin(),s.end(),'V')!=s.end()) { delNum(s,"FIVE"); res.push_back(5);}
		while(find(s.begin(),s.end(),'I')!=s.end()) { delNum(s,"NINE"); res.push_back(9);}
		while(s.length()) { delNum(s,"THREE"); res.push_back(3);}
		fout<<"Case #"<<i+1<<": ";
		sort(res.begin(),res.end());
		for(int k=0; k<res.size(); k++) fout<<res[k];
		fout<<endl;
		i++;
	}
	
	return 0;
	
}

void delNum(string& s, string n){
	for(int i=0; i<n.length(); i++){
		s.erase(find(s.begin(),s.end(),n[i]));		
	}
}
