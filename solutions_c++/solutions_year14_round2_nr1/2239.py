#include<string>
#include<vector>
#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;

int ary[100];

string trimm(string orig){
	string temp;
	for(int i = 0; i<orig.size(); i++){
		if( i != 0){
			if(orig[i] != orig[i-1])temp += orig[i];
		}else temp += orig[i];
	}
	return temp;
}
void minus(string& orig){
	
}
int main(){
	ifstream ifs("A-small-attempt2.in");
	ofstream ofs("output.out");
	int numC;
	ifs>>numC;
	for(int g = 0; g<numC; g++){
		int N;
		ifs>>N;
		vector<string> str;
		vector<string> trim;
		string tempS;
		bool hasAns = true;
		for(int i = 0; i<N; i++){
			ifs>>tempS;
			str.push_back(tempS);
			tempS = trimm(tempS);
			trim.push_back(tempS);
			if(i != 0){
				if( trim[i] != trim[i-1])
					hasAns = false;
			}
		}
		int res = 0;
		if(hasAns){
			for(int i = 0; i<trim[0].size(); i++){
				int cntUp = 0, cntD = 0;
				for(int j = 0; j < str[0].size(); j++){
					if( j != 0){
						if( str[0][j] != str[0][j-1])break;
						else cntUp++;
					}else cntUp++;
				}
				for(int j = 0; j < str[1].size(); j++){
					if( j != 0){
						if( str[1][j] != str[1][j-1])break;
						else cntD++;
					}else cntD++;
				}
				int sth = cntUp - cntD;
				if(sth < 0)sth = -sth;
				res += sth;
				if(i != trim[0].size() - 1){
					for(int j = 0; j<str.size(); j++){
						if(j == 0)
							str[0] = str[0].substr(cntUp, str[0].size() - cntUp);
						else
							str[1] = str[1].substr(cntD, str[1].size() - cntD);
					}
				}

			}
		}
		ofs<<"Case #"<<g+1<<": ";
		if(hasAns)ofs<<res<<endl;
		else ofs<<"Fegla Won"<<endl;
	}
	

	system("pause");
}