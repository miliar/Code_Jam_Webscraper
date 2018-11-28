#include <iostream>
#include <algorithm>
#include<set>
#define ll long long 
#define inf 99999999999999999
#define ninf -99999999999999999
using namespace std;
set <long long int> st;
long long int flag=0;
void findi(long long int n)
{
	while(n)
	{
		st.insert(n%10);
		n=n/10;
	}
	if(st.size()==10)
	flag=1;
}
int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int n,t,cases;
cin>>t;
cases=t;
while(t--)
{
	cin>>n;
	if(n==0)
	cout<<"Case #"<<cases-t<<": INSOMNIA\n";
	else
	{
		long long int i=1;
		flag=0;
		while(1)
		{
			findi(n*i);
			i++;
			if(flag==1)
			break;
		}
		cout<<"Case #"<<cases-t<<": "<<n*(i-1)<<endl;
	}
	st.clear();

}
	
}
