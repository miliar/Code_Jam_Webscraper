#include<iostream>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>
#include<iomanip>
#include<algorithm> 
#include<string>
#include<vector>
using namespace std;


int main(){
    int inc=1;
	ifstream file("i1.in");
	ofstream file2("o1.txt",ios::trunc);
	int t;   file>>t;
	
	int s; string str; long ar[1004];
	for(int x=1;x<=t;x++){
		file2<<"Case #"<<inc++<<": ";
		
		long count=0;
		file>>s; file>>str;
		for(int i=0;i<=s;i++){
			ar[i]=str[i]-'0';
		}
		
		for(int i=1;i<=s;i++){
			if(ar[i-1]<i){
				count+= i-ar[i-1];
				ar[i-1]=i;
			}
			ar[i]+=ar[i-1];
		}
		
	    
		file2<<count;
		
		file2<<endl;
	}
}
