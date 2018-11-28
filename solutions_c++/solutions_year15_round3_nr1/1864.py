#include <vector> 
#include <string>
#include <iostream>
#include <algorithm>
#include <climits>
#include <map>
#include <queue>  
#include <fstream>
using namespace std;


int main()
{
	ifstream in;
	in.open("input.txt");
	ofstream out;
	out.open("output.txt");

	int n;
	in >> n;
	
	for (int i = 0; i < n; i++)
	{
		int r, c, w;
		in >> r >> c >> w;

		int result;
		int resultLast = 0;
		resultLast += c / w + w - 1 + ((c % w) == 0 ? 0 : 1);
		result = resultLast + (r - 1)*c / w;
		out<<"Case #"<<i + 1<<": " << result<<endl;
	}

}