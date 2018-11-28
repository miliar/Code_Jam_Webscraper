#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
	ifstream ifile;ofstream ofile;ifile.open("magician.in");ofile.open("magician.txt");
	int cases,arr1[4][4],arr2[4][4],row1,row2,rep[4],chk1[4],chk2[4],ele,ind;
	ifile>>cases;
	for(int a=0;a<cases;a++){
		for(int b=0;b<4;b++){rep[b]=0;}
		ele=ind=0;
		ifile>>row1;
		for(int b=0;b<4;b++){
			for(int c=0;c<4;c++){
				ifile>>arr1[b][c];}}
		for(int b=0;b<4;b++){chk1[b]=arr1[row1-1][b];}
		ifile>>row2;
		for(int b=0;b<4;b++){
			for(int c=0;c<4;c++){
				ifile>>arr2[b][c];}}
		for(int b=0;b<4;b++){chk2[b]=arr2[row2-1][b];}
		for(int b=0;b<4;b++){
			for(int c=0;c<4;c++){
				if(chk1[b]==chk2[c])
				{	rep[b]++;ind=b;}
			}}
		for(int b=0;b<4;b++){if(rep[b]>0){ele++;}}
		ofile<<"Case #"<<a+1<<": ";
		if(ele==0)
			ofile<<"Volunteer cheated!";
		if(ele>1)
			ofile<<"Bad magician!";
		if(ele==1)
			ofile<<arr1[row1-1][ind];
		ofile<<endl;
	}
	return 0;
}