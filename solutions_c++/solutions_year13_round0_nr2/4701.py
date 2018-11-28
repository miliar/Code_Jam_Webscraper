#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream fin("test.in");
	ofstream fout("test.out");

	int testC;
	int X,Y, feld[100][100], maxX[100], maxY[100];
	int test,x,y;
	bool possib;

	fin>>testC;

	for(test=0;test<testC;++test){
		fout<<"Case #"<<test+1<<": ";
		fin>>X>>Y;
		for(x=0;x<X;++x)
			for(y=0;y<Y;++y)
				fin>>feld[x][y];
		for(x=0;x<X;++x)
			maxX[x]=-1;
		for(y=0;y<Y;++y)
			maxY[y]=-1;
		for(x=0;x<X;++x)
			for(y=0;y<Y;++y){
				maxX[x]=max(maxX[x],feld[x][y]);
				maxY[y]=max(maxY[y],feld[x][y]);
			}
		possib=true;
		for(x=0;x<X&&possib;++x)
			for(y=0;y<Y&&possib;++y)
				if(feld[x][y]<min(maxX[x],maxY[y])){
					possib=false;
					fout<<"NO"<<endl;
				}
		if(possib)
			fout<<"YES"<<endl;
	}
	
	return 0;
}