#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <fstream>
#include <sstream>
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

bool check(int num)
{
int len=0,r=num;string s="",sr="";
while(r!=0){len++;s+=(r%10)+'0';r/=10;}
while(len--){sr+=s[len];}
if(s==sr)return true;
else return false;	
}
int main()
{
ifstream in("inc.txt");	
ofstream out("outc.txt");	
int T,i=1;
in>>T;
while(i<=T)
{
int a,b,cnt=0;
in>>a>>b;
for(int x=a;x<=b;x++)
{
	double root=sqrt(x);
	int r=(int)root;
	if(r==root)
	{if(check(x)&&check(root))cnt++;}
}	
out<<"Case #"<<i<<": "<<cnt<<'\n';   

i++;
}

return 0;
}
