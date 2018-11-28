/*
ID: Nadim_Ul_Abrar
PROG:
LANG: C++
*/

#include <iostream>
#include <fstream>
#include <iomanip>
#define ll long long

using namespace std;

int main ()
{
	ofstream fout ("BB.out");
    ifstream fin ("B.in");
    int T,c=1;
    fin>>T;
	double r,X,C,F,ans;
    while (T--){
    	ans=0,r=2;
    	fin>>C>>F>>X;
	    if (X<=C){
   		 	ans+=(X/r);
    	}
    	else{
    		while (C/r+X/(r+F)<X/r){
    			ans+=C/r;
    			r+=F;
    		}
    		ans+=(X/r);
    	}
    	fout<<"Case #"<<c++<<": "<<fixed<<setprecision(7)<<ans<<endl;
    }
    return 0;
}
