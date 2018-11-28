#include <iostream>
#include <iomanip>
#include <cstdio>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <cmath>
#include <algorithm>
#include <memory.h>
#include <string>
#include <cstring>
#include <sstream>
#include <cstdlib>
#include <ctime>
#include <cassert>
#include <utility>
#include <fstream>
using namespace std;
int main()
{
	std::iostream::sync_with_stdio(false);
	int t;
	ofstream myfile;
	myfile.open ("example.txt");
	ifstream infile;
	infile.open("D-large.in");
	infile>>t;
	int s=1;
	while(t--)
	{
		int n;
		infile>>n;
		std::vector<double> v1(n),v2(n);
		int i;
		for(i=0;i<n;i++)
		{
			infile>>v1[i];
		}
		for(i=0;i<n;i++)
		{
			infile>>v2[i];
		}
		sort(v1.begin(),v1.end());
		sort(v2.begin(),v2.end());
		int j=0;
		i=0;
		int ans1,ans2;
		std::vector<int> w;
		while(i<n && j<n)
		{
			while(v2[j]<v1[i] && j<n)
			{
				j++;
			}
			if(j<n && v2[j]>v1[i])
			{
				w.push_back(j);
				i++;
				j++;
			}
			else
			{
				break;
			}
		}
		ans2=n-i;
		i=0;
		j=0;
		int p=n;
		ans1=0;
		while(i<n && j<p)
		{
			if(v1[i]>v2[j])
			{
				i++;
				j++;
				ans1++;
			}
			else
			{
				i++;
				p--;
			}
		}
		myfile<<"Case #"<<s<<": "<<ans1<<" "<<ans2<<endl;
		s++;
	}
	return 0;
}