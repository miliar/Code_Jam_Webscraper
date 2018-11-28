#include <iostream>
#include <string>
#include <fstream>
#define N 4
using namespace std;

int main()
{
	int testn; 
	int ii,j,k;	
	int r1, r2, arr1[N][N]={0}, arr2[N][N]={0};
	int store1[N] ={0}, store2[N] = {0};	
	ifstream readfile ;
	readfile.open("A-small-attempt1.in");
	readfile >> testn;
	//cin >> testn;
	int* nm = new int[testn];
	int* val = new int[testn];
	ofstream myfile;
	myfile.open ("q1.txt");
	
	for(ii=0; ii<testn; ii++)
	{
		nm[ii] =0;
		readfile >> r1;
		for(j=0;j<N;j++) {
			for(k=0;k<N;k++)
				readfile >> arr1[j][k];			
		}
		
		for(j=0;j<N;j++) {
			store1[j] = arr1[r1-1][j];
			
		}

		readfile >> r2;
		for(j=0;j<N;j++) {
			for(k=0;k<N;k++)
				readfile >> arr2[j][k];
			
		}
		for(j=0;j<N;j++)
			store2[j] = arr2[r2-1][j];


		for(j=0;j<N;j++) {
			for(k=0;k<N;k++) {
				if(store1[j] == store2[k])
				{
					nm[ii]++ ;
					val[ii] = store1[j];
				}
			}
		}	
		//cout << "nm: " << nm[ii] << endl;
		
	}

	for(ii=0;ii<testn;ii++)
	{
		if(nm[ii] == 0)
			myfile << "Case #" << ii+1 << ": Volunteer cheated!" << endl;
		else if(nm[ii] == 1)
			myfile << "Case #" << ii+1 << ": " << val[ii] << endl;
		else myfile << "Case #" << ii+1 << ": Bad magician!" << endl;
	}
	myfile.close();
	return(0);
}
