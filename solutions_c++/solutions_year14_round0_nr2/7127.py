#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

#define OO (int) 1e9

using namespace std;
	

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.text","w",stdout);
	int tc;
	cin>>tc;
	for(int i=1;i<=tc;i++)
	{
		double C,F,X;
		cin>>C>>F>>X;
		double current=0;
		double result=0;
		double firstChoice,secondChoice;
		double rate=2;
		while(1)
		{
			firstChoice=(X-current)/rate;
			if(current>=C)
				secondChoice=((X-(current-C))/(rate+F));
			else 
				secondChoice=(X/(rate+F))+( (C-current)/rate );

			if(secondChoice<firstChoice)
			{
				if(current<C)
					result+=(C-current)/rate;
				else current-=C;
				rate+=F;
			}
			else 
			{
				result+=firstChoice;
				break;
			}

		}
		cout<<"Case #"<<i<<": "<<fixed<<setprecision(7)<<result<<endl;
	}

}