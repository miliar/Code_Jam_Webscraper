#include <iostream>
#include <string>
#include <iomanip>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
		
	int n;
	long double t_taken=0.0,t_min=0.0;
	double cookie,c,f,x;
	bool less;

	fin.open("B-large.in");
	fout.open("B-large.out");
	
	fin>>n;
	
	for(int i=0;i<n;i++){

		fin>>c>>f>>x;
		t_taken=0.0;
		cookie=2.0;
		less=false;
		
		int t=0;
		t_min=0;
		
		while(t<10000){

			if(x<=c){
				t_taken=x/cookie;
				t_min=t_taken;
				less=true;
				break;
			}

			if(t_taken+(x/cookie) <= (t_taken+(c/cookie) + (x/(cookie+f)))){
				t_taken+=x/cookie;

				if(t_min<t_taken)
					t_min=t_taken;
				break;
			}

			t_taken= t_taken+(c/cookie);
			cookie=cookie+f;
		}

		fout<<"Case #"<<i+1<<": "<<setprecision(10)<<t_min<<endl;

	}
	
	return 0;
}