#include<fstream>
#include<string>

using namespace std;

int main(){
	ifstream fin("inp.txt");
	ofstream fout("op.txt");
	int t;
	fin>>t;
	for(int ca=1;ca<=t;ca++){
		string str;
		fin>>str;
		int len=str.length(),i;
		string res;
		res += str[0];
		for(i=1;i<len;i++){
			string left=str[i]+res;
			string right=res+str[i];
			if(left.compare(right)>0)
				res=left;
			else
				res=right;
		}
		fout<<"Case #"<<ca<<": "<<res<<"\n";
	}
}