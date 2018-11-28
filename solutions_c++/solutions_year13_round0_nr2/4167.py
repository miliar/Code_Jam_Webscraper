#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>

using namespace std;
bool ifWorks(int n, int m, const vector<int> &a);

struct square
{
	bool row;
	bool column;
	square()
	{
		row=false;
		column=false;
	}
};

bool ifWorks(int n, int m, const vector<int> &a)
{
	struct square lawn[n][m];
	bool flag=true;
	int max=0;
	for (int i=0; i<n; ++i)
	{
		for (int j=0; j<m; ++j)
		{
			if (a.at(i*m+j)>max)
				max=a.at(i*m+j);
		}
		for (int j=0; j<m; ++j)
		{
			if (a.at(i*m+j)<max)
				lawn[i][j].row=false;
			else
				lawn[i][j].row=true;
		}
		max=0;
	}
	max=0;
	for (int j=0; j<m; ++j)
	{
		for (int i=0; i<n; ++i)
		{
			if (a.at(i*m+j)>max)
				max=a.at(i*m+j);
		}
		for (int i=0; i<n; ++i)
		{
			if (a.at(i*m+j)<max)
				lawn[i][j].column=false;
			else
				lawn[i][j].column=true;
		}
		max=0;		
	}
	for (int i=0; i<n; ++i)
	{
		for (int j=0; j<m; ++j)
		{
			//cout<<i*m+j+1<<" "<<lawn[i][j].row<<" "<<lawn[i][j].column<<endl;
			if (!lawn[i][j].row && !lawn[i][j].column)
			{	
				flag=false;
				break;
			}
		}
		 if (!flag)
			break; 		
	}
	return flag;
}


int main()
{
	bool state=false;
	string line,subStr;
	int count=0;
	int n=0,m=0;
	string::size_type pos1=0,pos2=0;
	ifstream infile("testcase2",ios::binary | ios::in);
	if(!infile)		
		return -1;
	getline(infile,line);
	count=atoi(line.c_str());
	for (int i=0; i<count; ++i)
	{
		vector<int> tt;
		getline(infile,line);
		
		pos2=line.find(' ',pos1);

		subStr=line.substr(pos1, pos2 - pos1);
		n=atoi(subStr.c_str());
		pos1 = pos2 + 1;
		subStr=line.substr(pos1);
		m=atoi(subStr.c_str());
		pos1=0;
		pos2=0;
		
		for (int j=0; j<n; ++j)
		{
			pos1=0;
			pos2=0;
			getline(infile,line);
			pos2=line.find(' ',pos1);
			while (string::npos != pos2)
			{
				subStr=line.substr(pos1, pos2 - pos1);
				tt.push_back(atoi(subStr.c_str()));
				pos1 = pos2 + 1;
				pos2 = line.find(' ', pos1);
			}
			subStr=line.substr(pos1);
			tt.push_back(atoi(subStr.c_str()));	
			pos1=0;
			pos2=0;
		}
		if (n==1 || n==1)
		{
			cout<<"Case #"<<i+1<<": YES"<<endl;
			continue;
		}
//		cout<<tt.size()<<": n: "<<n<<" m: "<<m<<endl;
		state=ifWorks( n, m, tt);
		if (state)
			cout<<"Case #"<<i+1<<": YES"<<endl;
		else
			cout<<"Case #"<<i+1<<": NO"<<endl;
	}
	
	
	
	return 0;
}

