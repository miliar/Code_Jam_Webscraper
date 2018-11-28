#include <iostream>
#include <fstream>
#include <vector>
#include <math.h>

using namespace std;

int main(){
	//ifstream fin("test.in");
	ofstream fout("test.out");
	int N=32;
	int J=500;
	fout << "Case #1:" << endl;
	int D=(N/2)-2;
	for (int i=0;i<J;i++)
	{
		int temp=i;
		vector<int> dig(D);
		for(int j=0; j<D; j++){
			dig[j]=temp%2;
			temp=temp/2;
		}
		fout << "1";
		for(int j=0; j<D; j++){
			fout << dig[D-j-1];
		}
		fout << "1";
		fout << "1";
		for(int j=0; j<D; j++){
			fout << dig[D-j-1];
		}
		fout << "1";
		for (double k=2;k<11;k++){
			long long factor=1+pow(k,D+1);
			for(double j=0; j<D; j++){
				factor+=dig[j]*pow(k,j+1);
			}
			fout << " " << factor;
		}
		fout << endl;
	}
}