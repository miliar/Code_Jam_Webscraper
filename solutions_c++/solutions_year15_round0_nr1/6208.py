#include <bits/stdc++.h>
using namespace std;
#define FOR(i,n) for (int i = 0; i < (int)(n); ++i)
#define mod 1000000007
#define bigger(a,b) (a>b?a:b)
#define smaller(a,b) (a<b?a:b)
#define mem(A,g) memset(A,g,sizeof(A))
#define positive(a) (bigger(a,-a))
int chtoint(const char c)
{
    switch (c)
    {
    case '0':
    	return 0;
    case '1':
    	return 1;
    case '2':
    	return 2;
    case '3':
    	return 3;
    case '4':
    	return 4;
    case '5':
    	return 5;
    case '6':
    	return 6;
    case '7':
    	return 7;
    case '8':
    	return 8;
    case '9':
    	return 9;
    default:
    	return 0;
    }
}
int main() {
ios_base::sync_with_stdio(false); cin.tie(0);
int t;
cin>>t;
int y = t;
while(t--)
{
	int n;
	cin>>n;
	int B[n];
	long long sum = 0;
    char A[n];
    int count = 0;
    for(int i=0;i<=n;i++)
    {
    	cin>>A[i];
    	B[i] = chtoint(A[i]);
    }
    for(int i=0;i<=n;i++)
    {
    	sum += B[i];
    	if(sum<i+1)
    	{
    		count++;
    		sum+=1;
    	}
    }
    cout<<"Case #"<<y-t<<":"<<" "<<count<<"\n";
}
return 0;
}
