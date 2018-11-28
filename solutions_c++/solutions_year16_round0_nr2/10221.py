#include<iostream>
#include<string>
#include<functional>
#include<algorithm>
#include<set>
#include<vector>
#include<queue>
#include<deque>
#include<map>
#include<list>
#include<cmath>
#include<sstream>
#include<fstream>
using namespace std;
int main(){
	int i = 0, j, a, b;
	char ss[101];	
	int T;
	ifstream fin("2.txt");
	ofstream fout("b.txt");
	string s;
	fin>>T;
	while(i < T){
		fin>>s;
		if(i){
			fout<<endl;
		}
		if(s.size() == 0){
			fout<< "Case #"<<i + 1<<": 0";
			i++;
			continue;
		}
		int a = 1;
		ss[0] = s[0];
		for(j = 0;j < s.size(); j++){
			if(ss[a - 1] != s[j]){
				ss[a] = s[j];
				a++;
			}
		}
		if(ss[0] == '-'){
			fout<< "Case #"<<i + 1<<": "<< a + (a % 2) - 1;
		}
		else{
			fout<< "Case #"<<i + 1<<": "<< a/ 2 * 2;			
		}
		i++;
	}
	return 0;
}
