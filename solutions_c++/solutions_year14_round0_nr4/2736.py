#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;
int main(){
	int t,n;
	cin>>t;
	for (int it = 1; it <=t ; it++)
	{
		cin>>n;
		vector<double> a(n),b(n);
		for (int i = 0; i < n; i++)
		{
			cin>>a[i];			
		}
		for (int i = 0; i < n; i++)
		{
			cin>>b[i];
		}
		sort(a.begin(),a.end());
		sort(b.begin(),b.end());
		int war=0,dec=0,en=n-1,st;
		for (int i = n-1; i >=0; i--)
		{			
			if(a[i]>b[en]){
				war++;
			}
			else{
				en--;
			}
		}
		st=0;
		en=n-1;
		for (int i = n-1,j=0; i >=0; i--,j++)
		{		
			//cout<<a[j]<<" : "<<b[i]<<"\n";	
			if(a[j]>b[st]){
				dec++;
				st++;
			}	
			else{
				en--;
			}	
		}
		cout<<"Case #"<<it<<": "<<dec<<" "<<war<<endl;
		
	}
	
	return 0;
}

