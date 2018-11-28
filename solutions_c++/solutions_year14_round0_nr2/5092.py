#include <iostream>
#include <iostream>
#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <climits>
#include <cctype>
#include <cmath>
#include <sstream>
#include <cstdlib>
#include <climits>
#include <ctime>
#include <set>
#include <map>
#include <numeric>
#include <utility>
#include <deque>
#include <queue>
#include <stack>
#include <iomanip>
#include <complex>
#include <list>
#include <bitset>
#include <fstream>
#include <limits>
#include <memory.h>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
#include<sstream>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;


/* run this program using the console pauser or add your own getch, system("pause") or input loop */
bool decide(double c,double f, double x,double rate )
{
double time1=0,time2=0;
time1=x/rate;
time2=c/rate;
rate+=f;
time2+=x/rate;
if(time1>time2)
return 1;
return 0;	
	
	
}
int main(int argc, char *argv[]) {
freopen("B-large.in", "r", stdin);
freopen("B-large.out", "w", stdout);
double n,c,f,x,time=0, rate=2;
bool ch=0;
cin>>n;

for(int i=0;i<n;i++)
{
rate=2,time=0;
cin>>c>>f>>x;	
while(1)
{
if(decide( c, f, x,rate ))	
{
time+=c/rate;
rate+=f;


	
	}
	else
	{
time+=(x/rate);
cout<<"Case #"<<i+1<<": "<<setprecision (8)<<fixed <<time<<endl;
break;
		}	
	
}


	
	
}



	return 0;
}
