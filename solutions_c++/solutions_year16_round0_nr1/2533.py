#include <iostream>
#include <fstream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <set>
using namespace std;

bool isallone(vector<bool>& v)
{
	bool ret = true;
	for(unsigned int i = 0; (i<v.size()) && ret;i++)
	{
		if(!v[i]) ret = false;
	}
	return ret;
}

string solve(int n)
{
	int i = 1;
	string ret = "";
	if(n==0)
	{
		ret = "INSOMNIA";
	}else{

		vector<bool> vec(10,false);
		//vec[0] = true;

		while(!isallone(vec))
		{
			ostringstream str;
			str<<(n*i);
			cout<<" str "<< str.str()<<endl;
			string s = str.str();
			for(unsigned int j = 0;j<s.size();j++)
			{
				int m = s[j]-'0';
				cout<<s[j]<<endl;
				vec[m] = true;
			}
			i++;
		}
		ostringstream str;
		str<<(i-1)*n;
		ret = str.str();

	}

	return ret;
}


int main() {

	ifstream infile("small.in");
	ofstream outfile("small.out");

	if(!infile.is_open() || !outfile.is_open())
	{
		cout<<"file error"<<endl;
		exit(1);
	}

	int cases = 0, i=0;
	string line = "";

	vector<string> words;

	infile>>cases;

	getline(infile,line);
	while(i<cases)
	{
		getline(infile,line);
		cout<<line<<endl;
		stringstream s;
		int num = 0;
		s<<line;
		s>>num;
		string alma = solve(num);

		outfile << "Case #" << i+1 << ": "<< alma <<endl;
		i++;
	}

	return 0;
}
