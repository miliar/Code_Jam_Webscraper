#include <fstream>
#include <string>
#include <algorithm>
#include <map>
#include <vector>

using namespace std;

int main(){
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++){
		string str;
		fin>>str;
		map<char,int>mp;
		for(int i=0; i<str.length(); i++)
			mp[str[i]]++;
		vector<int>dig;
		while(mp.count('Z')){
			dig.push_back(0);
			mp['Z']--;
			if(mp['Z']<=0)
				mp.erase('Z');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
			mp['R']--;
			if(mp['R']<=0)
				mp.erase('R');
			mp['O']--;
			if(mp['O']<=0)
				mp.erase('O');
		}
		while(mp.count('W')){
			dig.push_back(2);
			mp['T']--;
			if(mp['T']<=0)
				mp.erase('T');
			mp['W']--;
			if(mp['W']<=0)
				mp.erase('W');
			mp['O']--;
			if(mp['O']<=0)
				mp.erase('O');
		}
		while(mp.count('U')){
			dig.push_back(4);
			mp['F']--;
			if(mp['F']<=0)
				mp.erase('F');
			mp['O']--;
			if(mp['O']<=0)
				mp.erase('O');
			mp['U']--;
			if(mp['U']<=0)
				mp.erase('U');
			mp['R']--;
			if(mp['R']<=0)
				mp.erase('R');
		}
		while(mp.count('X')){
			dig.push_back(6);
			mp['S']--;
			if(mp['S']<=0)
				mp.erase('S');
			mp['I']--;
			if(mp['I']<=0)
				mp.erase('I');
			mp['X']--;
			if(mp['X']<=0)
				mp.erase('X');
		}
		while(mp.count('G')){
			dig.push_back(8);
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
			mp['I']--;
			if(mp['I']<=0)
				mp.erase('I');
			mp['G']--;
			if(mp['G']<=0)
				mp.erase('G');
			mp['H']--;
			if(mp['H']<=0)
				mp.erase('H');
			mp['T']--;
			if(mp['T']<=0)
				mp.erase('T');
		}
		while(mp.count('H')){
			dig.push_back(3);
			mp['T']--;
			if(mp['T']<=0)
				mp.erase('T');
			mp['H']--;
			if(mp['H']<=0)
				mp.erase('H');
			mp['R']--;
			if(mp['R']<=0)
				mp.erase('R');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
		}
		while(mp.count('O')){
			dig.push_back(1);
			mp['O']--;
			if(mp['O']<=0)
				mp.erase('O');
			mp['N']--;
			if(mp['N']<=0)
				mp.erase('N');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
		}
		while(mp.count('F')){
			dig.push_back(5);
			mp['F']--;
			if(mp['F']<=0)
				mp.erase('F');
			mp['I']--;
			if(mp['I']<=0)
				mp.erase('I');
			mp['V']--;
			if(mp['V']<=0)
				mp.erase('V');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
		}
		while(mp.count('V')){
			dig.push_back(7);
			mp['S']--;
			if(mp['S']<=0)
				mp.erase('S');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
			mp['V']--;
			if(mp['V']<=0)
				mp.erase('V');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
			mp['N']--;
			if(mp['N']<=0)
				mp.erase('N');
		}
		while(mp.count('N')){
			dig.push_back(9);
			mp['N']--;
			if(mp['N']<=0)
				mp.erase('N');
			mp['I']--;
			if(mp['I']<=0)
				mp.erase('I');
			mp['N']--;
			if(mp['N']<=0)
				mp.erase('N');
			mp['E']--;
			if(mp['E']<=0)
				mp.erase('E');
		}
		sort(dig.begin(),dig.end());
		fout<<"Case #"<<ca<<": ";
		for(int i=0; i<dig.size(); i++)
			fout<<dig[i];
		fout<<"\n";
	}
}