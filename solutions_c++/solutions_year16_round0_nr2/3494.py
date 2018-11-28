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
	int cases,count =0,flag,pos,k=0;
	string n;
	ifstream infile;
	
	infile.open("bl.in");
	infile>>cases;
	ofstream outfile;
   outfile.open("out.txt");
	for(int j=1;j<=cases;j++){
		count =0,pos=0;
		flag=0;
		infile>>n;
		int l = n.length();
		while(true){
			flag=0;
			for(int i=0;i<l;i++){
				if(n[i]=='-'){
					flag =1;
					break;
				}
			}
			if(flag==0){
				outfile<<"Case #"<<j<<": "<<count<<endl;
				break;
			}


			if(n[0]=='+'){
				for(int i=0;i<l;i++){
					if(n[i]=='-'){
						pos = i;
						break;
					}
				}
				n = flip(n.substr(0,pos))+n.substr(pos,l-pos);
				//cout<<n<<endl;
				count++;
			}else{
				for(int i=l-1;i>=0;i--){
					if(n[i]=='-'){
						pos =i;
						break;
					}
				}
				n = flip(n.substr(0,pos+1))+n.substr(pos+1,l-pos-1);
				count++;
			}

		}
		
	}
	outfile.close();
	return 0;
}


