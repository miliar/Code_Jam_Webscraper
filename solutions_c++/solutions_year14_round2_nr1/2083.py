#include<iostream>
#include<string>
#include<fstream>
#include<vector>
#include<math.h>
#include<algorithm>
using namespace std;

int N;
string str[1000];
bool flag;
int steps;

void showAns(int round, ofstream& file,bool flag){
	file<<"Case #"<<round<<": ";
	if(flag)
		file<<steps;
	else
		file<<"Fegla Won";
	file<<endl;
	return;
}

string simplify(string& str){
	int len = str.size();
	string temp="";
	temp+=str[0];
	int idx = 1;
	while(idx<len){
		if(str[idx]!=str[idx-1])
			temp+=str[idx];
		++idx;
	}
	return temp;
}

bool checkPossible(){
	string temp = simplify(str[0]);
	for(int i = 1; i < N; ++i)
		if(simplify(str[i])!=temp)
			return false;
	return true;
}

void getAns(){

	steps=0;
	string temp = simplify(str[0]);
	int num = temp.size();
	vector<int> helper(num,0);
	vector<vector<int> > stringcnt(N,vector<int>(num,0));
	for(int i = 0 ; i < N; ++i){
		int helper_idx = 0;
		helper[0]++;
		int cnt = 1;
		for(int idx= 1; idx<str[i].size();++idx){
			if(str[i][idx]==str[i][idx-1]){
				cnt++;

			}
			else{
				stringcnt[i][helper_idx] = cnt;
				helper_idx++;
				
				cnt=1;
			}
			helper[helper_idx]++;
		}
		stringcnt[i][num-1] = cnt;
	}

	for(int i = 0; i < num; ++i){
		helper[i]/=N;
	}

	for(int i = 0 ; i <N; ++i){
		for(int j = 0; j <num; ++j){
			steps+=abs(stringcnt[i][j]-helper[j]);
		}
	}

	return;

}

void main(){
	ifstream file("A-small-attempt0.in");
	if(!file)
		return;
	int T = 0;
	file>>T;
	ofstream outfile("output");
	for(int idx = 1; idx<=T; ++idx){
		file>>N;
		
		for(int i = 0; i <N; ++i){
			file>>str[i];
		}
		if(checkPossible()){
			flag = true;
			getAns();
		}
		else
			flag = false;
		showAns(idx,outfile,flag);	
	}
	outfile.close();
	file.close();

}



