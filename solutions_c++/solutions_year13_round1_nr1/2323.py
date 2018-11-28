#include <iostream>
using namespace std;

int main(int argc, char *argv[]){

	long long count, t,r;
	cin >> count;
	long long max=0;
	long casenum=1;
	
	while(count--){
		cin >> r >> t;

		
		while(t>=0){

			r++;
			t-= r*r-((r-1)*(r-1));
			if(t>=0)
				max++;
			r++;
		}

		if(max==0)
			max++;

		cout << "Case #"<<casenum<<": "<<max<<endl; 
		casenum++;
		max=0;

	}	
}