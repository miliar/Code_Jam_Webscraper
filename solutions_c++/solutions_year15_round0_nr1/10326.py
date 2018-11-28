#include <iostream>
#include <fstream>
#include <cstdlib>
#include <conio.h>
#include <string.h>
#include <stdio.h>
using namespace std;
int sum (int*, int);
int char2int (char);
int main(){
    ifstream IN("A-small-attempt0.in");
    ofstream OUT("output.txt");
    string str;
    getline(IN,str);
    int T = atoi(str.c_str());
    
    for(int i=0; i<T; i++) {
    	int Smax,needed=0;
		getline(IN, str);
		Smax = char2int(str[0]);
		int* L = new int[Smax+1]; //Shyness Levels
		for(int j=0; j<Smax+1; j++) {
				L[j] = char2int(str[j+2]);
		}
		for(int j=0; j<Smax+1; j++) {
			if(j >= sum(L,j+1) + needed)
				 needed++;
		}
		OUT <<"Case #"<<i+1<<": "<<needed<<"\n";           
    }
	cout << ".. done!";    
    getch();
    return 0;    
}
int sum (int* L, int len){
	int s=0;
	for (int i=0; i<len; i++)
		s+=L[i];
	return s;
}
int char2int (char c){
	if (c>='0' && c<='9')
	    return int(c-'0');
	else
		cout<<"char2int: invalid conversion: "<<c<<"\n";	
}
