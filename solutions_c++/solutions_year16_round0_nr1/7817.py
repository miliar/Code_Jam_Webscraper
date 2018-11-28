// GoogleCodeJam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <set>
#include <vector>
#include <fstream>

using namespace std;

void main()
{
	ofstream outfile("pb1outlarge.txt");
	ifstream infile("pb1inlarge.txt");
	
	cin.rdbuf(infile.rdbuf());
	set<int> v;
	int n;
	cin>>n;
	int m = 1;
	for (int i = 0; i < n; i++)
	{
		int temp;
		outfile<<"Case #"<<i+1<<": ";
		cin>>temp;
		if(temp == temp*2)
		{
			outfile<<"INSOMNIA"<<endl;
			continue;
		}
		bool found = false;
		int number = temp;
		int j = 1;
		int save = temp;
		while(!found)
		{
			
			while(number!=0)
			{
				int t = number%10;
				v.insert(t);
				number /=10;
			}
			if(v.size() == 10)
			{
				outfile<<save<<endl;
				found = true;
			}
			
			number = temp*(++j);
			save = number;
		}
		v.clear();
		if(i%10000 == 0)
			cout<<i/10000<<endl;
	}
	//cin>>n;
}