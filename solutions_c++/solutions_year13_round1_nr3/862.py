#include<algorithm>
#include<cmath>
#include<cstdio>
#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<queue>
#define pi 3.14159
using namespace std;

int main()
{
vector <int> v;
vector <int> v1;
int t,i,j,r,n,n1,m,k;
cin>>t;
cout<<"Case #"<<1<<":"<<" "<<"\n";
cin>>r>>n>>m>>k;
n1=n;
int a[k];
while(r!=0)
{
	for(j=0;j<k;j++)
	{
	cin>>a[j];
        v.push_back(a[j]);
	}
	sort(v.rbegin(),v.rend());
	for(i=m;i>=2;i--)
	{
	if(v[0]%i==0)
	{
        v[0]=v[0]/i;
	v1.push_back(i);
        if(v[0]%i==0)
         v1.push_back(i);
	n--;
	if(n==0)
	break;
	}
	}
        for(i=0;i<n1;i++)
         cout<<v1[i];        
	v1.clear();
        v.clear();
        r--;
        cout<<endl;
}
return 0;
}