#include<iostream>
#include<cmath>
#include"BigIntegerLibrary.hh"
#include <iomanip>
#include <locale>
#include <sstream>
#include <string>
#include <fstream> 
using namespace std;
BigInteger isSquare(BigInteger n){
	if (n==1) return 1;	
	BigInteger i=0;	
	for(i=0;i<n;i++) if(i*i == n) break;
	if (i==n) return -1;
	else return i;
}
/*bool isPalind(BigInteger x){
	BigInteger tmp=0;
	BigInteger n=x;
	while(n>0){
		tmp = (tmp*10) + (n%10);
		n= n/10;
	}
	if (tmp==x) return true;
	else return false;}
*/
bool isPalind(string x){
	unsigned int i=0;

	for(i=0;i<x.length();i++) if (x[i] != x[x.length()-i-1]) break;
	if (i==x.length()) return true;
	else return false;
	}

int main()
{	
	ofstream filer("out.txt");
	ifstream fileio("C-small-attempt0.in");
	unsigned int t;
	string line;
	fileio >>t;
	// while (getline(file,line))
		    {	
			
			//istringstream ss(line);
			//ss >>t;
			string x1,y1;
			BigInteger x,y;
			for (unsigned int m=0;m<t;m++)
			{
			fileio>>x1>>y1;
			//ss >> x1>>y1;
			x= stringToBigInteger(x1);
			y= stringToBigInteger(y1);
			BigInteger l=0;
			for(BigInteger z = x; z<=y; z++){
				if ( 	 isPalind(bigIntegerToString(z)) && 	isPalind(	bigIntegerToString(isSquare(z) )	 ) 	) l++;
							}				
	
			filer<<"Case #"<<(m+1) <<": "<< l<<"\n";}
	

		}fileio.close();
	
	filer.close();
	return 0;
}
