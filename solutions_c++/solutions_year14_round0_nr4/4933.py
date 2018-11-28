#include<iostream>
#include<vector>
#include<utility>
#include<limits.h>
#include<set>
#include<map>
#include<algorithm>
using namespace std;

int main()
{
	//freopen("outD.txt","w",stdout);
	int cases;
	cin>>cases;
	int ct=1;
	while(cases--)
	{
		int num;
		cin>>num;
		vector<double> n(num),k(num);
		int i=0;
		while(num--)
		cin>>n[i++];
		i=0;
		num=n.size();
		while(num--)
		cin>>k[i++];
		num=n.size();
		
		sort(n.begin(),n.end());
		sort(k.begin(),k.end());
		
		// for q2;
		int i2s=0,i2b=num-1;
		int i1=num-1;
		int q2=0;
		while(i1>=0)
		{
			if(n[i1]>k[i2b])
			{
				i1--;
				i2s++;
				q2++;
			}
			else
			{
				i1--;
				i2b--;
			}
		}
		
		//for q1
		int q1=0;
		i1=0;
		i2s=0,i2b=num-1;
		while(i1 < num)
		{
			if(n[i1] < k[i2b] && n[i1] < k[i2s])
			{
				i1++;
				i2b--;
			}
			else if(n[i1] < k[i2b] && n[i1] > k[i2s])
			{
				i2s++;
				i1++;
				q1++;
			}
			else
			{
				i2s++;
				q1++;
				i1++;
			}
		}
		
		cout<<"Case #"<<ct<<": "<<q1<<" "<<q2<<endl;
		ct++;
	}
	return 0;
}


