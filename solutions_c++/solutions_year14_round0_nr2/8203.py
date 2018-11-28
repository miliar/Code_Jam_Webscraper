#include <iostream>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <string.h>
#include <cmath> 
#include<iomanip>
#include <cstring>
#include <ctype.h>
#include <stdio.h> 
#include<sstream>
#include<map>
#include<vector>
#include<queue>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	double c,f,x,rate,sec,cook;
	cin>>t;
	for(int i=0;i<t;i++)
	{
	cin>>c>>f>>x;
	cook=0;
	rate=2;
	sec=0;
	while(1)
	{
	if(x/rate<((c/rate)+(x/(rate+f))))
		{
			sec+=x/rate;
			printf("Case #%d: %.7f\n",i+1,sec);
			break;
	}
	else {
		sec+=c/rate;
		rate+=f;
	}

	}
	
	
	
	}
	return 0;
 
}