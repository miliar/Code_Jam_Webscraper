#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
 long long t, k ,fre[10010], ankur=0, n, a[10010] ,r;
 freopen("op.txt","w",stdout);
 cin>>t;
 while(t--)
 {	
  r=0;
  cin>>n;
  for(long long i=0;i<=10010;i++)
  fre[i] = 0;
		
 for(long long i=1;i<=2*n-1;i++)
 {
  for(long long j=1;j<=n;j++)
  {
   long long x;
   cin>>x;
   fre[x]++;
  }
 }
		for(long long i=0;i<=10000;i++)
		{
			if(fre[i]%2==1)
				a[r++]=i;
		}
 	sort(a,a+r);
 	cout<<"Case #"<<++ankur<<": ";
 	for(long long i=0;i<r;i++)
 		cout<<a[i]<<" ";
 	cout<<endl;
	}

	
}
