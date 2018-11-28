/* Sahil Sondhi : Don't check my solutions STALKER!*/
 

#include <iostream>
#include<vector>
#include<cmath>
#include <iomanip>
#include<string>
#include<algorithm>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<list>
#include<map>
#include<cctype>
#include<limits>

#define scan(x) scanf("%d",&x)
#define forall(i,x,n) for(int i=x;i<n;i++)
#define forequal(i,x,n) for(int i=x;i<=n;i++)
#define scanl(x) scanf("%ld", &x)
#define scanll(x) scanf("%lld", &x)
#define minimum(a,b) (a>=b?b:a)
#define maximum(a,b) (a<=b?b:a)
#define scanfloat(x) scanf("%f", &x)
#define mod 1000000009
#define swap(xxx,yyy) { xxx=xxx+yyy; yyy=xxx-yyy; xxx=xxx-yyy; }
#define MAXARRAY 730000
#define __gcd(a,b) gcd(a,b)
#define LL long long
#define LD long double


using namespace std;


int main()
{
	int t;
	int a[10],b[10],temp[10][10];
	int n1,n2;
	int count;
	int ans;
	cin>>t;
	
	for(int p=1;p<=t;p++) //test cases
	{	
		count=0;
		cin>>n1;
		n1--;
		
		
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		  cin>>temp[i][j];
		
		for(int i=0;i<4;i++)
		  a[i]=temp[n1][i];
		  
		cin>>n2;
		n2--;
		
		for(int i=0;i<4;i++)
		 for(int j=0;j<4;j++)
		  cin>>temp[i][j];
		
		for(int i=0;i<4;i++)
		  b[i]=temp[n2][i];
		  	
		for(int i=0;i<4;i++)
		  for(int j=0;j<4;j++)
		   if(a[i]==b[j])
		   { count++;
			 ans=a[i];
		   }	 
		   
		  cout<<"Case #"<<p<<": ";
		if(count==1)
			cout<<ans<<endl;
		else if (count>1)
			cout<<"Bad magician!"<<endl;
		else if (count == 0)
			cout<<"Volunteer cheated!"<<endl;
		  
		
	
	
	
	
	}
	

	
	return 0;
}