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

bool palind(string s)
{
for(int i=0;i<s.size()/2;i++)
{if(s[i]!=s[s.size()-1-i])
return 0;
	}	
	
return true;	
}
string stream(int temp)
{
	stringstream ss;

ss<<temp;
string s;
ss>>s;
return s;
}

int main(int argc, char *argv[]) {
	
	
READ("C-small-attempt1.in");
WRITE("C-small-attempt1.out");
int n=3;

cin>>n;
int count =0;
string s;
int temp;
int a=10,b=120;
for(int i=0;i<n;i++)
{cin>>a>>b;
count=0;
for(int k=1;k*k<=b;k++)
{
temp=k*k;
s=stream(temp);
if(temp>=a&&palind(stream(k))==1)
count+=palind(s);	
}
cout<<"Case #"<<i+1<<": "<<count<<endl;	
	
	
}



	
	return 0;
}
