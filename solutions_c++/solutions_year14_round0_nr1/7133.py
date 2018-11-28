
#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define all(a)    a.begin(), a.end()
#define foreach(v, c)   for( typeof( (c).begin()) v = (c).begin();  v != (c).end(); ++v)
#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define fill(a,v) memset(a, v, sizeof a)
#define forall(i,a,b)               for(int i=a;i<b;i++)


inline int inp(){int n=0,s=1,c=getchar_unlocked();if(c=='-')s=-1;while(c<48)c=getchar_unlocked();while(c>47)n=(n<<3)+(n<<1)+c-'0',c=getchar_unlocked();return n*s;}

int main()
{
	int t;
	t=inp();
	for(int T=1;T<=t;T++){
		int ans1,ans2;
		ans1=inp();
		ans1--;
		int A[4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				int k=inp();
				if(i==ans1)
					A[j]=k;
			}
		}
		ans2=inp();
		ans2--;
		int B[4];
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				int k1=inp();
				if(i==ans2)
					B[j]=k1;
			}
		}
		vector<int>common;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(A[i]==B[j])
					common.push_back(A[i]);
			}
		}
		if(common.size()==1)
			cout<<"Case #"<<T<<": "<<common[0]<<endl;
		else if(common.size()==0)
			cout<<"Case #"<<T<<": "<<"Volunteer cheated!"<<endl;
		else if(common.size()>1)
			cout<<"Case #"<<T<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}
