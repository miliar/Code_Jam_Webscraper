#include<iostream>
#include<vector>
#include<algorithm>
#include<string>
#include<cstring>
#include<fstream>
#include<ostream>
#include<cmath>


using namespace std;

bool is_pall(long long int x)
{
	vector<long long int> v1,v2;
	while(x != 0)
	{
		v1.push_back(x%10);
		x /= 10;
	}
	v2 = v1;
	reverse(v2.begin(),v2.end());
	if(v1 == v2)
		return 1;
	else
		return 0;
}

int main(int argc,char *argv[])
{
	ifstream infile;
	ofstream outfile;
	string line;

	infile.open(argv[1]);
	outfile.open("output.txt");
	getline(infile,line);
	int cases = atoi(line.c_str());
	for(int i=1;i<=cases;i++)
	{
		getline(infile,line);
		vector<long long int> vec;
		long long int count =0;
		string delimiters = " ";
		size_t current;
		size_t next = -1;
		do
		{
			current = next + 1;
			next = line.find_first_of( delimiters, current );
			vec.push_back(atol((line.substr( current, next - current )).c_str()));
		}while (next != string::npos);	

		for(long long int j=sqrt(vec[0]);j<=sqrt(vec[1]);j++)
		{
			long long int x = pow(j,2);
			if( is_pall(j) && is_pall(x) && (x>=vec[0]) && (x<=vec[1]))
				count++;
		}
		
		outfile << "Case #" << i << ": " << count << endl;
	}
	infile.close();
	outfile.close();
	return 0;
}

