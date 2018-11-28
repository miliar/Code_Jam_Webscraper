#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>

using namespace std;

bool ispal(int num)
{
    vector<int> v;
    while(num!=0)
    {
        v.push_back(num%10);
        num /= 10;
    }

    for (int i = 0; i < v.size(); ++i)
    {
        if (v[i]!=v[v.size()-1-i])
	    return false;
    }
    return true;
}

int main(int argc, char *argv[])
{
  if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int n;
    fin >> n;
    for (int i = 0; i < n; ++i)
    {
	int min, max;
	int count = 0;
	fin >> min;
	fin >> max;
	min = ceil(sqrt(min));
	max = floor(sqrt(max));
	for (int j = min; j <= max; ++j)
	{
	    if (ispal(j) && ispal(j*j))
		count++;
	}
	fout << "Case #" << i+1 << ": " << count << endl;
    }
}
