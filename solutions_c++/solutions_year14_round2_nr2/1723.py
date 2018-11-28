/*
ID: Nadim_Ul_Abrar
PROG:
LANG: C++
*/

#include <bits/stdc++.h>
#define ll long long

using namespace std;

int main ()
{
	ofstream fout ("B.out");
    ifstream fin ("B-small-attempt0.in");
    int A,B,C,ans,T,c=1;
    fin>>T;
    while (T--){
    	fin>>A>>B>>C;
    	ans=0;
    	for (int i=0;i<A;i++){
    		for (int j=0;j<B;j++){
    			if ((i&j)<C){
    				ans++;
    			}
    		}
    	}
    	fout<<"Case #"<<c++<<": "<<ans<<endl;
    }
}

