#include <fstream>
#include <algorithm>
#include <cstring>
#include <sstream>
#include <vector>
#include <iostream>
#define	   LIMIT 1000
using namespace std;
int main(int argc, char *argv[])
{
	string infpath="A-small-attempt2.in";
	string outfile="A-small-attempt2.out";
	string Template="Case #";
	int N,T1,T2;
	int temp;
	vector<int> vecx,vecy;
	ifstream inf(infpath.c_str(),ifstream::in);
	ofstream ouf(outfile.c_str(),ofstream::out);
	inf>>N;
	for(int Case=0;Case<N;Case++)
	{
		vecx.clear();
		vecy.clear();
		inf>>T1;
		for(int k=0;k<4;k++)
		  for(int p=0;p<4;p++)
		  {
			  inf>>temp;
			  if(k==(T1-1))
				vecx.push_back(temp);
		  }
		inf>>T2;
		for(int k=0;k<4;k++)
		  for(int p=0;p<4;p++)
		  {
			  inf>>temp;
			  if(k==(T2-1))
				vecy.push_back(temp);
		  }
	
		sort(vecx.begin(),vecx.end());
		sort(vecy.begin(),vecy.end());
		vector<int> vecre;
		size_t k=0,p=0;
		while(k<vecx.size()&&p<vecy.size())
		{
			if(vecx[k]==vecy[p])
			{
			  vecre.push_back(vecx[k]);
			  k++;p++;
			}
			else if(vecx[k]<vecy[p])
			  k++;
			else
			  p++;
		}
		if(vecre.size()==0)
			ouf<<Template<<(Case+1)<<": "<<"Volunteer cheated!"<<endl;
		else if(vecre.size()==1)
		  ouf<<Template<<(Case+1)<<": "<<vecre[0]<<endl;
		else
		  ouf<<Template<<(Case+1)<<": "<<"Bad magician!"<<endl;
	}
	inf.close();
	ouf.close();
	return 0;
}





