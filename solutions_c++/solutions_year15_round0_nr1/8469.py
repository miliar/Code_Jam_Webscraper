#include<iostream>
#include<fstream>
#include<cstdlib>
using namespace std;

int toNumber(char x){
	if(x=='0')
		return 0;
	else if(x=='1')
		return 1;
	else if(x=='2')
		return 2;
	else if(x=='3')
		return 3;
	else if(x=='4')
		return 4;
	else if(x=='5')
		return 5;
	else if(x=='6')
		return 6;
	else if(x=='7')
		return 7;
	else if(x=='8')
		return 8;
	else if(x=='9')
		return 9;

return 0;
}
int main(){
	int cases;
	ifstream infile;
	infile.open("A-large.in");
	ofstream outfile;
	outfile.open("output.txt");
	int c=1,maxShy=0;
	infile>>cases;
	while(c<=cases){
		int people=0;
		int count=0;
		infile>>maxShy;
		maxShy++;
		int *list = new int[maxShy];
		string shyString;
		infile>>shyString;
		for(int i=0;i<(int)shyString.length();i++)
			list[i]=toNumber(shyString[i]);

		people+=list[0];
		for(int i=1;i<maxShy;i++){
			while(i>people){
				count++;
				people++;
			}
			people+=list[i];
		}
		outfile<<"Case #"<<c<<": "<<count<<endl;
		c++;
		delete []list;
	}
}