#include<iostream>
#include<fstream>
#include<string>

using namespace std; 

int main()
{
cout<<"Enter file name";
string file;
cin>>file;

ifstream infile;
infile.open(file);

int N;

infile>>N;

ofstream out;
out.open("output.txt");
for(int i=0;i<N;i++){


	char A[1200];
	infile>>A;
	cout<<A;
	char B[1200];
	B[0]=A[0];
	if(A[1]=='\0')
		B[1]='\0';
	else {
	for(int j=1;A[j]!='\0';j++){
		
		if(A[j]>=B[0])
		{
			string a = B;
			a=A[j]+a;
			//cout<<a<<endl;
			strcpy (B, a.c_str());

		}
		else {
			B[j]=A[j];
		}
		B[j+1]='\0';

	}
}
	out<<"Case #"<<i+1<<": "<<B<<endl;

}
/*

*/
}