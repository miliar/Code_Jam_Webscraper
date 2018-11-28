#include <iostream>
#include <fstream>

using namespace std;
int main()
{
	ifstream file("A-large.in");
	ofstream f;
	f.open("output.txt");
	char ch;
	int t, s, i, sum, j, count, k;
	file>>t;
	file.get(ch);
	for(j=1;j<=t;j++)
	{
		file>>s;
		file.get(ch);
		char a[s+1];
		file>>a;
		file.get(ch);
		sum=0;
		count=0;
		for(i=1; i<=s+1;i++)
		{
			sum+=(int)(a[i-1])-48;
			if(sum<i)
			{
				sum+=i-sum;
				count++;
			}
		}
		f<<"Case #"<<j<<": "<<count<<endl;
	}
	return 0;
}
