#include <iostream>
#include<vector>
using namespace std;
int N=0,M=0;
vector <vector <int> > arr;
vector <vector <int> > garden;
int findmax(int m, int n, int i,int j)
{
			
	if((i==N-1 && m==1) || (n==1 && j==M-1))
		return arr.at(i).at(j);
	int temp=findmax(m,n,i+m,j+n);
		if(arr.at(i).at(j)>temp)
		return arr.at(i).at(j);
		else 
			return temp;
}
int main()
{
	
	int T=0,he=0;
	arr.clear();
	garden.clear();
	
	N=0;M=0;
	bool flag=true;
	vector<int>temp;
	std::cin>>T;
	for(int casa=0;casa<T;casa++)
	{
		garden.clear();
		arr.clear();
		std::cin>>N>>M;
		temp.clear();
		for(int asd=0;asd<N ;asd++)
		{
			for(int asdf=0;asdf<M;asdf++)
			{
				cin>>he;
				temp.push_back(he);
			}
			arr.push_back(temp);
			temp.clear();
		}
		for(int as=0;as<N ;as++)
		{
			int maximum=findmax(0,1,as,0);
			vector <int> t1;
			for(int qwe=0;qwe<M;qwe++)
			{
				t1.push_back(maximum);
			}
			garden.push_back(t1);

		}
		for(int as=0;as<M;as++)
		{
			int maximum=findmax(1,0,0,as);
			
			for(int qwe=0;qwe<N;qwe++)
			{
				if(garden.at(qwe).at(as)>maximum)
					garden.at(qwe).at(as)=maximum;
			}
			
		}
		bool result=true;
		for(int p=0;p <N && result==true;p++)
			for(int o=0;o <M;o++)
				if(garden.at(p).at(o)!=arr.at(p).at(o))
				{
					result=false;
					break;
				}
				if(result) cout<<"Case #"<<casa+1<<": YES"<<endl;
		else cout<<"Case #"<<casa+1<<": NO"<<endl;
	}
return (0);
}