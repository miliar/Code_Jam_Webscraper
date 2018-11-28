#include<iostream>
#include<fstream>
#include<string>
#include <sstream>
using namespace std;
int myfunc(string *tic){
	int count=0;
	int count2=0;
	int count3=0;
	int count4=0;
	int count5=0;
	int count6=0;
	int count7=0;
	int count8=0;
	int count9=0;

	for(int i=0;i<4 ;i++){
		for(int j=0;j<4;j++){
		if(tic[i][j]=='X'||tic[i][j]=='T')
			count++;
		if(tic[i][j]=='O'||tic[i][j]=='T')
			count2++;
		if(tic[j][i]=='X'||tic[j][i]=='T')
			count3++;
		if(tic[j][i]=='O'||tic[j][i]=='T')
			count4++;
		if(tic[j][j]=='X'||tic[j][j]=='T')
			count5++;
		if(tic[j][3-j]=='X'||tic[j][3-j]=='T')
			count8++;
		if(tic[j][3-j]=='O'||tic[j][3-j]=='T')
			count9++;
		if(tic[j][j]=='O'||tic[j][j]=='T')
			count6++;
		if(tic[i][j]=='O'||tic[i][j]=='T'||tic[i][j]=='X')
			count7++;
		}
		if(count==4||count3==4||count5==4||count8==4)
			return 1;
		else if(count2==4||count4==4||count6==4||count9==4)
			return 2;
		else if(count7==16)
			return 3;
		count=0;count2=0;count3=0;count4=0;count5=0;count6=0;count8=0;count9=0;

	}
	return 4;



}
int main (){

	fstream myfile;
	ofstream out;
	string number;
	myfile.open("input.txt");
	out.open("output.txt");
	if(myfile.is_open()){
		getline(myfile,number);
		int numb;
		stringstream a(number);
		a >> numb;
		for(int i=0;i<numb;i++){
			string a[4];
			for(int k=0;k<4;k++)
			getline(myfile,a[k]);
			int res=myfunc(a);
			if(res==1)
				out << "Case #"<<i+1<<": X won\n";
			else if(res==3)
				out << "Case #"<<i+1<<": Draw\n";
			else if(res==2)
				out << "Case #"<<i+1<<": O won\n";
			else if(res==4)
				out << "Case #"<<i+1<<": Game has not completed\n";
			getline(myfile,number);


		}

		out.close();
	}
}