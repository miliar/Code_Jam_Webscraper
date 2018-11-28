/*
 * contest.cpp
 *
 *  Created on: May 7, 2016
 *      Author: natali
 */
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stdio.h>


using namespace std;

int check[1001];

int main()
{
	int T;
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	string res1,res2;
	string a,b;
	cin>>T;
	int n;
	int q;
	vector<pair<int,char> > data(26);
	for(int i=0; i<26; i++)
	{
		data[i].first=0;
		data[i].second=('A'+i);
	}
	pair<int,char> tmp;
	bool metia,naklebia;
	for(int t=1; t<=T; t++)
	{

		cin>>n;
		for(int i=0; i<n; i++)
		{
			cin>>data[i].first;
			//cout<<data[i].first<<" "<<data[i].second<<endl;
			check[data[i].first]++;
		}
		sort(data.rbegin(), data.rend());
		q=check[data[0].first];
		//cout<<"Q "<<q<<endl;
		cout<<"Case #"<<t<<": ";
		while(data[q-1].first>0)
		{
			if(q%2==1)
			{
				cout<<data[0].second<<" ";
				data[0].first--;
				for(int i=1; i<q; i+=2)
				{
					cout<<data[i].second<<data[i+1].second<<" ";
					data[i].first--;
					data[i+1].first--;
				}
			}
			else
			{
				for(int i=0; i<q; i+=2)
				{
					cout<<data[i].second<<data[i+1].second<<" ";
					data[i].first--;
					data[i+1].first--;
				}
			}
			if(q!=n)
			{
				//cout<<"here somehow\n";
				if(data[q-1].first==data[q].first)
				{
					q+=check[data[q].first];
				}
			}
		}
		cout<<endl;
		for(int i=0; i<26; i++)
		{
			data[i].first=0;
			data[i].second=('A'+i);
		}
		for(int i=0; i<1001; i++)
			check[i]=0;
	}
	return 0;
}




