#include <iostream>
#include<cstdio>
#include<cstring>
#include<string>
#include<set>
#include<map>
#include<list>
#include<array>
#include<algorithm>
using namespace std;
array< int,2505 > a = {};
list<int> l;
list<int>::iterator it;
int main() {
	// your code goes here
	int t;
	scanf("%d",&t);
	for(int k=1;k<=t;k++)
	{
		l.clear();
		cout<<"Case #"<<k<<": ";
		int n,num;
		cin>>n;
		a.fill(0);
		for(int i=0;i<2*n-1;i++)
		{
			//fill(a[i].begin();a[i].end();0);
			for(int j=0;j<n;j++)
			{
				cin>>num;
				a[num]+=1;
			}
		}
		for(int i=1;i<=2500;i++)
		{
			if(a[i]%2)
				l.push_back(i);
		}
		//l.sort();
		for(it=l.begin();it!=l.end();it++)
			cout<<*it<<" ";
		cout<<"\n";	
			
	}	
	//sort(a.begin(),a.begin()+2*n-1);
	return 0;
}