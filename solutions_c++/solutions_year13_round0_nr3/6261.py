#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
vector<int> v;
void pre()
{
	for(int i=1;i<=32;i++)
	{
		int temp=i;
		int reverse=0;
		while(temp!=0)
		{
			reverse = reverse*10;
			reverse = reverse+temp%10;
			temp = temp/10;
		}
		if(i==reverse)
		{

		
		int j = i*i;
		int k =i*i;
		int rep=0;
		while(k!=0)
		{
			rep = rep*10;
			rep = rep+ k %10;
			k=k/10;
		}
		if(j==rep)
			v.push_back(j);
		}
		
	}
	
}
int main()
{
	pre();
	//for(int i=0;i<v.size();i++)
		//cout<<v[i]<<" ";
	int t;
	cin>>t;
	for(int test=0;test<t;test++)
	{
		int count=0;
		int low,high;
		cin>>low>>high;
		
		for(int i=0;i<v.size();i++)
		{
			if(v[i]>=low&&v[i]<=high)
				count++;
		}
	
		cout<<"Case #"<<test+1<<":"<<" "<<count<<endl;

	}
	return 0;
}
