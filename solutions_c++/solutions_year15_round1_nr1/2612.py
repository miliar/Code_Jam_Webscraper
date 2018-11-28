#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int method1(vector<int>& mush)
{

int eat = 0;

for(int i=0;i<mush.size()-1;i++)
{
	if(mush[i+1]<mush[i])
	{
		eat += mush[i]-mush[i+1];
	}

}

	return eat;

}

int method2(vector<int>& mush)
{


vector<int> rate(mush.size()-1);

for(int i=0;i<mush.size()-1;i++)
{

	rate[i]=mush[i]-mush[i+1];

}

int minrate = (*max_element(rate.begin(),rate.end()));

int eat = 0 ;
for(int i=0;i<mush.size()-1;i++)
{

	if(mush[i]<minrate)
	{
		eat += mush[i];
	}
	else
	{
		eat += minrate;
	}


}


	return eat;


}


int main()
{

int t;
std::cin>>t;

for(int i=0;i<t;i++)
{
	int n;
	std::cin>>n;
	vector<int> mush;
	int temp;
	for(int j=0;j<n;j++)
	{
		std::cin>>temp;
	 	mush.push_back(temp);
	}

	int ans1 = method1(mush);
	int ans2 = method2(mush);

	cout<<"Case #"<<i+1<<": "<<ans1<<" "<<ans2<<endl;


}




}
