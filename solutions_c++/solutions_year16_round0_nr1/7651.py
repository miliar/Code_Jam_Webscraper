#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iterator>
#include<cmath>
#include<string>
#include<sstream>
#include<cstring>
#include<ctype.h>
#include<iomanip>
#include<bitset>
#include<stdio.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
 
using namespace std;

string int_to_str(long long x)
{
	string xs;
	stringstream ss;
	ss<<x;
	xs=ss.str();
	return xs;
}
int main() 
{
freopen("small_input.txt","r",stdin);
freopen("small_output.txt","w",stdout);
int t,flag;
long long temp,n,ans;
string str;
cin>>t;
map<int,int> m;
for(int i=1; i<=t; i++)
{
	flag=0;
	m.clear();
	cin>>n;
	for(int j=1; j<100000; j++)
	{
		temp=j*n;
		str=int_to_str(temp);
		for(int s=0; s<str.size(); s++)
			m[str[s]-'0']++;
		if(m.size()==10)
		{
			flag=1;
			ans=temp;
			break;
		}
	}
	if(flag==1)
		cout<<"Case #"<<i<<": "<<temp<<endl;
	else
		cout<<"Case #"<<i<<": INSOMNIA"<<endl;
}

//system("pause");
  return 0;
}
