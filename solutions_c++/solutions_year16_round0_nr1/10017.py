#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

string funct(int N, string& seen)
{
	//if(e == 12) return "INSOMINA";
	string trux = "0123456789";
	
	string a = to_string(N);
	for(int j=1; j!=1000000;j++)
	{
		for(int i=0; i<a.length();i++)
		{
			if(seen.find(a[i])==std::string::npos) seen.push_back(a[i]);
			//cout<<seen<<endl;
		}
		sort(seen.begin(),seen.end());
		//cout<<seen<<endl;
		if(seen==trux) return a;
		else a=to_string(N*j);
	}
	return "INSOMNIA";
}


int main()
{
	//string seen = "";
	ifstream filex;
	filex.open("A-large.in");
	ofstream filx;
	filx.open("A-large.out");
	vector<string> results;
	int T, N,x=1;
	bool flag = false;
	filex>>T;
	for(int i =0; i<T; i++)
	{
		filex>>N;
		string seen="";
		if(N == 0) results.push_back("INSOMNIA");
		else results.push_back(funct(N,seen));
	}
	for(vector<string>::iterator it = results.begin(); it!=results.end();it++)
	{
		if(it == results.end()-1)
			filx<<"CASE #"<<x<<": "<<*it;
		else
			filx<<"CASE #"<<x<<": "<<*it<<endl;
		x++;
	}
	return 0;
}