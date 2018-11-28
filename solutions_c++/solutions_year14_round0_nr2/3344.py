#include<fstream>
#include<iomanip>
using namespace std;

int main(int argc,char *argv[])
{
ifstream fin(argv[1]);
ofstream fout("output.txt");
	int t;
	fin>>t;
	for(int i=1;i<=t;i++){
	fout<<"Case #"<<i<<": ";
			long double C,F,X;
			fin>>C>>F>>X;
			long double rate=2.0;
			long double lastAns=(X/rate),time=0,curAns;
			while(1){
				time = time + (C/rate);
				rate= rate + F;
				curAns=time+(X/rate);
				if(curAns>lastAns)break;
				else lastAns=curAns;
			}
			fout<<std::setprecision(20)<<lastAns<<endl;
	}
fin.close();
fout.close();
return 0;
}


