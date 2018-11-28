#include <fstream>
#include <string>

using namespace std;

string S;

int dfs(int i,char c){
	//[0,i]‚ð‚·‚×‚Äc‚É•Ï‚¦‚é
	if (i==0){
		if (S[0]!=c){
			return 1;
		}
		else{
			return 0;
		}
	}
	if (S[i]==c){
		return dfs(i-1,c);
	}
	else{
		return dfs(i-1,S[i])+1;
	}
}

int main(){
	ifstream fin("input.in");
	ofstream fout("output.txt");
	int T;
	fin>>T;
	for (int i=0;i<T;i++){
		fin>>S;
		fout<<"Case #"<<i+1<<": "<<dfs(S.size()-1,'+')<<endl;
	}
	return 0;
}