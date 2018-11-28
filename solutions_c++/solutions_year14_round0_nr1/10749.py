#include <iostream>
#include <algorithm>
#include <vector>
#include<fstream>
using namespace std;
int main()
{
  int T,i,j,k;
  int a[4];
  int b[4];
  int rowa, rowb;
  int temp,num;
  ifstream input;
  ofstream output;
  input.open("A-small-attempt0.in");
  output.open("aout.txt");
  input >> T;
  for(i=0;i<T;i++){
	input >> rowa;
//	cout << rowa;
	rowa=rowa-1;
	for(j=0;j<16;j++){
		input >> temp;
		if( rowa*4 <=j && (rowa+1)*4 > j)
			a[j-rowa*4]=temp;
	}
	input >> rowb;
	//cout << rowb;	
	rowb=rowb-1;
	for(j=0;j<16;j++){
		input >> temp;
		if( rowb*4 <=j && (rowb+1)*4 > j)
			b[j-rowb*4]=temp;
	}
//	for(j=0;j<4;j++)
//		cout << a[j];
//	cout << endl;
	temp=0;
	for(j=0;j<4;j++)
		for(k=0;k<4;k++)
			if(a[j]==b[k]){
					temp++;
					num = a[j];
			}
	output << "Case #"<< i+1 <<": ";
	if(temp==1)
		output << num;
	if(temp ==0)
		output << "Volunteer cheated!";
	if(temp >1)
		output << "Bad magician!";
	output << endl;
  }
  return 0;
}
