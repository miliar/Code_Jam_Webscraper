#include<iostream>
#include<fstream>

using namespace std;


int main(){
	ifstream f1("A-small-attempt0.in");
	ofstream f2("A-small-attempt0.out");

	int T;
	f1>>T;
	for(int mt=0;mt<T;mt++){
		long long r,t;
		f1>>r>>t;
		int y=0;
		long long s;

		while(1){
			s=2*r+1;
			if(s<=t){
				y++;
				t-=s;
				r+=2;
			}else
				break;
		}

		f2<<"Case #"<<mt+1<<": "<<y<<endl;

	}

	f1.close();
	f2.close();
	return 0;
}
