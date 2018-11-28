#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main(){
	std::ifstream ifs("A-small.in");
	std::ofstream ofs("result.txt");

	if(ifs.fail()){
		std::cout<<"error"<<std::endl;
		exit(0);
	}

	int N,C,I,tmp,T;
	int a,b;
	int ans1,ans2;
	int number1[4][4];
	int number2[4][4];
	int count=0;
	std::vector<int> result;

	char *ctx;

	std::string str;
	std::vector<int> item;
	
	getline(ifs,str);
	sscanf_s(str.data(),"%d",&T);
	//std::cout<<C<<std::endl;

	for(int i=1;i<=T;i++){

		getline(ifs,str);
		sscanf_s(str.data(),"%d",&ans1);

		for(int j=0;j<4;j++){
			getline(ifs,str);
			char *tp;
			tp=strtok_s((char*)str.c_str()," ",&ctx);

			number1[j][0] = atoi(tp);

			for(int k=1;k<4;k++){
				tp = strtok_s(NULL," ",&ctx);
				number1[j][k] = atoi(tp);
			}
		}

		getline(ifs,str);
		sscanf_s(str.data(),"%d",&ans2);

		for(int j=0;j<4;j++){
			getline(ifs,str);
			char *tp;
			tp=strtok_s((char*)str.c_str()," ",&ctx);

			number2[j][0] = atoi(tp);

			for(int k=1;k<4;k++){
				tp = strtok_s(NULL," ",&ctx);
				number2[j][k] = atoi(tp);
				std::cout<<atoi(tp)<<std::endl;
			}
		}

		result.clear();

		for(int j=0;j<4;j++){
			tmp = number1[ans1-1][j];
			for(int k=0;k<4;k++){
				if(number2[ans2-1][k] == tmp){
					result.push_back(tmp);
				}
			}
		}
		
		if(result.size()==0){
			ofs<<"Case #"<<i<<": "<<"Volunteer cheated!"<<std::endl;
		}else if(result.size()==1){
			ofs<<"Case #"<<i<<": "<<result.front()<<std::endl;
		}else{
			ofs<<"Case #"<<i<<": "<<"Bad magician!"<<std::endl;
		}

	}
}