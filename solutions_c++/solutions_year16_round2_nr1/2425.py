#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>

#define pb       	push_back
#define fi       	first
#define se       	second
#define inf		 	1000000000
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define yeral() (node *)calloc(1,sizeof(node))
#define dbg(x) cerr<<#x<<":"<<x<<endl

using namespace std;

typedef long long int lint;
typedef pair<int,int> ii;

lint n,a,b,c;
string ar[10] = {"ZERO", "ONE", "WTO", "RTHEE", "UFOR", "FIVE", "XSI", "SEVEN", "GEIHT", "INNE"};
int harf[30];
char s[2005];
int T,dig[15];
int main()
{
	
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	scanf("%d",&T);
	for(int t=1;t<=T;t++){
		
		for(int i= 0;i<26;i++)
			harf[i] = 0;
		for(int i= 0;i<10;i++)
			dig[i] = 0;
			
		scanf(" %s",s);
		int len = strlen(s);
		for(int i= 0;i<len;i++)
			harf[s[i]-'A']++;
		
		for(int j = 0;j<10;j+=2){
			dig[j] += harf[ar[j][0] - 'A'];
			for(int i = 1;i<ar[j].length();i++)
				harf[ar[j][i] - 'A'] -= harf[ar[j][0] - 'A'];
			
		}	
		
		for(int j = 1;j<10;j+=2){
			dig[j] += harf[ar[j][0] - 'A'];
			for(int i = 1;i<ar[j].length();i++)
				harf[ar[j][i] - 'A'] -= harf[ar[j][0] - 'A'];
			
		}	
		
		printf("Case #%d: ",t);
		for(int i= 0;i<10;i++)
			while(dig[i]--){
				printf("%d",i);	
			}
			
		puts("");
	}
}
