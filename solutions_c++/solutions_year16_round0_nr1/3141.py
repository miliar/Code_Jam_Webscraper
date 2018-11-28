#include <stdio.h>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

 int main(){
			int ii[199];   string s; int cc=1; int n=0;
			ifstream f("io.txt"); ofstream ff; ff.open("ot.txt");
			f>>cc; getline(f,s);

			for(int k=1; k<cc+1; k++) {string t; n=0;
                                      bool one=false,two=false,three=false,four=false,five=false,six=false,seven=false,eight=false,nine=false,zero=false; int s; string str;
									 f>>s; getline(f,t);

                                    if(s==0)  {ff<<"Case #"<<k<<": "<<"INSOMNIA"<<"\n"; continue;}

                           n=s;
                                for(int d=2;1 ;d++){

stringstream ss;
ss << n;
str = ss.str(); //cout<<str;

								for(int i=0; i<str.length();i++){int c;
											c=str.at(i); c-=48;

											if (c==0) zero=true;
											if (c==1) one=true;
											if (c==2) two=true;
											if (c==3) three=true;
											if (c==4) four=true;
											if (c==5) five=true;
											if (c==6) six=true;
											if (c==7) seven=true;
											if (c==8) eight=true;
											if (c==9) nine=true;


											} //cout<<"asd";
										if(zero&&one&&two&&three&four&&five&&six&&seven&&eight&&nine) {ff<<"Case #"<<k<<": "<<n<<"\n"; break;}	 else n=s*d;}



											}

									//ff<<"Case #"<<k<<": "<<fwc<<"\n";
									//cout<<"Case #"<<k<<": "<<fwc<<endl;}
			return 1;}
