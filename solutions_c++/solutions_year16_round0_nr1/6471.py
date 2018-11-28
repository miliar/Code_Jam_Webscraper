#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <math.h>
#include <stdlib.h>
#include <cstdlib>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <map>
#include <set>
using namespace std;
const unsigned long long O = 2e9;
const double E = 1e-13;
const double pi = 3.1415926536;
int DX[] = { 1, -1, 0, 0 };
int DY[] = { 0, 0, 1, -1 };

/*bool valid(int x, int y)
{
    return ((x >= 0 && x<n) && (y >= 0 && y<n));
}*/
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,X=1;
	cin>>t;
	while(t--)
	{
		long long n,num=1,tmp1;
		cin>>n;
		tmp1=n;
		bool vis[10]={0},ok=0;

		while(n>0)
		{
			long long tmp=n;
			num++;
			ok=1;
			while(tmp>0)
			{
				vis[tmp%10]=1;
				tmp/=10;
			}

			for(int i=0;i<10;i++)
				ok&=vis[i];

			if(ok)
				break;
			n=tmp1*num;
		}

		if(!ok)
			cout<<"Case #"<<X++<<": "<<"INSOMNIA\n";
		else
			cout<<"Case #"<<X++<<": "<<n<<endl;
	}
}
