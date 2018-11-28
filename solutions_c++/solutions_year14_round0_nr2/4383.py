#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>


using namespace std;

double time2shop( double c, double acc ){
	return c/acc; 
}

double time2collect( double x, double acc ){
	return x/acc;
}



int main(int argc, char* argv[])
{
	ifstream fin ("B-large.in");
	//ifstream fin ("test");
	ofstream fout ("output.out");

	int cases;
	fin >> cases;

	cout<<cases;

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";

		double c, f, x;
		fin>>c;
		fin>>f;
		fin>>x;

		double acc = 2;

		double time = 0;

		double toShop, toAcc, toAcc2;
		while(true){
			toShop = time2shop(c, acc);
			toAcc = time2collect(x, acc);
			toAcc2 = time2collect(x, acc+f);

			if(toAcc < toShop + toAcc2){
				//not worth shopping
				time += toAcc;
				break;

			} else {
				time += toShop;
				acc += f;
			}

		}
		fout<<fixed <<setprecision(8)<<time;

		fout<<endl;		
	}

	fin.close();
	fout.close();


	return 0;
}

