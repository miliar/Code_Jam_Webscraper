#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <string>
#include <vector>
#include <bitset>
#include <fstream>
#include <sstream>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <list>
#include <climits>
#include <assert.h>

//#include <gmpxx.h>

#ifdef _WIN32
#include <time.h>
#else
#include <sys/time.h>
#endif

using namespace std;
#define ll long long

int main()
{
	int T;
	cin>>T;
	for(int _t=0; _t<T; ++_t)
	{
		cerr<<"processing: " << _t+1<<endl;
		int X,R,C;
		cin>>X>>R>>C;

		if(R<C)swap(R,C);

		string result;
		if(X==1)
		{
			result = "GABRIEL";
		}else if(X==2)
		{
			if(R==1 || (R==3&&C==1) || (R==3&&C==3))
			{
				result = "RICHARD";

			}else{
				result = "GABRIEL";
			}
		}else if(X==3)
		{
			if( (R==3&& (C==2 || C==3) ) || ( R==4&&C==3))
			{
				result = "GABRIEL";

			}else{
				result = "RICHARD";

			}
		}else{
			if(R==4&&C>=3)
			{
				result = "GABRIEL";

			}else{
				result = "RICHARD";

			}
		}


		cout<<"Case #"<<_t+1<<": "<<result<<endl;
	}
}
