#include<iostream>
#include<fstream>
using namespace std;




int main(){

	int t=0;
	int v1,v2;
	int outpt=0;
	int index=0;

//	ifstream fin("A-small-attempt0.in");
	ifstream fin("A-small-attempt0.in");
	ofstream fout("out.txt");

	int arr1[4][4];
	int arr2[4][4];
	int count[4];



	fin>>t;

	for(int loop=0;loop<t;loop++){

		fin>>v1;





		for(int j=0;j<4;j++){

			count[j]=0;    // just ignore its initilizing with 0 //

			for(int k=0;k<4;k++){


				fin>>arr1[j][k];
			}

		}  // end of 2nd loop





		fin>>v2;



		for(int j=0;j<4;j++){

			for(int k=0;k<4;k++){


				fin>>arr2[j][k];
			}

		}  // end of 2nd loop



		--v1;
		--v2;

		int val;

		for(int check=0;check<4;check++){

			val= arr1[v1][check];

			for(int match=0;match<4;match++){

				if(val == arr2[v2][match]){

					count[check]++;
				}
			}




		}



		for(int x=0;x<4;x++){

			if(count[x] > 0){
				outpt++;
				index=x;
			}
		}



		if(outpt==1){

			fout<<"Case #"<<(loop+1)<<": "<<arr1[v1][index]<<endl;
		}else if(outpt == 0){
			fout<<"Case #"<<(loop+1)<<":"<<" Volunteer cheated!"<<endl;
		}else{

			fout<<"Case #"<<(loop+1)<<":"<<" Bad magician!"<<endl;
		}

		outpt=0;
		index=0;

	}




	return 0;



}