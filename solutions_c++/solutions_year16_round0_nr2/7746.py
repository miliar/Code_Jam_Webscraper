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


int main() 
{
freopen("small_input.txt","r",stdin);
freopen("small_output.txt","w",stdout);
string str;
int t,ans=0;

cin>>t;
for(int j=1; j<=t; j++)
{
	ans=0;
	cin>>str;
	for(int i=0; i< str.size(); i++)
	{
		if(i==0 && str[i]=='-')
		{
			ans+=1;
			while(i<str.size() && str[i]=='-')
				i++;
		}
		for(; i<str.size(); i++)
		{
			if(str[i]=='-')
			{
				ans+=2;
				while(i<str.size() && str[i]=='-' )
					i++;
			}
					
		}
		
	}
	cout<<"Case #"<<j<<": "<<ans<<endl;
}
//system("pause");
  return 0;
}
