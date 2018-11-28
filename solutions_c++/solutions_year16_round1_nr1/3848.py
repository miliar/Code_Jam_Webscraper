#include <fstream>
#include <list>
#include <string>

using namespace std;

string S;
int len;

list<char> ls;

int main(){
	int T;
	ifstream fin("input.in");
	ofstream fout("output.txt");
	fin>>T;
	for (int i=0;i<T;i++){
		fin>>S;
		len=S.length();
		ls.clear();
		ls.push_back(S[0]);
		for (int j=1;j<len;j++){
			if (S[j]>=ls.front()){
				ls.push_front(S[j]);
			}
			else{
				ls.push_back(S[j]);
			}
		}
		fout<<"Case #"<<i+1<<": ";
		list<char>::iterator ite=ls.begin();
		for (;ite!=ls.end();ite++){
			fout<<*ite;
		}
		fout<<endl;
	}
	return 0;
}