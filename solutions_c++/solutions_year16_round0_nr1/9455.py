#include <iostream>
#include<map>
#include<bits/stdc++.h>
using namespace std;
map<int,bool>m;
void upd(long long n)
{
 while(n!=0)
 {
     int r=n%10;
     m[r]=true;
     n/=10;
 }

}
int main() {
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
	long long t;
	cin>>t;
	for(long long  k=1;k<=t;k++)
	{

	long long i;
	cin>>i;

	cout<<"Case #"<<k<<": ";
	if(i==0)
	{
	    cout<<"INSOMNIA"<<endl;
	    continue;
	}
	    m.clear();
	    for(long long  j=1; ;j++)
	    {

	        upd(i*j);
	        if(m.size()==10)
	        {
	            cout<<i*j<<endl;
	            break;
	        }
	    }

	}
	return 0;
}
