#include <iostream>
#include <fstream>

using namespace std;


void main (){


	fstream fin;
	fstream fout;

	fin.open("input.in",ios::in | ios::binary);
	fout.open("out.txt",ios::out | ios::trunc);

	long long int n = 0;
	long long int r , t;

	long long int temp;
	long long int count;

	fin>>n;

	for (int m = 0 ; m < n ; m++){
	
		fin>>r;
		fin>>t;

		count = 0;
		
		while (1){
			
			temp = 2*r+1;

			if (temp  > t){
			
				break;

			}

			t = t - temp;
			r = r+2;
			count++;
			
		}


		fout<<"Case #"<<m+1<<": "<<count<<endl;

	}

		

	fin.close();
	fout.close();

	

}