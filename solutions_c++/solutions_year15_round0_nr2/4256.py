#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <vector>
#define INF (0XFFFFFFF)
using namespace std;

int a[2000];
int main (int argc, char *argv[])
{
	int noc;
	scanf("%d",&noc);
	for (int cs=1;cs<=noc;cs++){
		int n;
		scanf("%d",&n);
		for (int i=1;i<=n;i++){
			scanf("%d",&a[i]);
		}
		int ans=INF;
		for(int i=1;i<=1000;i++){
		    int x=i;
		    for(int j=1;j<=n;j++){
		    	if(a[j]>i){
					x+=a[j]/i;
				    if (a[j]%i==0)	x--;
				}
		    }
		    ans=min(ans,x);
		}
		cout<<"Case #"<<cs<<": "<<ans<<endl;
	}
	return 0;
}
