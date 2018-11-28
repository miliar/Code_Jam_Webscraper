#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<utility>
#include<vector>
#include<stack>
#include<queue>
#include<deque>
#include<map>
#include<set>
#include<list>
#include<cstring>
#include<string>
#define mp make_pair
#define ff first
#define ss second
#define pb push_back
#define pf push_front
#define pob pop_back
#define pof pop_front
#define OO (int)2e9
#define INF (ll)9e18
#define ll long long
#define pii pair<int,int>
#define pll pair<ll,ll>
#define atasx(x,a,b,c) for(int x=a;x<=b;x+=c)
#define atas1(x,a,b) atasx(x,a,b,1)
#define bawahx(x,a,b,c) for(int x=a;x>=b;x-=c)
#define bawah1(x,a,b) bawahx(x,a,b,1)
using namespace std;
int tc,cek[16],input,temp;
void tanda (int input){
	while(input){
	if(!cek[input%10]){
		cek[input%10]=1;
		cek[11]++;
		}
	
	input/=10;
	}
}

int main()
{
	scanf("%d",&tc);
	atas1(k,1,tc){
		scanf("%d",&input);
		if(input>0){
		atas1(i,0,12)cek[i]=0;
			atas1(j,1,72){
				tanda(input*j);
				if(cek[11]==10){
					printf("Case #%d: %d\n",k,input*j);
					break;
					}
				}
			}
			else printf("Case #%d: INSOMNIA\n",k);
	}
	
	return 0;
}
