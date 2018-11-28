#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

long double n, t, a, b;
#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
bool pali (string c)
{
	for(int j=0;j<=(c.size()/2);j++)
			{
				if (c.size()==1)
				{
					return true;
				}
				if(c[j] != c[c.size()-1-j])
					break;
				if(2*j>=c.size()-1)
					return true;
	}
	return false;
}
int main() {
	ifstream myfile;
	myfile.open("input.txt");
	ofstream myfile2;
	myfile2.open("output.txt");
	
	myfile >> n;

	for (int u = 0; u < n; u++) {
		
		int count=0;
		

		myfile >> a >> b;
		
		for(long double i=a; i<=b;i++)
		{
			bool sq=false,pal=false;
			string c=to_string(i);
			pal = pali(c);
			sq=pali(to_string(sqrt(i)));
			
			if(pal && sq)
			{
				count++;
			}
		}
		cout<<"Case #"<<u+1<<": "<< count<<endl;
		myfile2<<"Case #"<<u+1<<": "<< count<<endl;
	}
	system("pause");
}