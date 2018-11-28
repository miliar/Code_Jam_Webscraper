#include <iostream>
#include <fstream>
#define _USE_MATH_DEFINES
#include <math.h>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <functional>
#include <string>

using namespace std;

bool isConsonant(char c)
{
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
		return false;
	else
		return true;
}

bool containsn(string sub,int n)
{
	int length=strlen(sub.c_str());
	int cnt=0;
	//bool prevcons=true;
	string check=" ";
	//cout<<sub<<endl;
	for (int i = 0; i < length; i++)
	{
		if(isConsonant(sub[i]))
		{
			cnt++;
							//cout<<"yes"<<endl<<sub<<endl<<cnt<<endl;

			//prevcons=true;
		}
		else
		{

			cnt=0;
							//cout<<"no"<<endl<<sub<<endl<<cnt<<endl;

			//prevcons=false;
		}
		if (cnt>=n)
		return true;
	
	}
			return false;

	
}

int main()
{
	int cases,n;
	//unsigned long long r,t,req,white,black;
	string line,temp;
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
	cin>>cases;
	getline(cin,line);
	for (int x=0; x < cases ; x++)
	{
		int nvalue =0;
		int j=0;
		string name=" ";
		getline(cin,line);
		istringstream strstr(line);
		while(strstr >> temp)
		{
			if (j==0)
				name=temp;
			else
				n=atoi(temp.c_str());
			j++;
		}
		int len=strlen(name.c_str());
		//int len2=n;
		string sub=" ";
		for(int a=0;a<len-n+1;a++)
		{

			int len2=strlen((name.substr(a,len)).c_str());
			for(int b=n;b<=len2;b++)
			{

				sub=name.substr(a,b);
				if (containsn(sub,n))
				{
					nvalue++;
				}
			}
		}


		cout<<"Case #"<<x+1<<": "<<nvalue<<endl;
	}
	return 0;

}

