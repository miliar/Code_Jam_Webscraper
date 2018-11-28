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

int N,t,tc;
double arr1[1005],arr2[1005];
bool chk1[1005],chk2[1005];

int main(){
	int i,j,k,a,b,ans1,ans2,lo,hi;
	S(t);
	for(tc=1;tc<=t;tc++){
		S(N);
		//cout<<"he";
		for(i=0;i<N;i++)
			scanf("%lf",&arr1[i]);
		for(i=0;i<N;i++)
			scanf("%lf",&arr2[i]);
		sort(arr1,arr1+N);
		sort(arr2,arr2+N);
		a=b=ans1=ans2=0;
		//memset(chk1,false,sizeof(chk1));
		memset(chk2,false,sizeof(chk2));
		for(i=0;i<N;i++){
			bool flag=false;
			for(j=0;j<N;j++)
				if(!chk2[j] && arr2[j]>arr1[i]){
					flag=true;
					break;
				}
			if(flag){
				chk2[j]=true;
				b++;
			}
		}
		ans1=0;
		ans2=N-b;
		memset(chk2,false,sizeof(chk2));
		for(i=0;i<N;i++){
			bool flag=false;
			for(j=N-1;j>=0;j--)
				if(!chk2[j] && arr2[j]<arr1[i]){
					flag=true;
					break;
				}
			if(flag){
				chk2[j]=true;
				ans1++;
			}
		}
		//ans1=max(ans1,ans2);
		printf("Case #%d: ",tc);
		P(ans1);
		SP;
		P(ans2);
		NL;	
	}

}