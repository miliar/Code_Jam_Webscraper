#include   <fstream>
#include   <iostream>
#include   <iomanip>
#include   <algorithm>
#include   <cstring>
#include   <sstream>
#include   <vector>
#define	   LIMIT 1000
using namespace std;
int solveWar(vector<double> & vecx,vector<double> &vecy)
{
	int num=vecx.size();
	sort(vecx.begin(),vecx.end());
	sort(vecy.begin(),vecy.end());
	int i=0,j=0;
	while(i<num&&j<num)
	{
		if(vecx[i]<vecy[j])
		{
			i++;j++;
		}
		else
		  j++;
	}
	return (num-i);
}
int solveDWar(vector<double>& vecx,vector<double>& vecy)
{
	int num=vecx.size();
	sort(vecx.begin(),vecx.end(),greater<double>());
	sort(vecy.begin(),vecy.end(),greater<double>());
	int i=0,j=0;
	while(i<num&&j<num)
	{
		if(vecx[i]>vecy[j])
		{
			i++;j++;
		}
		else
		  j++;
	}
	return i;
}
void printvec(vector<double> vec)
{
	int num=vec.size();
	for(int i=0;i<num;i++)
	  cout<<vec[i]<<" ";
	cout<<endl;
}
int main(int argc, char *argv[])
{
	string infpath="D-large.in";
	string outfile="D-large.out";
	string Template="Case #";
	int N,T;
	double t1,t2;
	vector<double> vecx,vecy;
	ifstream inf(infpath.c_str(),ifstream::in);
	ofstream ouf(outfile.c_str(),ofstream::out);
	inf>>N;
	for(int Case=0;Case<N;Case++)
	{
		inf>>T;
		vecx.clear();
		vecy.clear();
		for(int p1=0;p1<T;p1++)
		{
			inf>>t1;
			vecx.push_back(t1);
		}
		for(int p2=0;p2<T;p2++)
		{
			inf>>t2;
			vecy.push_back(t2);
		}
		cout<<endl;
		int war=0,dwar=0;
		war=solveWar(vecx,vecy);
		printvec(vecx);
		printvec(vecy);

		dwar=solveDWar(vecx,vecy);
		printvec(vecx);
		printvec(vecy);

		ouf<<Template<<(Case+1)<<": "<<dwar<<" "<<war<<endl;
	}
	inf.close();
	ouf.close();
	return 0;
}
