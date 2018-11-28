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
freopen("A-large.in", "r", stdin);
freopen("A-large.out", "w", stdout);
int n,t,res,men;
string s;
cin>>t;

for(int i=0;i<t;i++){
cin>>n>>s;
res=0;
men=0;
men+=s[0]-'0';
for(int j=1;j<s.length();j++)
{
if(s[j]>'0')
{
  if(j>men)
    {
        res+=j-men;
       men+=j-men;
    }
    men+=s[j]-'0';
}

}
cout<<"Case #"<<i+1<<": "<<res<<endl;




}

	return 0;
}
