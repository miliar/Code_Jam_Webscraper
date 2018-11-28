#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;
ifstream fin ("B-large.in");
ofstream fout ("output.txt");

string stringa;
bool S [100];
int T, lunghezza;

void scambia (int n){
	bool c;
	for (int i=0; i<(n/2)+1; i++){
		c=S[i];
		S[i]=!S[n-i];
		S[n-i]=!c;
		}
	//fout<<"("<<n<<") ";
	//for (int i=0; i<lunghezza; i++) fout<<S[i]<<" ";
	//fout<<"\n";
	return;
	}
	
int quanti (int l){
	if (l==-1) return 0;
	else if (S[l]==1) return quanti (l-1);
	else if (S[0]==0) 
		{
			scambia (l);
			return quanti (l-1)+1;
		}
	else
	{		
			int m=0;
			for (m=0; S[m+1]==1 && m<l-1; m++);
			scambia (m);
			scambia (l);
			return quanti (l-1) + 2;
	}
	}
	
int main(){
	fin>>T;
	
	for (int i=0; i<T; i++){
		fin>>stringa;
		lunghezza=stringa.length();
		for (int j=0; j<lunghezza; j++) {
			if (stringa[j]=='+') S[j]=1;
			else S[j]=0;
			}
		//fout<<"    ";
		//for (int i=0; i<lunghezza; i++) fout<<S[i]<<" ";
		//fout<<"\n";
		fout<<"Case #"<<i+1<<": "<<quanti(lunghezza-1)<<"\n";
		}
	return 0;
	}
