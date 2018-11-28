#include <iostream>
#include <iomanip>
#include <cmath>
#include <list>
#include <stack>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
string name;
istringstream iss;
char arr[1000010];
bool flag[1000010];
long long cases,n,c,res,counter,arr2[1000010];
int main()
{
	//freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	cin>>cases;
	for(long long kase=1;kase<=cases;kase++)
	{
		cin>>name>>n;
		iss.str(name);
		for(c=1;iss>>arr[c];c++)
		{
			arr2[c]=-1;
		}
		c--;
		iss.clear();
		res=0;
		counter=0;
		for(long long i=1;i<=c;i++)
		{
			if(!(arr[i]=='a' || arr[i]=='e' || arr[i]=='i' || arr[i]=='o' || arr[i]=='u'))
			{
				counter++;
				if(counter>=n)
				{
					flag[i]=true;
					for(long long j=i-n+1;j>=1;j--)
					{
						if(arr2[j]!=-1)break;
						arr2[j]=i;
					}
				}
				else
				{
					flag[i]=false;
				}
			}
			else
			{
				counter=0;
				flag[i]=false;
			}
		}
		res=0;
		for(long long i=1;i<=c;i++)
		{
			if(arr2[i]==-1)break;
			res+=c-arr2[i]+1;
		}
		cout<<"Case #"<<kase<<": "<<res<<"\n";
	}
	return 0;
}
