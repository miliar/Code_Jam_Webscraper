#include<fstream>
#include<string>

using namespace std;

int toint(string str){
	int num=0;
	for(int i=0; i<str.length(); i++){
		num *= 10;
		num += (str[i]-'0');
	}
	return num;
}

void helper(string s1, string s2, string &f1, string &f2, int i, int j, int &diff){
	if(i==s1.length() && j==s2.length()){
		int curdiff=toint(s1)-toint(s2);
		if(curdiff < 0)
			curdiff=-curdiff;
		if(diff==-1){
			diff=curdiff;
			f1=s1;
			f2=s2;
		}
		else if(diff > curdiff){
			diff=curdiff;
			f1=s1;
			f2=s2;
		}
		return;
	}
	if(i<s1.length() && s1[i]=='?'){
		for(char ch='0'; ch<='9'; ch++){
			s1[i]=ch;
			helper(s1,s2,f1,f2,i,j,diff);
		}
	}
	if(j<s2.length() && s2[j]=='?'){
		for(char ch='0'; ch<='9'; ch++){
			s2[j]=ch;
			helper(s1,s2,f1,f2,i,j,diff);
		}
	}
	helper(s1,s2,f1,f2,i+1,j+1,diff);
}


int main(){
	ifstream fin("inp.txt");
	ofstream fout("out.txt");
	int t;
	fin>>t;
	for(int ca=1; ca<=t; ca++){
		string s1,s2;
		fin>>s1>>s2;
		string f1,f2;
		int diff=-1;
		helper(s1,s2,f1,f2,0,0,diff);
		fout<<"Case #"<<ca<<": "<<f1<<" "<<f2<<"\n";
	}
}