#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<cstring>

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define VI vector<int>
#define PII pair<int,int>
#define st first
#define nd second
#define mp make_pair
#define pb push_back
#define max_n 10005
#define lint long long int

using namespace std;

lint gcd(lint a,lint b){
	return a%b==0 ? b : gcd(b,a%b);
}

int main(){
	int z; scanf("%d",&z);
	int casenr=0;
	while(z--){
		casenr++;
		printf("Case #%d: ",casenr);
		int n,x;
		scanf("%d%d",&n,&x);
		VI s;
		FOR(i,0,n){
			int a; scanf("%d",&a);
			s.pb(a);
		}
		sort(s.begin(),s.end());
		int wziete[max_n]; FOR(i,0,n) wziete[i] = 0;
		int ile = 0;
		int wzial = 0;
		if(n==1) printf("1\n");
		else{
			int pos1 = 0, pos2=n-1;
			while(wzial!=n){
				while(pos1<pos2 && s[pos1]+s[pos2]>x) pos2--;
				if(pos1>=pos2){
					FOR(i,0,n){
						if(!wziete[i]) {ile++; wzial++;}
					}
				}
				else{
					wziete[pos1] = 1;
					wziete[pos2] = 1;
					pos1++;
					pos2--;
					ile++;
					wzial+=2;
				}
			}
			printf("%d\n",ile);
		}

	}
	return 0;
}
  

