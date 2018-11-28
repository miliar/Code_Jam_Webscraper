
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
		double c,f,x;
		cin>>c>>f>>x;
		double time_added=c/2;
		double count=2+f;
		double final_ans;
		double ans1=x/2;
		while(1){
			double ans=time_added+(x/count);
//				cout<<"Outer"<<ans<<" "<<ans1<<endl;

			if(ans>=ans1)
			{final_ans=ans1;break;}
			if(ans<ans1){
//				cout<<ans<<" "<<ans1<<endl;
				ans1=ans;
				time_added=time_added+(c/count);
				count=count+f;
			}
		}
		printf("Case #%d: %.7lf\n",T,final_ans);
	}
	return 0;
}
