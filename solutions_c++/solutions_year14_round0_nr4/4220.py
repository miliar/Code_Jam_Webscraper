#include <cstdio>
#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int higher(float *list, int n){
	int maxPos = 0;
	for(int i = 0; i < n; i++){
		if(list[maxPos] < list[i])
			maxPos = i;
	}
	return maxPos;
}

int smaller(float *list, int n){
	int minPos = 0;
	for(int i = 0; i < n; i++){
		if( list[minPos] > list[i] )
			minPos = i;
	}
	return minPos;
}


int smallerHigher(float *list, int n, float val){
	int minPos = 0;
	int ii=0;
	for( ii = 0; ii < n; ii++){
		if( list[ii] > val ){
			minPos = ii;
			break;
		}
	}
	for(int i = minPos; i < n; i++){
		if( list[i]>val && list[minPos] > list[i] )
			minPos = i;
	}

	if(list[minPos] < val || list[minPos] == 2)
		return n;
	return minPos;
}

int main(int argc, char* argv[])
{
	ifstream fin ("D-large.in");
	//ifstream fin ("test");
	ofstream fout ("output.out");

	int cases;
	fin >> cases;

	cout<<cases;

	for(int i=1;i<=cases;i++){
		fout << "Case #"<<i<<": ";
		//cout<<"#######################"<<endl;
		int n;
		fin>>n;
		
		float *naomi = new float[n];
		float *ken = new float[n];
		float *naomi2 = new float[n];
		float *ken2 = new float[n];

		for(int j = 0; j<n; j++){
			fin>>naomi[j];
			naomi2[j]=naomi[j];
		}
		for(int j = 0; j<n; j++){
			fin>>ken[j];
			ken2[j]=ken[j];
		}

		int pnaomi; //pick naomi
		int pken; //pick ken

		int wins = 0;
		int trueWins = 0;

		//War
		for( int a = 0; a<n; a++){
			pnaomi = smaller(naomi2, n);
			//cout<<naomi2[pnaomi]<<" ";
			pken = smallerHigher(ken2, n, naomi2[pnaomi]);
			//cout<<"@ "<<ken2[pken]<<" "<<pken<<"@ ";
			
			if( pken == n ){
				pken = smaller(ken2,n);
			//	cout<<ken2[pken]<< "W"<<endl;
				trueWins++;
			}

			
			naomi2[pnaomi] = 2;
			ken2[pken] = 2;	
		}

		for(int turn = 0; turn < n; turn++ ){

			pken = higher(ken, n);
			pnaomi = smallerHigher(naomi, n, ken[pken]);
			
			if(pnaomi<n && naomi[pnaomi] > ken[pken] )
				wins++;
			else{
				//select naomi smallest
				pnaomi = smaller(naomi, n);
			}
			
			naomi[pnaomi] = 2;
			ken[pken] = -1;	
		}
			

		fout<<wins<<" "<<trueWins<<endl;

		delete naomi, ken, naomi2, ken2;		
	}

	fin.close();
	fout.close();


	return 0;
}

