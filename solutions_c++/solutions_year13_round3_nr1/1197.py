#include<iostream>
#include<stdlib.h>
#include<fstream>
#include<math.h>
using namespace std;


bool judgeCon(char c)
{
	if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
		return false;
	else
		return true;
}

int main()
{
	ifstream file("A-small-attempt0.in");
	cin.rdbuf(file.rdbuf());
	ofstream out("out.txt");
	cout.rdbuf(out.rdbuf());

	long long T;
	char str[120];
	int n;
	int length = 0;

	cin>>T;
	for(int x=0;x<T;x++)
	{
		cin>>str;
		cin>>n;

		length = strlen(str);
		int sum = 0;
		for(int i=0;i<length;i++)
		{
			for(int j=i;j<length;j++)
			{
				if(j-i+1<n)
					continue;

				bool suc = false;
				int cur = 0;
				for(int a=i;a<=j;a++)
				{
					if(judgeCon(str[a]))
					{
						cur++;
						if(cur==n)
						{
							suc = true;
							break;
						}
					}
					else
					{
						cur = 0;
					}
				}

				if(suc)
				{
					sum++;
				}
			}
		}

		cout<<"Case #"<<x+1<<": "<<sum<<endl;
	}

	return 0;
}
		