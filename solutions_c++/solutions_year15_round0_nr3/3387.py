#include<iostream>
#include<fstream>
using namespace std;

int arr[4][4]={{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};
int ar[100000];

int multiply(int a,int b){
	if(a<0 && b<0) return multiply(-1*a,-1*b);
	else if(a<0) return -1*(multiply(-1*a,b));
	else if(b<0) return -1*(multiply(a,-1*b));
	else return arr[a-1][b-1];
}


int main(){
	ifstream infile;
	ofstream myfile;
	myfile.open("b.txt");
	infile.open ("C-small-attempt1.in");;
	int t,j,c,i,l,v=0,val,x,flagi,flagk;
	string s,str;

	infile>>t;
	for(i=0;i<t;i++){
		infile>>l;
		infile>>x;
		infile>>s;
		str="";
		for(j=0;j<x;j++){
			str.append(s);
		}
		l=l*x;
		val=1;
		for(j=0;j<l;j++){
			if(str[j]=='i')
			ar[j]=2;
			if(str[j]=='j')
			ar[j]=3;
			if(str[j]=='k')
			ar[j]=4;
		}
		flagi=0;flagk=0;
		for(j=0;j<l;j++){
			val=multiply(val,ar[j]);
			if(val==2)flagi=1;
			if(val==4 && flagi==1)flagk=1;
		}
		if(val==-1 && flagi==1 && flagk==1)
			myfile<<"Case #"<<i+1<<": YES"<<"\n";
		else
			myfile<<"Case #"<<i+1<<": NO"<<"\n";
	}
	myfile.close();
	return 0;
}
