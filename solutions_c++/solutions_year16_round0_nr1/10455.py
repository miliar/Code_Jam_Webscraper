#include <bits/stdc++.h>
using namespace std;
bool full(map<int,int> & map,int temp)
{
	
	while(temp)
	{
		map[temp%10]++;
		temp/=10;
	}
	for(int i=0;i<10;i++)
	if(!map[i])
		return false;
	return true;
}
int main()
{
	ofstream fout;
	fout.open("output.txt");
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		int n;
		cin>>n;
		if(n==0)
			cout<<"Case #"<<i+1<<": INSOMNIA\n";
		else{
			map<int,int>Map;
			int cunt=1;
			while(!full(Map,n*cunt))
				cunt++;
			cout<<"Case #"<<i+1<<": "<<n*cunt<<"\n";
		}		
		
	}
}
