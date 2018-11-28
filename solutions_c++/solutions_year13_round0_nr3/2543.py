using namespace std;
#include<iostream>
#include<cstdio>
#include<cmath>
#include<string>
#include<cstring>
#include<vector>
#include<bitset>
#include<map>
#include<set>
#include<climits>
#include<algorithm>
#include<utility>
#include<cstdlib>
#include<cctype>
#include<queue>
#include<sstream>
#define read(x) scanf("%d",&x)
#define write(x) printf("%d\n",x)
#define assign(x,n) x=(int*)calloc(n,4)
#define rep(i,n) for(i=1;i<=n;++i)
#define max(a,b) ((a)>(b))?(a):(b)
typedef  long long int ull;

ull rev(ull n)
{
	ull rem=0;
	while(n)
	{
		rem=rem*10 +n%10;
		n/=10;
	}
	return rem;
}

int palin(ull n)
{
	return n%10 && rev(n)==n;
}

vector <ull> ans;

int count(ull a,ull b)
{
	int k=ans.size(),i,kk=0;
	for(i=0;i<k;i++)
	if(ans[i]>=a && ans[i]<=b)kk++;
	
	
	return kk;
}


int main()
{
	//freopen("in.txt","r",stdin);freopen("out.txt","w",stdout);
ull i,j,k;
int t;
ull a,b;

for(i=1;i*i<=100000000000000ll;i++)
{
	j=i*i;
	if(palin(i) && palin(j)){ans.push_back(j);
	              // cout<<j<<" "<<endl;
				   }
}
read(t);
int tt=1;
while(t--)
{
	cin>>a>>b;
	printf("Case #%d: %d\n",tt++,count(a,b));

}


}

