#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <map>
void makeInVector(std::string & kl,std::vector<int> &row,int &smax)
{
	using namespace std;
	int digits = 0;
	for(int i=0;i<smax;i++)
	{

		char a = kl[i];
		int ia = a - '0';
		row.push_back(ia);
	}


}
int main()
{
	int ts;
	std::cin>>ts;
	int ks=ts+1;
	typedef std::pair<int, std::string> pair_k;
	std::map<int,pair_k> maa;





	for(int j=0;j<ts;j++)
	{
		int SMax ;
		std::string row;

		std::cin>>SMax;
		std::cin>>row;
		if(j==ts-1)
		{
			std::cout<<"\n";
		}
		SMax++;
	//	maa.insert( std::make_pair( i, std::make_pair(SMax,row) ) );
	//}
	//for(int j=0;j<ts;j++)
	//{
	//	pair_k pk=maa[j];
	//	int SMax=pk.first ;
	//	std::string row=pk.second;

		std::vector<int> rowData;

		makeInVector(row,rowData,SMax);
		int k=0;
		int count=0;
		int extra=0;
		for(int i = 0;i<rowData.size();i++)
		{


			if(count<k)
			{
				if(rowData[i]!=0)
				{
					extra=extra+k-count;
					count=count+extra;
				}
			}


			count = count+rowData[i];
			k++;
		}
		std::cout<<"Case #"<<j+1<<": "<<extra<<std::endl;

	}
}
