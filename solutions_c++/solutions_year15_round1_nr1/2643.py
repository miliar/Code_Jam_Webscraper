//============================================================================
// Name        : HairCut.cpp
// Author      : Yao Zhang
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream infile("input.txt");
	ofstream SaveFile("output.txt");
	if (infile.is_open()){
		long long total;
		infile>>total;
		for(long long i=0;i<total;i++){
			long long num;
			long long ans1 = 0;
			long long ans2 = 0;
			infile>>num;
			long long *bar = new long long[num];
			for(long long j=0;j<num; j++){
				infile >> bar[j];
			}
			for(long long j=num-1; j>0; j--){
				if(bar[j-1]>bar[j])
					ans1 += bar[j-1]- bar[j];
			}

			long long max =0;
			long long *rat = new long long[num-1];
			for(long long m=0;m<num-1;m++){
				rat[m] = bar[m] - bar[m+1];
				if(max<rat[m])
					max = rat[m];
			}
			rat[num -2] = bar[num-2] - bar[num-1];
			if(max<rat[num-2])
				max = rat[num-2];
	//		cout<<"max="<<max<<endl;
			for(long long m=0; m<num-1;m++){
				if(bar[m]<max)
					ans2+= bar[m];
				else
					ans2 +=max;
			}
			//ans2 +=bar[num-2] - bar[num-1];



			SaveFile<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2<<endl;
			delete[] bar;
		}
		infile.close();
		SaveFile.close();
	}
}
