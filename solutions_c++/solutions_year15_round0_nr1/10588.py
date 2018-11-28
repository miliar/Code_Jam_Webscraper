#include <fstream>
#include<conio.h>
#include<iostream>
#include<string>

using namespace std;
int main(){
	long int a; int n,q; string b;
	long int i,j, n_aud, additional_aud;

	ofstream outfile;
	outfile.open("A-small.out");

	ifstream infile;
	//infile.open("A-small-practice.in");
	infile.open("A-small-attempt1.in");
	infile>>n;
	for(i=1;i<=n;i++){
		additional_aud=0;
		n_aud=0;
		infile>>a;
		getline(infile, b);
		//cout<<a<<b<<endl;

		for (j=0; j<=a;j++){
			//shy level j
			//number of audience with j shy level b[j+1]
			q=b[j+1]-'0';
			//cout<<q<<"    ";
			if(j==0)n_aud=n_aud+q;
			else if(q!=0) {
				if (n_aud>=j){
					n_aud=n_aud+q;
				}else{
					additional_aud=additional_aud+(j-n_aud);
					n_aud=n_aud+q+additional_aud;
				}
			}
		}

		//cout<<"Case #"<<i<<": "<<additional_aud<<endl;
		outfile<<"Case #"<<i<<": "<<additional_aud<<endl;
	
	}

	getch();
	return 0;
}
