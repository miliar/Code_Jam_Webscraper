#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>

using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 120


int main()
{
	freopen("a.in","r",stdin);
	//freopen("a.out","w",stdout);
	
	int a[1010],v[1010],den[1010];
	int n,i,curr,ind,maxcir,lastind;
//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		cin>>n;
		for(i=1;i<=n;i++){
			cin>>a[i];
		}
		for(i=1;i<=n;i++){

		}
		maxcir=0;
		init(den,0);
		for(i=1;i<=n;i++){
			init(v,0);
			curr=i;
			ind=1;
			while(!v[curr]){
				v[curr]=ind;
				curr=a[curr];
				ind++;
			}
			if(v[curr]==ind-2)
				{
					den[a[curr]]=max(den[a[curr]],v[curr]);
				}
			maxcir=max(maxcir,ind-v[curr]);
		}
		int countt=0;
		for(i=1;i<=n;i++)countt+=den[i];
		cout<<max(maxcir,countt);
//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}