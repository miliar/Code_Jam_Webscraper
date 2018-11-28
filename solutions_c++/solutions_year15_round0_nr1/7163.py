#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <cstring>
using namespace std;

#define rep(i,n)    for(int i=0; i<(n); ++i)
#define forn(i,a,b)  for(int i=(a); i<=(b); ++i)
#define lli long long int
int main() {
   
    ifstream in;
    in.open("A-large.in");
    
    ofstream out;
    out.open("output.txt");
    
    
    
	int tt;
	in>>tt;
	int s;
	string str;
	for(int x=1;x<=tt;x++)
	{
		in>>s;
		in>>str;
		int a[s+1];
		for(int j=0;j<s+1;j++)
		{
			a[j]= str[j]-48;
		}
		int sum=0;
		sum+=a[0];
		
		int room=0;
		int start=1;
		goback:
		for(int j=start;j<s+1;j++)
		{
			if(sum>=j)
			{	
				sum+=a[j];
			}
			else
			{
				start=j;
				room++;
				sum+=1;
				goto goback;	
			}
			
		}	
		out<<"Case #"<<x<<": "<<room<<endl;
		
	}



    return 0;
}