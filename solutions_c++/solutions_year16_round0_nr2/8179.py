#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<fstream>
using namespace std;
typedef long long LL;

main(){
//	FILE *fin = freopen("B-small.in", "r", stdin);
//	assert( fin!=NULL );
//	FILE *fout = freopen("B-small.out", "w", stdout);
    ifstream fin;
	fin.open("B-large-attempt0.in");
    ofstream fout;
	fout.open("B-large.out");
    
	int T,i,total;
	fin>>T;
	string str;
	for(int t=1;t<=T;t++){
	fin>>str;
	total=0;
	
	for(i=1;i<str.length();i++){
	if(str[i]==str[i-1]){
	continue;	
	}	
	else{
	total=total+1;	
	}
	}	
	if(str[i-1]=='-')	
	total=total+1;	
	
	fout << "Case #" << t << ": ";
		fout << total << endl;
	
	
	
	}	
	

exit(0);




}


