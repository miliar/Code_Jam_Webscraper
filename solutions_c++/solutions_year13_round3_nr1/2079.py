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

bool check(string s,int n)
{
int c=0;	
for(int i=0;i<s.size();i++)	
	{
    if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u')	
	c++;
	else
	c=0;	
	if(c>=n)
    return 1;
		
	}
return 0;	
	
}

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
READ("A-small-attempt0.in");
WRITE("A-small-attempt0.out");
int t;
string s;
int n;
cin>>t;
int c=0;
string sub;
int v;
bool sure=0;
for(int i=0;i<t;i++)
{c=0;
cin>>s>>n;
for(int j=0;j<s.size()-n+1;j++)
{
sure=0;

sub=s.substr(j,n);

if(check(sub,n)==1)
{
c++;
sure=1;
}
v=sub.size();

for(int f=v+j;f<s.size();f++)
{
if(sure==1)
{c++;
continue;	
}
else
{sub+=s[f];
if(check(sub,n)==1)
{
c++;
sure=1;
}

}
}

	
	
	
	
	
}





cout<<"Case #"<<i+1<<": "<<c<<endl;
	
	
	
	
	
	
}








	return 0;
}
