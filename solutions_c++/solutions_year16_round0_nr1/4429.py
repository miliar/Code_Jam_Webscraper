#include<iostream>
#include<map>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("test.in");
	ofstream out("result.out");
	int k;
	in>>k;
	for(int j=0;j<k;++j)
	{
		int num;
		in>>num;
		if(num==0)
		{
			out<<"Case #"<<j+1<<": INSOMNIA"<<endl;
			continue;
		}
		map<int,int>counts;
		for(int i=1;;++i)
		{
			int n=num*i;
			while(n>0)
			{
				counts[n%10]++;
				n/=10;
			}
			if(counts.size()==10)
			{
				out<<"Case #"<<j+1<<": "<<i*num<<endl;
				break;
			}

		}

	}

	cin.get();
	cin.get();
	return 0;
}