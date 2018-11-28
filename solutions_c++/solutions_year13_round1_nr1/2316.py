#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>
using namespace std;
const double PI =  3.1415926535897932384626433832795028841971693993751058209;
int main()
{
	ifstream cin("A-small-attempt0(1).in");
	ofstream cout("A-OR1-small.out");
	int T;
	cin>>T;
	for (int i = 0; i < T ; i++)
	{
		long long r,t;
		cin>>r>>t;
		int counter=0;
		long long currentArea = (r+1)*(r+1)-r*r;
		long long newRadius = r+1;
		long long remainning = t;
		while(true)
		{
			if(currentArea<=remainning)
			{
				remainning-=currentArea;
				counter++;
			}
			else
			{
				break;
			}
			currentArea+=4;
		}
		/*while(true)
		{
			long long newArea = newRadius*newRadius - (newRadius-1)*(newRadius-1);
			if(remainning>=newArea)
			{
				counter++;
				remainning-=newArea;
			}
			else
			{
				break;
			}
			newRadius+=2;
		}*/
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}