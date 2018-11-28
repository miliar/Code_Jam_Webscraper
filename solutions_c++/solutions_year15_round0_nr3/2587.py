#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string s;

int map[5][5] = { {0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

int check(char a){
	if(a=='i') return 2;
	if(a=='j') return 3;
	if(a=='k') return 4;
	return 1;
}

int main()
{
	int n,N;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("output.txt");
	
	fin>>N;

	for(n=0;n<N;n++){
		string s,tmp;
		int x,l;
		int i;
		fin>>l>>x;
		fin>>tmp;

		for(i=0;i<x;i++) s += tmp;

		
		int cc = check(s[0]);
		for(i=1;i<s.size();i++){
			if(cc == 2)
				break;
			if(cc < 0)
				cc = -1 * map[-cc][check(s[i])];
			else
				cc = map[cc][check(s[i])];
		}

		if( i == s.size() ){
			fout<<"Case #"<<n+1<<": NO"<<endl;
			continue;
		}
		int start = i;

		for(i = s.size() -1 ;i>=0;i--){
			cc = check(s[i]);
			for(int j=i+1;j<s.size();j++){
				if(cc < 0)
					cc = -1 * map[-cc][check(s[j])];
				else
					cc = map[cc][check(s[j])];
			}
			if(cc == 4)
				break;
		}
		if(i< start){
			fout<<"Case #"<<n+1<<": NO"<<endl;
			continue;
		}
		int end = i;
		cc = check(s[start]);
		for(i = start+1;i<end;i++){
			if(cc < 0)
				cc = -1 * map[-cc][check(s[i])];
			else
				cc = map[cc][check(s[i])];
		}
		if(cc != 3){
			fout<<"Case #"<<n+1<<": NO"<<endl;
			continue;
		}
		fout<<"Case #"<<n+1<<": YES"<<endl;
	}


	return 0;
}