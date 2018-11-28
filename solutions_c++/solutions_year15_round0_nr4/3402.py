#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <list>
#include <complex>
#include <queue>
using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    int t,i,x,r,c,res;
    cin>>t;
    for(i=1;i<=t;i++){
    	cin>>x>>r>>c;
    	res=0;
    	if(x==1)
    	{
    		res=1;
		}
		else if(x==2){
			if( (r*c) %2==0)
				res=1;
		}
		else if(x==3){
			if(r>=2 && c>=2 && ((r*c) %3==0) ){
				res=1;
			}
		}
		else{
			if(r*c==12 || r*c==16)
				res=1;
		}
    	cout<<"Case #"<<i<<": "<<(res?"GABRIEL":"RICHARD")<<endl;
	}
	return 0;
}
