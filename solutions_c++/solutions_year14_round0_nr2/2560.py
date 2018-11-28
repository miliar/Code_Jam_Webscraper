#include<iostream>
#include<conio.h>
#include<string>
#include<fstream>
#include<algorithm>
#include <iomanip>
using namespace std;
int main(){
	std::ios_base::sync_with_stdio(false);
	ifstream fin("B-large.in");
	ofstream fout("sum.txt");
	int T;
	fin>>T;
	long double b[100];
	for(int l=0;l<T;l++){
		long double c, f, x ;
		fin>>c>>f>>x;
		long double k=x/c;
		int i=ceil(k-1-2/f);
		long double sum=0;
		int j;
		for(j=0;j<i;j++)
			sum+=(long double)c/(2+j*f);
		sum+=(long double)x/(2+(j*f));
		b[l]=sum;
	}
	fout.setf(ios::fixed, ios::floatfield );
	fout.precision(7);
	for(int l=0;l<T;l++){
		fout<<"Case #"<<l+1<<": ";
		fout<<b[l];
		fout<<endl;
	}
}