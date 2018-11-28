#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;


int main(){
	ofstream outfile;
	outfile.open("output.txt");
	int mat[4];
	int mat1[4];

	int K;
	scanf("%d",&K);
	cout << K<< endl;

	for (int numcase=1;numcase<=K;numcase++){
		int value;
		int answer;
		int counter=0;
		int resultvalue;
		scanf("%d",&answer);

		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				scanf("%d",&value);
				if(i==answer-1){
					mat[j]=value;
				}
			}
		}

		int answer1;
		scanf("%d",&answer1);
	
		for (int i=0;i<4;i++){
			for (int j=0;j<4;j++){
				scanf("%d",&value);
				int currow=answer1-1;
				if(i==currow){
					for (int k=0;k<4;k++){
						if(value==mat[k]){
							counter++;
							resultvalue=value;
						}

					}
				}
			}
		}

		if(counter>1){
			outfile<<"Case #" <<numcase <<": "<< "Bad magician!" <<endl; 
		}
		if(counter==1){
			outfile<<"Case #" <<numcase <<": "<< resultvalue <<endl; 
		}
		if(counter==0){
			outfile<<"Case #" <<numcase <<": "<< "Volunteer cheated!" <<endl; 
		}

		//outfile<<"Case #" <<numcase <<": "<< numcase <<endl;
	}


	outfile.close();
	return 0;

}