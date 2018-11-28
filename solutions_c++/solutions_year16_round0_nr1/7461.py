#include<iostream>
#include<fstream>


using namespace std;

int check(int A[10]);
int main()
{
cout<<"Enter file name";
string file;
cin>>file;

ifstream infile;
infile.open(file);

ofstream out;
out.open("output.txt");



int N;
infile>>N;

int n;

for(int i=0;i<N;i++){

	int a[10]; 

	for(int i=0;i<10;i++)
		a[i]=0;

	infile>>n;

	int b;

	for(int j=1;;j++){
		int c=j*n;
		b=j*n;

		if(c==0){
			break;
		}
		while(c>0){
			a[c%10]=1;
			c=c/10;
		}
		if(check(a))
			break;
	}
	if(b==0)
		out<<"Case #"<<i+1<<": INSOMNIA"<<endl;
	else
		out<<"Case #"<<i+1<<": "<<b<<endl;
}


}

int check(int A[10]){
	int res = 1;
	for(int i=0;i<10;i++)
		if(A[i]==0)
			res=0;

	return res;
}