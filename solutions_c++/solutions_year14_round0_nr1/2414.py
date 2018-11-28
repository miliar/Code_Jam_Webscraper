#include <cstdio>
#include <algorithm>
#include <vector>
#include<iostream>
#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second
#define pb push_back

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;
const int MAXN = 100005;
void solve()
{
	vector<int> V,S;
	int a,b;
	scanf("%d",&a);
	fru(i,4)fru(j,4){
		scanf("%d",&b);
		if(i+1==a)V.pb(b);
	}
	scanf("%d",&a);
	fru(i,4)fru(j,4){
		scanf("%d",&b);
		if(i+1==a)
		{
			fru(h,4)if(V[h]==b)S.pb(b);
		}
	}
	if(S.size()==1)printf("%d\n",S[0]);
	else if(S.size()==0)printf("Volunteer cheated!\n");
	else printf("Bad magician!\n");
}
int main()
{
	int t;
	scanf("%d",&t);
	fru(i,t){printf("Case #%d: ",i+1);solve();}
    return 0;
}
