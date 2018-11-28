#include<iostream.h>
#include<fstream>
#include<sstream>
#include<vector>
using namespace std;
int main()
{
	ifstream in("A-small-attempt0(1).in");
	ofstream out("output.txt");
	int Arr1[2][4];
	int nCase;
	in>>nCase;
	int noR;
	string s;
	for(long i=0;i<nCase;i++){
		for(int f=0;f<2;f++){
		in>>noR;
		getline(in,s);
		for(int z=0;z<noR-1;z++){
				getline(in,s);
		}
		for(int z=0;z<4;z++)
		in>>Arr1[f][z];
			getline(in,s);
		for(int z=noR;z<4;z++)
			getline(in,s);
		}
		int a[4]={0};
		for(int z=0;z<4;z++){
			for(int e=0;e<4;e++){
				if(Arr1[0][z]==Arr1[1][e])
					a[z]++;
			}
		}
		int c=0,p=0;
		for(int su=0;su<4;su++){
			if(a[su]==1){
				c++;
				p=su;
				}
		}
		out<<"Case #"<<i+1<<": ";
		if(c==0){
			out<<"Volunteer cheated!";
		}
		else
		if(c==1){
			out<<Arr1[0][p];
		}
		else
		out<<"Bad magician!";
			out<<endl;
	}//nCase
return 0;
}