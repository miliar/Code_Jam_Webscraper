#include<iostream>
#include<fstream>
#include<string>
#include<list>
using namespace std;
int main(){
	ifstream fin("A-large.in");
	ofstream fout("A_word.out");
	int N;
	fin>>N;
	string curr;
	for(int zzz=1; zzz<=N; zzz++){
		fin>>curr;
		//cout<<curr.length()<<endl;
		list<char> rslt;
		for(int i=0; i<curr.length(); i++){
			if(i==0) rslt.push_back(curr[i]);
			else
			{
				if(curr[i]<rslt.front())
					rslt.push_back(curr[i]);
				else
					rslt.push_front(curr[i]);
			}
		}
		fout<<"Case #"<<zzz<<": ";
		while(!rslt.empty()){
			fout<<rslt.front();
			rslt.pop_front();
		}
		fout<<endl;
	}
}
