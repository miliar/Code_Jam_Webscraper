#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
#include <math.h>

using namespace std;

int main()
{	
	long long t,k,c,s;
	cin>>t;
	long long in = 0;
	while(t--){
		in++;
		cin>>k>>c>>s;
		cout<<"Case #"<<in<<":";
		
		if(( s < k-1) || (s == k-1 && c < 2) ){
			cout<<" IMPOSSIBLE"<<endl;
		}
		else{
			int pl = 2;
			if(c==1)
				pl = 1;
			for(long long i=0;i<s;i++){
				if(k == 1){
					cout<<" 1";
					break;
				}
				if(i+pl <= k)
					cout<<" "<<i+pl;
			}
		}
		cout<<endl;
	}
	
	
	return 0;
}