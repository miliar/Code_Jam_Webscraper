#include <stdio.h>
#include <iostream>
#include <fstream>

using namespace std;
void main()
{
 	fstream fin;
	fin.open("problem1.in",ios::in);
	fstream fout;
	fout.open("output1.out",ios::out);
	int testCases=0;
	fin>>testCases;
	
	for(int i=1;i<testCases+1;i++){
	
	int k=0,k2=0;
	fin>>k;
	k=k-1;
	
	int arr[4][4];
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				fin>>arr[x][y];
			
			}
			
		}
	
	
	fin>>k2;
	k2=k2-1;
	
	int arr2[4][4];
		for(int x=0;x<4;x++){
			for(int y=0;y<4;y++){
				fin>>arr2[x][y];
			}
	
		}
	
	int common=0;int answer=-1;
		for(int z=0;z<4;z++){
			for(int y=0;y<4;y++){
				if(arr[k][z]==arr2[k2][y]){
					answer=arr[k][z];
					common++;
				}
			}
		}
		fout<<"case #"<<i<<": ";
		switch (common)
		{
		case 1:
			fout<<answer<<endl;
			break;
			
		case 0:
			fout<<"Volunteer cheated!"<<endl;
			break;
			
		default:
				fout<<"Bad magician!"<<endl;
			break;
		}		
	
	}
}