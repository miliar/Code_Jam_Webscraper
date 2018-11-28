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
double cons=.00000001;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int war(vector<double>bloc1,vector<double>bloc2)
{

bool ch=0;
for(int i=0;i<bloc1.size();i++)
{
ch=0;	
for(int j=0;j<bloc2.size();j++)
{
if(bloc2[j]>bloc1[i])
{

bloc2.erase(bloc2.begin()+j);
ch=1;
break;	
	
	}	
	
	}	
if(ch==0)
{
return bloc2.size();	
	
	}	
	
	
	}	
	
	
}
int dwar(vector<double>bloc1,vector<double>bloc2)
{
int coun=0;
bool ch=0;
for(int i=0;i<bloc1.size();i++)
{ch=0;
for(int j=bloc2.size()-1;j>=0;j--)
{


if(bloc1[i]>bloc2[j])
{ch=1;
	coun++;
bloc2.erase(bloc2.begin()+j);
break;
	}	
	
	
}

if(ch==0)
bloc2.erase(bloc2.begin()+bloc2.size()-1);

	}	
	return coun;
}
	
	


int main(int argc, char *argv[]) {
/*READ("A-large.in");
WRITE("A.out");
*/
freopen("D-small-attempt0.in", "r", stdin);
freopen("D-small-attempt0.out", "w", stdout);
vector<double>bloc1;
vector<double>bloc2;

int n,c;
cin>>n;

for(int i=0;i<n;i++)
{
cin>>c;
bloc1.resize(c);
bloc2.resize(c);
for(int j=0;j<c;j++)
cin>>bloc1[j];
for(int j=0;j<c;j++)
cin>>bloc2[j];
sort(bloc1.begin(),bloc1.end());	
sort(bloc2.begin(),bloc2.end());	
cout<<"Case #"<<i+1<<": ";
cout<<dwar(bloc1,bloc2)<<" "<<war(bloc1,bloc2)<<endl;;



	
	
	
}


	return 0;
}
