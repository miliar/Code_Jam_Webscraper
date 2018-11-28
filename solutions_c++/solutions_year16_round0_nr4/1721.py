#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>

#define f first
#define s second
#define pb push_back

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;


int main() 
{
	int t,i,j,k,c,s;
	
	freopen("input7.txt", "r", stdin);
	freopen("output7.txt", "w", stdout);

	scanf("%d",&t);
	
	for(i = 0;i < t;i++) {
		scanf("%d %d %d",&k,&c,&s);
		printf("Case #%d: ",i+1);
		for(j  = 1;j <= s;j++) {
			printf("%d ",j);
		}
		printf("\n");
	}
	return 0;	
	
}

