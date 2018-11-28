#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <functional>
#include <sstream>


using namespace std;

int main(){
	std::ifstream ifs("A-small.in");
	std::ofstream ofs("result.txt");

	

	int T;
	
	__int64 P,Q;
	char c;
	ifs >> T;

	vector<long> n;
	n.clear();
	for(int i=1;i<=40;i++){
		n.push_back(powl(2,i));
	}
	vector<long>::iterator it;

	for(int t=1;t<=T;t++){
		ifs>>P;
		ifs>>c;
		ifs>>Q;

		cout<<"t:"<<t<<" "<<P<<" "<<Q<<endl;

		long i=2;
		while(i<=P){
			if(Q%2==0 && P%2==0){
				P/=i;
				Q/=i;

			}else{
				for(i=3;i<=P;i+=2){

					if(P%i==0 && Q%i==0){
						P/=i;
						Q/=i;
					}

				}
			}
		}
		cout<<P<<" "<<Q<<endl;
		int l = (int)(log10l(Q)/log10l(2));
		int j=0;
		bool flag = true;

		while(Q>1){
			if((it = find(n.begin(),n.end(),Q)) == n.end()){
				flag = false;
				break;
			}

			Q/=2;

			j++;

			if(P>=Q){
				break;
			}
		}

		if(flag==false){
			ofs<<"Case #"<<t<<": impossible"<<endl;			
		}else{
			ofs<<"Case #"<<t<<": "<<j<<endl;
		}
	}
}