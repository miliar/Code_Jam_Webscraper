#include <stdio.h>
#include <fstream>
#include <string>
#include <iostream>
using namespace std;


int findplus(char ii[],int &cp,bool &ok,int length){if(cp==length) {return cp;}

                            if(ii[cp]=='+')
                                {cp++;findplus(ii,cp,ok,length);}
                             else { ok=true; if(ii[cp+1]=='+'||cp+1==length) return cp; else {cp++; findplus(ii,cp,ok,length);}}}


int findminus(char ii[],int &cp,bool &ok,int length){if(cp==length ) return cp;

                            if(ii[cp]=='-')
                                {cp++;findminus(ii,cp,ok,length);}
                             else { ok=true; if(ii[cp+1]=='-'||cp+1==length) return cp; else {cp++; findminus(ii,cp,ok,length);}}}



 int main () { char ii[150]; int cp=0; int total; bool ok=false; int cc=0; string s;
	ifstream f("io.txt"); ofstream ff; ff.open("ot.txt");
	f>>cc;  getline(f,s);
	for(int k=1; k<cc+1; k++) { int length=0; string str; cp=0; total=0; ok=false;
				 getline(f,str);
				 length=str.length();
				for(int i=0; i<str.length(); i++){
					ii[i]=str.at(i); } //cout<<length;

				while(ii[length-1]=='+') {length--;} if (length==0) {ff<<"Case #"<<k<<": "<<total<<endl; continue;}

				while(1){ok=false;
				if (ii[0]=='+') {findplus(ii,cp,ok,length);

                if(cp>0) { if(ok==false) break; total+=2;  for(int i=0; i<cp+1; i++){ ii[i]='+';} cp=0;}}

                if(ii[0]=='-') { findminus(ii,cp,ok,length);

                 if(cp>0) { total++; for(int i=0; i<cp+1; i++){ ii[i]='+';} cp=0; if(ok==false) { break;}  }}

                 // cout<<ii[0];
                 }



				ff<<"Case #"<<k<<": "<<total<<endl;}
	return 0;}
