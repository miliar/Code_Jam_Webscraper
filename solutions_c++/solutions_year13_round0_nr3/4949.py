#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <math.h>


using namespace std;

bool pali(int number){
	int num=number, rev=0, digit;
	do{
		digit = num%10;
		rev = (rev*10) + digit;
		num = num/10;
	}while (num!=0);
	return number == rev;
}

int main(int argc, char* argv[])
{
	ifstream fin ("C-small-attempt0.in");
	//ifstream fin ("test");
    ofstream fout ("output.out");

	int cases;
	fin >> cases;

	cout<<cases<<endl;
	
	string buffer;
	//(fin,buffer); //ignore first line

	for(int i=1;i<=cases;i++){
		int min,max;
		int counter=0;

		fout << "Case #"<<i<<": ";

		fin>>min;
		fin>>max;

		int smin=sqrt(min);
		int smax=sqrt(max);

		for(int j=smin;j<=smax;j++)
			if(pali(j)){
				int jj=j*j;
				if(jj>=min && jj<=max && pali(jj))
					counter++; 
				}

		fout<<counter;
		fout<<endl;
	}

	fin.close();
	fout.close();


	return 0;
}

