#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
using namespace std;

int warOpt(vector<double> nom, vector<double> ken)
{
	int size = nom.size();
	for( int i=0; i<size; i++)
	{
		bool flag = false;
		for(int j=0; j<ken.size(); j++)
		{
			if(nom[0] < ken[j])
			{
				nom.erase(nom.begin());
				ken.erase(ken.begin()+j);
				flag=true;
				break;
			}
		}

		if(!flag)
		{
			return nom.size();
		}
	}

	return 0;
}

int decWarOpt(vector<double> nom, vector<double> ken)
{
	int size = nom.size();
	int p=0;
	for( int i=0; i<size; i++)
	{
		bool flag = false;
		
		if(nom[0] > ken[0])
		{
			p++;
			nom.erase(nom.begin());
			ken.erase(ken.begin());
		}
		else
		{
			nom.erase(nom.begin());
			ken.erase(ken.begin()+ken.size()-1);
		}

	}

	return p;
}

int main()
{

	int T=0;
	ifstream fin("D-large.in");
	if(!fin)
		return 1;

	ofstream fout("DL.out");
	if(!fout)
		return 1;

	fin>>T;
	
	if(T<1 || T>50)
		return 1;
	
	for(int i=0; i<T; i++)
	{
		int N;
		fin>>N;
		if(N<1 || N>1000)
			return 1;

		vector<double> naomi;
		vector<double> ken;
		for(int i=0; i<N; i++)
		{
			double n;
			fin>>n;
			naomi.push_back(n);
		}
		for(int i=0; i<N; i++)
		{
			double n;
			fin>>n;
			ken.push_back(n);
		}
		sort(naomi.begin(), naomi.end());
		sort(ken.begin(), ken.end());
		int war = warOpt(naomi,ken);
		int dec = decWarOpt(naomi,ken);
		fout<<"Case #"<<i+1<<": "<<dec<<" "<<war<<endl;
	}
	return 0;
}