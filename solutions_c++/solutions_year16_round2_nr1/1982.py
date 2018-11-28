#include <stdio.h>
#include <algorithm>
#include <vector>
#include <string.h>
#include <queue>
#include <math.h>
#define SQ(a) ((a)*(a))
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<pii,int> piii;
typedef pair<double,double> pdd;

const int mod = 1000000007;
const int INF =2147483647;
char x[10][10]={"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
int TT;
int c[10][26];
int p[11]={0,2,6,8,3,4,5,1,7,9};
int main(){
	for(int i=0;i<10;i++){
		int ll=strlen(x[i]);
		for(int j=0;j<ll;j++){
			c[i][x[i][j]-'A']++;
		}
	}
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++){
		vector<int> v;
		int a[26];
		for(int i=0;i<26;i++){
			a[i]=0;
		}
		char s[2100];
		scanf("%s",s);
		int l=strlen(s);
		for(int i=0;i<l;i++){
			a[s[i]-'A']++;
		}

		for(int i=0;i<10;i++){
			int k=p[i];
			while(1){
				int t=1;
				for(int j=0;j<26;j++){
					if(a[j]<c[k][j]){
						t=0;
						break;
					}
				}
				if(t==0)break;
				for(int j=0;j<26;j++){
					a[j]-=c[k][j];
				}
				v.push_back(k);
			}
		}
		sort(v.begin(),v.end());

		printf("Case #%d: ",T);
		for(int i=0;i<v.size();i++){
			printf("%d",v[i]);
		}
		puts("");
	}
}