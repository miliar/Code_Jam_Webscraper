#include <iostream>
#include <fstream>
#include <set>
using namespace std;
ifstream fin("B-large.in");

void process(int t){
	double C,F,X;
	fin>>C>>F>>X;
	int c = 0;
	double time = 0;
	while(true){
		double t1 = X/(2+c*F);
		double t2 = C/(2+c*F) + X/(2+(c+1)*F);
		if(t2<t1){
			time += C/(2+c*F);
			++c;
		}
		else{
			time += t1;
			break;
		}
	}
	printf("Case #%d: %.7f\n",t,time);

}

int main() {
	int T;
	fin>>T;
	for(int i = 1;i<=T;i++)
		process(i);

	return 0;
}
