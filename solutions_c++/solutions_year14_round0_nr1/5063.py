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
int place;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
int compute(vector<int> v1,vector<int>v2)
{
	int c=0;
	for(int i=0;i<4;i++)
	for(int j=0;j<4;j++)
	{
if(v1[i]==v2[j])
{c++;
place=v1[i];
break;
}

	}

return c;
}

int main(int argc, char *argv[]) {
/*READ("A-large.in");
WRITE("A.out");
*/
freopen("A-small-attempt0.in", "r", stdin);
freopen("A-small-attempt0.out", "w", stdout);
vector<vector<int > >vec;
vec.resize(4);
vector<vector<int > >vec2;
vec2.resize(4);

for(int i=0;i<4;i++)
{vec[i].resize(4);
vec2[i].resize(4);

}
int n,f,s,c=0;
cin>>n;
for(int i=0;i<n;i++)
{
c=0;
cin>>f;
f--;
for(int j=0;j<4;j++)
for(int k=0;k<4;k++)
cin>>vec[j][k];
cin>>s;
s--;
for(int j=0;j<4;j++)
for(int k=0;k<4;k++)
cin>>vec2[j][k];
c=compute(vec[f],vec2[s]);
cout<<"Case #"<<i+1;
if(c==1)
cout<<": "<<place<<endl;
else if(c>1)
cout<<": Bad magician!"<<endl;
else if(c==0)
cout<<": Volunteer cheated!"<<endl;






}




	return 0;
}
