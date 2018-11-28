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

int main(int argc, char *argv[]) {
float a=22,b=7;
float f=a/b;
READ("A-small-attempt0.in");
WRITE("A-small-attempt0.out");

int test;
double t,r,area,newarea,curarea;
cin>>test;
int count=0;
for(int i=0;i<test;i++)
{area=0,newarea=0,curarea=0;
cin>>r>>t;
area=(r*r)*f;
count=0;
while(1)
{
r+=1;
newarea=(r*r)*f;
curarea=newarea-area;
if((curarea)/f<=t)
{count++;
t-=(curarea/f);
}
else
break;

r+=1;	
area=(r*r)*f;
}
cout<<"Case #"<<i+1<<": "<<count<<endl; 
	
	
	
}


	return 0;
}
