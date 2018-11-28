#include<iostream>
#include<set>
#include <sstream>
#include<fstream>
#include <algorithm>
using namespace std;

int main() {
freopen("D-large.in","r",stdin);
freopen("sai4large.out","w",stdout);
long long int t, n,i,j,war,wdd;
	float array1[1000], array2[1000];
    cin>>t;
for(long long int test=1;test<=t;test++)
{
		cin>>n;
		for(i=0;i<n;++i)
		cin>>array1[i];
		for(i=0;i<n;++i)
		cin>>array2[i];
		sort(array1,array1+n);
		sort(array2,array2+n);
		i=0,j=0;
		wdd=0;
		while(i<n)
		{
		if(array1[i]>array2[j])
		{
							j++;
				wdd++;
			}
			i++;
		}
		
		i=0,j=0;
		war=0;
		while(i<n)
		{
			if(j==n) 
			break;
			if(array1[i]<array2[j])
			{
				war--;
				i++;
			}
			j++;
		}
		war+=n;
		cout<<"Case #"<<test<<": "<<wdd<<" "<<war<<endl;
	}
	return 0;
}
