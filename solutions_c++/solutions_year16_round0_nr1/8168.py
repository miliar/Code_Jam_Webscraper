#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream infile ("input.txt");
	ofstream outfile ("output.txt");
	int t;
	infile >> t;
	int i, allnumsum, a, all_num[10], N, M, numdigit, ans;

	for (int k=0; k<t; k++){
		infile >> N;
		M=N;
		allnumsum=0,a=0, numdigit = 0;
		for (int j=0; j<10;j++){
			all_num[j]=0;
		}
		if (N==0){
			outfile << "case #"<<(k+1)<<": INSOMNIA"<<endl;
			continue;
		}
		i=0;

		while(allnumsum!=10){
			i++;
			N=i*M;
			ans = N;

			while (N>0){
				a = N%10;
				all_num[a] = 1;
				N /=10;

			}
			allnumsum=0;
			for (int j=0; j<10;j++){
				allnumsum += all_num[j];
			}
		}
		outfile << "case #"<<(k+1)<<": "<<ans<<endl;
	}
}