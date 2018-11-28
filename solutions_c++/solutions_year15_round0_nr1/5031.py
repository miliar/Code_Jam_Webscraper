#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream infile;
	ofstream myfile;
	myfile.open("b.txt");
	infile.open ("A-large.in");;
	int t,j,c,i,l,v=0,val;
	string s;
	int a[10000];
	infile>>t;
	for(i=0;i<t;i++){
		infile>>val;
		infile>>s;
		l=val+1;
		for(j=0;j<l;j++){
			a[j]=s[j]-48;
		}
		if(val==0) c=0;
		else v=a[0];
		c=0;
		for(j=1;j<l;j++){
			//cout<<"aa";
			//cout<<c<<" "<<v<<" "<<j<<"\n";
			if(v>=j)v=v+a[j];
			else {
				c=c+j-v;
				v=v+a[j]+j-v;
			}
		}
		myfile<<"Case #"<<i+1<<": "<<c<<"\n";
	}
	return 0;
}