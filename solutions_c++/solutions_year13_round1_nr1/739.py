#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <fstream>
#include <cstring>
#include <iomanip>
#include <limits.h>
//#include <sys/time.h>
//#include <time.h>

using namespace std;
#define ll long long

int main(void)
{
	int T;
	cin>>T;
	for(int _t=1;_t<=T;++_t){	

		ll r,t;
		cin>>r>>t;

		ll result=0;
		while(1){
			//cout<<t<<endl;
			t-=(r+1)*(r+1)-r*r;	
			if(t<0)break;
			++result;
			r+=2;
		}
		
		cout<<"Case #"<<_t<<": "<<result<<endl;
		cerr<<"cerr:"<<_t<<endl;	
	}
}


//	cout.setf(ios::fixed);

