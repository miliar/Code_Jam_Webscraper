#include<bits/stdc++.h>
using namespace std;
typedef pair<int,char> pii;
pii Array[26];
bool compare(const pair<int, int>&i, const pair<int, int>&j)
{
    return i.first > j.first;
}
int check()
{
	
	int count=0;
	for(int i=0;i<26;++i)
	{
		if(Array[i].first!=0)
		{
			count++;
			
		}	
	}
	return count;
}
void Solve(int K)
{
	printf("Case #%d: ",K);
	int N;
	int k1;
	for(int i=0;i<26;++i)
	{
		Array[i]=make_pair(0,char(65+i));
	}
	
	scanf("%d",&N);
	for(int i=0;i<N;++i)
	{
		scanf("%d",&k1);
		Array[i].first=k1;
	}
	
	//cout<<"MANIT"<<endl;
	int count=0;
	int one,two;
	sort(Array,Array+sizeof(Array)/sizeof *Array,compare);
	
	
	while(true)
	{
		k1=check();
		if(k1==0)
		{
			cout<<endl;
			return;
		}
		one=Array[0].first;
		two=Array[1].first;
		//cout<<k1<<one<<two<<endl;

		if(one-2 >= two )
		{
			cout<<Array[0].second<<Array[0].second<<" ";
			Array[0].first = Array[0].first-2;
		}	
		else if(k1>3)
		{
			cout<<Array[0].second<<Array[1].second<<" ";
			Array[0].first = Array[0].first-1;
			Array[1].first = Array[1].first-1;
		}
		else if(k1==3)
		{
			int three = Array[2].first;
			if(three < two)
			{
				cout<<Array[0].second<<Array[1].second<<" ";
				Array[0].first = Array[0].first-1;
				Array[1].first = Array[1].first-1;
			}
			else if(one > two)
			{
				cout<<Array[0].second<<Array[0].second<<" ";
				Array[0].first = Array[0].first-2;
			}	
			else
			{
				cout<<Array[0].second<<" ";
				Array[0].first = Array[0].first-1;
			}
		}
		if(k1==2)
		{
			cout<<Array[0].second<<Array[1].second<<" ";
			Array[0].first = Array[0].first-1;
			Array[1].first = Array[1].first-1;
		}
		sort(Array,Array+sizeof(Array)/sizeof *Array,compare);
	}
	return;
}
int main()
{
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;++i)
		Solve(i);
}