#include <fstream>
#include <iomanip>
using namespace std;

char filename[30]="B-small-attempt1.in";

int main(int argc, char const *argv[])
{
	ifstream in(filename);
	ofstream out("bb2");

	int casenum;
	in>>casenum;
	

	for(int i=0;i<casenum;i++){
		out<<"Case #"<<i+1<<": ";
		//cout<<"Case #"<<i+1<<": ";
		int a,b,k;
		//c
		in>>a>>b>>k;
		
		int cnt=0;
		for(int j=0;j<a;j++){
			for(int s=0;s<b;s++){
				if((j&s) < k)
					cnt++;
			}
		}
		
		//c
		out<<cnt<<endl;

	}


	return 0;
}