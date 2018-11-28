/*
 * mag.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: dhiraj
 */
#include <iostream>
#include<fstream>
#include<stdio.h>
using namespace std;
int main(int argc,char*argv[]){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int t,ans1,ans2;
	fin>>t;

	int a[16],b[16];
	for(int i=1;i<(t+1);i++){
		fin>>ans1;
		for(int j=0;j<16;j++){
			fin>>a[j];
		}
		fin>>ans2;

		for(int j=0;j<16;j++){
			fin>>b[j];
		}
		int count=0,ans=0;

		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(a[(ans1-1)*4+j]==b[(ans2-1)*4+k]){
					count++;
					ans=a[(ans1-1)*4+j];

				}
			}
		}
		if(count==1){
			fout<<"Case #"<<i<<": "<<ans<<"\n";
		}
		else if(count>1){
			fout<<"Case #"<<i<<": Bad Magician!\n";
		}
		else{
			fout<<"Case #"<<i<<": Volunteer Cheated!\n";
		}



	}
}






