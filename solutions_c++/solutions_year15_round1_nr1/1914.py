#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream infile;
	ofstream myfile;
	myfile.open("b.txt");
	infile.open ("A-small-attempt0 (1).in");;
	int t,j,c,i,l,v=0,val,r,x,n,p,q,max;
	int a[10003];
	infile>>t;
	for(i=0;i<t;i++){
		infile>>n;
		for(j=0;j<n;j++){
			infile>>a[j];
		}
		p=0;q=0;max=0;
		for(j=0;j<n-1;j++){
			if(a[j]>a[j+1])p=p+a[j]-a[j+1];
		}
		for(j=0;j<n-1;j++){
			if(a[j]>a[j+1] && a[j]-a[j+1]>max)max=a[j]-a[j+1];
		}
		for(j=0;j<n-1;j++){
			if(a[j]<max)q=q+a[j];
			else q=q+max;
		}
			myfile<<"Case #"<<i+1<<": "<<p<<" "<<q<<"\n";
	}
	return 0;
}
