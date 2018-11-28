#include <algorithm>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

typedef long long LL;


int main()
{
ifstream in("in.txt");
ofstream out("out.txt");	
int T,i=0;LL t,r;
in>>T;
while(i<T)	
{
LL cnt=0;	
in>>r>>t;
LL x=2*r+1;
while(x<=t)
{
	cnt++;t-=x;
	r=r+2;
	x=2*r+1;;
}

i++;
out<<"Case #"<<i<<": "<<cnt<<'\n';
}	


return 0;
}




