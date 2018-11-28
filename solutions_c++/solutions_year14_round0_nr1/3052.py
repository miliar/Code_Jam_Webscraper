#include <bits/stdc++.h>
using namespace std;

//DEFINITIONS

#define ll long long int
#define S(a) scanf("%d",&(a))
#define SL(a) scanf("%lld", &(a))
#define P(a) printf("%d",(a))
#define PL(a) printf("%lld",(a))
#define STR(a) scanf("%s",(a))
#define SP printf(" ")
#define NL printf("\n")
#define pb push_back
#define mp make_pair
#define MAX 100000005
#define mod 1000000007

int arr1[5][5],arr2[5][5];
vector<int> v1,v2,ans;

int main(){
	int t,x,y,tc,i,j;
	S(t);
	for(tc=1;tc<=t;tc++){
		S(x);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				S(arr1[i][j]);
				if(i==x)
					v1.pb(arr1[i][j]);
			}
		S(y);
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++){
				S(arr2[i][j]);
				if(i==y)
					v2.pb(arr2[i][j]);
			}
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				if(v1[i]==v2[j])
					ans.pb(v1[i]);
		printf("Case #%d: ",tc);
		j=ans.size();
		if(j==1)
			P(ans[0]);
		else if(!j)
			printf("Volunteer cheated!");
		else
			printf("Bad magician!");
		NL;
		v1.clear();
		v2.clear();
		ans.clear();
	}
}