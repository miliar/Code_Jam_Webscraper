#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>

using namespace std;

int war(std::vector<double> Naomi,std::vector<double> Ken){
	int ans=0;

	while(Naomi.size()!=0){
		if(Naomi.front() < Ken.front()){
			if(Naomi.back()<Ken.back()){
				Naomi.erase(Naomi.end()-1);
				Ken.erase(Ken.end()-1);
			}else{
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.begin());
			}
		}else{
			if(Naomi.back()<Ken.back()){
				Naomi.erase(Naomi.end()-1);
				Ken.erase(Ken.end()-1);
			}else{
				Naomi.erase(Naomi.end()-1);
				Ken.erase(Ken.begin());
				ans++;
			}
		}
	}

	return ans;
}

int deciteful_war(std::vector<double> Naomi,std::vector<double> Ken){
	int ans=0;

	while(Naomi.size()!=0){
		if(Naomi.front() < Ken.front()){
			if(Naomi.back()<Ken.back()){
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.end()-1);
			}else{
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.end()-1);
			}
		}else{
			if(Naomi.back()<Ken.back()){
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.end()-1);
			}else{
				Naomi.erase(Naomi.begin());
				Ken.erase(Ken.begin());
				ans++;
			}
		}
	}

	return ans;

}

int main(){
	std::ifstream ifs("D-large.in");
	std::ofstream ofs("result.txt");

	if(ifs.fail()){
		std::cout<<"error"<<std::endl;
		exit(0);
	}

	char *ctx;
	char *tp;

	std::string str;

	std::vector<double>Naomi,Ken;
	int ans1,ans2;

	int T,N;
	getline(ifs,str);
	sscanf_s(str.data(),"%d",&T);

	for(int i=1;i<=T;i++){
		Naomi.clear();
		Ken.clear();

		getline(ifs,str);
		sscanf_s(str.data(),"%d",&N);

		getline(ifs,str);
		tp=strtok_s((char*)str.c_str()," ",&ctx);
		Naomi.push_back(atof(tp));
		for(int j=1;j<N;j++){
			tp = strtok_s(NULL," ",&ctx);
			Naomi.push_back(atof(tp));
		}

		getline(ifs,str);
		tp=strtok_s((char*)str.c_str()," ",&ctx);
		Ken.push_back(atof(tp));
		for(int j=1;j<N;j++){
			tp = strtok_s(NULL," ",&ctx);
			Ken.push_back(atof(tp));
		}

		std::sort(Naomi.begin(),Naomi.end());
		std::sort(Ken.begin(),Ken.end());

		ans1 = deciteful_war(Naomi,Ken);
		ans2 = war(Naomi,Ken);



		ofs<<"Case #"<<i<<": "<<ans1<<" "<<ans2<<std::endl;


	}
}