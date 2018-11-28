#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <functional>
#include <set>
#include <sstream>
#include <map>
#include <queue>
#include <stack>

using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int t=1;t<=T;t++){

		int x,r,c;
		cin>>x>>r>>c;

		string res;
		const string G="GABRIEL";
		const string R="RICHARD";

		if(x==1) res=G;
		if(x==2){
			if((r*c)%2) res=R;
			else res=G;
		}
		if(x==3){
			if((r*c)==6 || (r*c)==9 || (r*c)==12) res=G;
			else res=R;
		}
		if(x==4){
			if((r*c)==12 || (r*c)==16) res=G;
			else res=R;
		}
		printf("Case #%d: %s\n",t,res.c_str());


	}

	return 0;
}