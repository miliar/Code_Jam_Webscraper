#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>

using namespace std;

vector<long long> motes;

void debug(vector<long long> v)
{
	for(int i=0;i<v.size();i++) cout<<v[i]<<" ";
	cout<<endl;
}
int findout(vector<long long> temp,long long mi)
{
	if(temp.empty()) return 0;
	int minele=*min_element(temp.begin(),temp.end());
	if(minele>=mi && mi==1) return temp.size();
	debug(temp);
	cout<<mi<<endl;
	while(temp[0]<mi)
	{
		mi+=temp[0];
		temp.erase(temp.begin());
		if(temp.empty()) break;
	}
	if(temp.empty()) return 0;
	vector<long long> v1=temp;
	v1.erase(v1.end()-1);
	debug(temp);
	debug(v1);
	cout<<endl;
	return min(1+findout(temp,mi+mi-1),1+findout(v1,mi));
}
int main()
{
	int t;
	ifstream fin("file.in");
	ofstream fout("SaiBaba.out");
	fin>>t;
	int index=0;
	while(t--)
	{
		long long mine;
		int n;
		fin>>mine>>n;
		motes.clear();
		for(int i=0;i<n;i++)
		{
			long long temp;fin>>temp;
			motes.push_back(temp);
		}
		sort(motes.begin(),motes.end());
		fout<<"Case #"<<++index<<": "<<findout(motes,mine)<<endl;
	}
	return 0;
}
