#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>

using namespace std;

int main(){
	std::ifstream ifs("B-large.in");
	std::ofstream ofs("result.txt");

	if(ifs.fail()){
		std::cout<<"error"<<std::endl;
		exit(0);
	}

	int T;
	double C;
	double F;
	double X;
	
	double cps; //cookie per second
	double cookie;
	double time;
	double time_worst;
	double time_tmp;

	char *ctx;
	char *tp;

	std::string str;
	
	getline(ifs,str);
	sscanf_s(str.data(),"%d",&T);
	//std::cout<<C<<std::endl;

	for(int i=1;i<=T;i++){
		std::cout<<"case "<<T<<std::endl;

		getline(ifs,str);
		tp=strtok_s((char*)str.c_str()," ",&ctx);
		C = atof(tp);
		tp = strtok_s(NULL," ",&ctx);
		F = atof(tp);
		tp = strtok_s(NULL," ",&ctx);
		X = atof(tp);

		cookie=0;
		cps=2.0;
		time=0.0;

		time_worst = X/2.0;
		//std::cout<<"time_worst "<<time_worst<<std::endl;
		//getchar();
		while(1){

			time += C/cps;

			time_tmp = time + (X/(cps+F));
			if(time_worst > time_tmp){
				cps+=F;
				time_worst = time_tmp;
			}else{
				time = time_worst;
				break;
			}
			//std::cout<<time<<std::endl;
		}

		ofs<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<time<<std::endl;


	}
}