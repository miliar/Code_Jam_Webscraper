#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <utility>
using namespace std;

#define ll long long
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define mod 1000000007

int t;
int ra,rb;
int a[5][5],b[5][5];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("A-small-attempt0.out","w",stdout);
	cin>>t;
	for (int c=1;c<=t;c++){
		cin>>ra;
		for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++) cin>>a[i][j];
		cin>>rb;
		for (int i=1;i<=4;i++)
		for (int j=1;j<=4;j++) cin>>b[i][j];
		int ans=0;
		int card;
		printf("Case #%d: ",c);
		for (int i=1;i<=4 && ans<=1;i++)
		for (int j=1; j<=4 && ans<=1; j++)
		if (a[ra][i]==b[rb][j]) ans++, card=a[ra][i];
		if (ans>1) puts("Bad magician!");
		else if (ans==1) cout<<card<<endl;
		else puts("Volunteer cheated!");
	}	
}
