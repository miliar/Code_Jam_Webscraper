#include <iostream>
#include <fstream>
#include <algorithm>
#include <math.h>

using namespace std;

int checknum(int N){
	bool digits[10];
	for (int i=0; i<10;i++) digits[i]=false;
	for (int i=1;i<100;i++)
	{
		int temp=N*i;
		while(temp>0){
			digits[temp%10]=true;
			temp=temp/10;
		}
		bool check=true;
		for (int j=0; j<10;j++){
			if(digits[j]==false){
				check=false;
				j=10;
			}
		}
		if(check){
			return i;
		}
	}
	return -1;
}

int main(){
	
	ifstream fin("test.in");
	ofstream fout("test.out");
	int N;
	fin >> N;
	for(int i=1; i<N+1;i++){
		int temp;
		fin >> temp;
		fout << "Case #" << i << ": ";
		int x=checknum(temp);
		if(x==-1) fout << "INSOMNIA" << endl;
		else fout << x*temp << endl;
	}
	system("pause");
}