#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

int main() {
	// your code goes here

	ifstream myfile1;
	ofstream myfile2;
	myfile1.open ("input.txt");
	myfile2.open ("output.txt");

	int numCase;

	myfile1>>numCase;

	for (int i=0; i<numCase; i++){
		myfile2<<"Case #"<<i+1<<": ";

		int numParty;
		myfile1>>numParty;
		bool checker=false;
		double *senator = new double[numParty];
		double sum=0;
		int first;
		int second;

		for (int j=0; j<numParty; j++){
			myfile1>>senator[j];
		}

		for (int k=0; k<numParty; k++) {
			sum=sum+senator[k];
		}
		if (sum!=0){
			while (!checker){
				second=-1;
				if (sum==2) {
					for (int m=0;m<numParty;m++){
						if (senator[m]!=0){
							myfile2<<(char)(m+65);
						}
					}
					sum=0;
				}
				else{
					first=distance(senator, max_element(senator, senator + numParty));
					senator[first]--;
					sum--;
					myfile2<<(char)(first+65);
					if (sum>2){
						for (int l=0; l<numParty; l++) {
							if ((sum/2)<senator[l]){
								senator[l]--;
								second=l;
								myfile2<<(char)(second+65);
							}
						}
						if (second!=-1){
							sum--;
						}
					}
				}
					if (sum==0){
						checker=true;
					}
				myfile2<<" ";
			}
		}
		myfile2<<endl;
		delete [] senator;	
	}

	myfile1.close();
	myfile2.close();



	return 0;
}
