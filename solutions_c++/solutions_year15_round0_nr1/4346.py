#include <vector>
#include <algorithm>
#include <fstream>
#include <stdlib.h> 
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stack>
#include <string.h>
#include <iomanip>
#include <sstream>
#include <map>
#include <set>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
	int i, smax, numCase;
	string s;
	cin>>numCase;
	for(i=0; i<numCase; i++){
		int ans=0;
		cin>>smax;
		cin>>s;
		int numtotal=s[0]-'0';	
		for(int i=1; i<=smax; i++){
			if(i > numtotal){
				ans=ans+i-numtotal;
				numtotal=i+s[i]-'0';
			}
			else{
				numtotal=numtotal+s[i]-'0';
			}
		}
		cout << "Case #" << (i+1) << ": "<<ans<<endl;
	}	
	return 0;
}
