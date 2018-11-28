#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<cmath>
#include<climits>
#include <fstream>
 
using namespace std;
#include <sstream>

template <typename T>
  string NumberToString ( T Number )
  {
     ostringstream ss;
     ss << Number;
     return ss.str();
  }

int main(int argc, char const *argv[])
{
	/* code */
	int cases;
	long long n;
	
	int a[10];
	for(int i=0;i<10;i++){
		a[i] =0;
	}
	ifstream infile;
	infile.open("A-large.in");
	infile>>cases;
	ofstream outfile;
   outfile.open("out.txt");
	for(int j=1;j<=cases;j++){
		infile>>n;
		
		long long m=n;
		while(true){
		if(n==0){
			 outfile<<"Case #"<<j<<": INSOMNIA\n";
			break;
		}
		string u =NumberToString(m);
		int k = u.length();
		
		for(int i=0;i<k;i++){
			if(u[i]=='0'){
				if(a[0]==0)
					a[0]=1;
			}else if(u[i]=='1'){
				if(a[1]==0)
					a[1]=1;
			}else if(u[i]=='2'){
				if(a[2]==0)
					a[2]=1;
			}else if(u[i]=='3'){
				if(a[3]==0)
					a[3]=1;
			}else if(u[i]=='4'){
				if(a[4]==0)
					a[4]=1;
			}else if(u[i]=='5'){
				if(a[5]==0)
					a[5]=1;
			}else if(u[i]=='6'){
				if(a[6]==0)
					a[6]=1;
			}else if(u[i]=='7'){
				if(a[7]==0)
					a[7]=1;
			}else if(u[i]=='8'){
				if(a[8]==0)
					a[8]=1;
			}else if(u[i]=='9'){
				if(a[9]==0)
					a[9]=1;
			}

		}

			int sum = 0;
			for(int i=0;i<10;i++){
				sum = sum+a[i];
			}
			
			if(sum==10){
				 outfile<<"Case #"<<j<<": "<<m<<"\n";
				break;
			}else {
				m = m+n; 
			}
		}
	for(int i=0;i<10;i++){
		a[i] =0;
		}
		
	}
	outfile.close();
	return 0;
}
