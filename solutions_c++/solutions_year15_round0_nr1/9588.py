#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <iostream>
#include <fstream>
using namespace std;

int main(){

	FILE * ifs;
	ofstream ofs("A-large.out");
	int t=0; long result=0;

	ifs = fopen("A-large.in","r");

	fscanf(ifs,"%d",&t);

	for(int tt=1;tt<=t;tt++){

		int maxs=0;

		fscanf(ifs,"%d",&maxs);
		maxs++;

		long current = 0, addtotal=0,add=0, thisround = 0;
		fscanf(ifs,"%1d",&current);
		for(int i=1;i<maxs;i++){
			fscanf(ifs,"%1d",&thisround);
			add = i - current - addtotal;
			current+=thisround;
			if(add>0)addtotal+=add;
		}

		result = addtotal;

		ofs<<"Case #"<<tt<<": "<<result<<endl;
	}

	fclose(ifs);
	ofs.close();
	return 0;

}