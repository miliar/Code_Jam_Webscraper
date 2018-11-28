#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int consec(string M,int a)
{
	int i;
	int cnt=0;
	for(i=0;i<M.size();i++)
	{
		if(cnt>=a)
			return 1;
		if(M.at(i)=='a'|| M.at(i)=='i'|| M.at(i)=='u'|| M.at(i)=='e'|| M.at(i)=='o')
			cnt=0;
		else
			cnt++;
	}
	if(cnt>=a)
			return 1;
	return 0;
}

int ans(string L, int a)
{
	int i,j;
	int cnt=0;
	int conse=0;
	string M;
	for(i=0;i<L.size();i++)
	{
		for(j=L.size();j>i+a-1;j--)
		{
			M=L;
			M.erase(j,L.size()-j);
			M.erase(0,i);
			if(consec(M,a)==1)
				cnt++;
		}
	}
	return cnt;
}

int main()
{
	int i,j,k,n;
	string L;
	int a;
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("out.out");
	in >> n;
	string line;
	getline(in, line);
	for(k=0;k<n;k++)
	{
		
		in >> L;
		in >> a;
		/*for(i=0;i<L.size();i++)
			out << L.at(i) << " ";
		out << "\n";*/
		out << "Case #" << k+1 << ": " << ans(L,a) << "\n";
	}
	in.close();
	out.close();
	return 0;
}
