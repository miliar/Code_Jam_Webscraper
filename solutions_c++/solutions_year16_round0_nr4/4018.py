#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string>

using namespace std;


int main() {
    int t,k,c,s;
	cin>> t;
	for(int i=1; i<=t; i++)
	{
		long long int pos;
		
		cin >>k>>c>>s; 
		cout << "Case #" << i << ":";
		//for small input, k=s, so just checking all positions from 1 to k should do the trick
		for(int j=1; j<=k; j++)
		{
			cout<<" "<<j;
		}		
		cout<< endl;
	}
	return 0;
}
