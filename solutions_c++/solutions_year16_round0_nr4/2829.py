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


string flip(string s){
	int k = s.length();
	 reverse(s.begin(),s.end());
	 for(int i=0;i<k;i++){
	 	if(s[i]=='+'){
	 		s[i]='-';
	 	}else{
	 		s[i] = '+';
	 	}
	 }
	 
	 return s;
}


int main(int argc, char const *argv[])
{
	/* code */
	int cases,count =0,flag,pos,k=0,c,s;
	
	ifstream infile;
	
	infile.open("ds.in");
	infile>>cases;
	ofstream outfile;
   outfile.open("out.txt");
	for(int j=1;j<=cases;j++){
		count =0,pos=0;
		flag=0;
		infile>>k>>c>>s;
		if(c==1){
			if(k==1){
				outfile<<"Case #"<<j<<": ";
				outfile<<1<<endl;
			}
			else if(s==k){
				outfile<<"Case #"<<j<<": ";
				for(int i=1;i<=k;i++){
					outfile<<i<<" ";
				}
				outfile<<endl;
			}else if(s<k){
				outfile<<"Case #"<<j<<": ";
				outfile<<"IMPOSSIBLE"<<endl;
			}
		}else if(c>1){
			if(s<k-1){
				outfile<<"Case #"<<j<<": ";
				outfile<<"IMPOSSIBLE"<<endl;
			}else if(k==1){
				outfile<<"Case #"<<j<<": ";
				outfile<<1<<endl;
			}else if(s>=k-1){
				outfile<<"Case #"<<j<<": ";
				for(int i=2;i<=k;i++){
					outfile<<i<<" ";
				}
				outfile<<endl;
			}
		}
		
		}
	outfile.close();
	return 0;
}


