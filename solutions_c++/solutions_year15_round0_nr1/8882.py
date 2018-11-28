#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
//#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include<fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
//I m sai prasanna

using namespace std;




int main()
{
	fstream fin,fout;
	fin.open("A-large.in");
	fout.open("out_ovation.txt");
	int t;
	fin>>t;
	int count=1;
	while(t--)
	{
		int temp;fin>>temp;
		string a;
		fin>>a;
		
		int sum=a[0]-'0';
		int ans=0;
		for(int i=1;i<a.length();i++)
		{
			if(a[i]!='0' && i>sum){ans+=i-sum;sum=i;}
			sum+=a[i]-'0';
		}
		fout<<"Case #"<<count++<<": "<<ans<<'\n';
	}
 	return 0;
}

