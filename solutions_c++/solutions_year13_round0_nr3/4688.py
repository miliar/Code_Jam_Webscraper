#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <cmath>
using namespace std; 
int main()	
{
	freopen("C-large-1.in","r",stdin);
      freopen("C-large-1.out","w",stdout);
    int t;
    cin>>t;
    
	int a[41]={0,1,2,3,11,22,101,111,121,202,212,1001,1111,2002,
 10001,10101,10201,11011,11111,11211,20002,20102,
 100001,101101,110011,111111,200002,1000001,
 1001001,1002001,1010101,1011101,1012101,1100011,
 1101011,1102011,1110111,1111111,2000002,2001002};
 int cc=1;
	while(t--)
	{
	long long int min,max;
	cin>>min>>max;
	long int count=0;
	for(int i=0;i<42,pow(a[i],2)<=max;i++)
	{
		if(pow(a[i],2)>=min)
		count++;
		}
		
		cout<<"Case #"<<cc<<": "<<count<<endl;
		cc++;
 }
 
 return 0;
}
