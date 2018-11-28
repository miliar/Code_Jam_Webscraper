#include <vector>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <queue>
#include <fstream>

using namespace std;
int main()
{
ifstream fin("B-large.in");
ofstream fout("output2large.txt");
# define cin fin
# define cout fout
int r,i=1,p=10;
double n=0.0,a=0.0,k=0.0,c,f,x,t,min;
cin>>r;
LOOP:
while(i<=r)
{
cin>>c>>f>>x;
t=x/2;
a=t;
min=t;
while(a>=0.0000001)
{
n++;
k=k+c/(2+f*(n-1));
a=x/(2+f*n);
t=k+a;
if(t<min)
{
min=t;
}
else{
	cout<<"Case #"<<i<<": "<<setprecision(p)<<min<<'\n';
	k=0;a=0;min=0,n=0;
	i=i+1;
	goto LOOP;
}
}
}
return 0;
}

