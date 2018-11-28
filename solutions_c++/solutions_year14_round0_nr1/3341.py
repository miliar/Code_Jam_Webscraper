#include <iostream>
#include <algorithm>
#include <cmath>
#include <time.h>
#include <stdlib.h>
#include <string>
#include <string.h>
#include <queue>
#include <utility>
#include <vector>
#include <time.h>
#include <stdio.h>
#include <list>
#include <limits> // for numeric_limits
#include <set>
#include <iterator>
#include <memory.h>

using namespace std;

#define ff first
#define ss second
#define pb push_back
#define mp make_pair
#define var(a,b)  __typeof(b) a = b
#define rep(i,n)  for(int i = 0;(i) < (n);  ++i)
#define rept(i,a,b) for(var(i,a); i < (b); ++i)
#define tr(v,it)  for(var(it,v.begin());it!=v.end();++it)
#define fill(a,val) memset(a,val,sizeof(a))
#define gi(n) scanf("%d",&n);
#define all(v) v.begin(),v.end()
#define max(a,b) a>b?a:b
#define min(a,b) a>b?b:a
#define MOD 1000000007
#define INF 99999999
#define a_max 100100
#define ll long long int
#define debug_lld(a) printf("Debug here %lld\n",a);

typedef pair<ll,ll> pll;
typedef pair<int,int > pii;
typedef pair<ll,pii>plp;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		int choice1, choice2;
		int num;
		int arr1[4][4], arr2[4][4];
		int score=0;

		scanf("%d",&choice1);
		for(int j = 0; j<4; j++)
		{
			scanf("%d%d%d%d",&arr1[j][0], &arr1[j][1], &arr1[j][2], &arr1[j][3]);
		}
		
		scanf("%d",&choice2);
		for(int j = 0; j<4; j++)
		{
			scanf("%d%d%d%d",&arr2[j][0], &arr2[j][1], &arr2[j][2], &arr2[j][3]);
		}

		choice2--;
		choice1--;

		for(int j =0 ;j<4;j++){
			for(int k = 0; k<4; k++){
				if(arr1[choice1][j] == arr2[choice2][k]){
					num = arr2[choice2][k];
					score++;
				}
			}
		}
		printf("Case #%d: ",i+1);
		if(score==1){
			printf("%d\n",num);
		}
		else if(score==0){
			printf("Volunteer cheated!\n");
		}
		else
			printf("Bad Magician!\n");
	}
	return 0;
}