/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
 * Created By : Aditya Agarwal
 * IT, MNNIT-ALLAHABAD 
 * aditya.mnnit15@gmail.com
 _._._._._._._._._._._._._._._._._._._._._.*/


#include<bits/stdc++.h>
using namespace std;

#define MP make_pair
#define pb push_back
#define rep(i,n) for(int i=0;i<n;i++)
#define REP(i,a,b) for(int i=a;i<=b;i++)
#define PER(i,a,b) for(int i=b;i>=a;i--)
#define X first
#define Y second

 //i/o
#define inp(n) scanf("%d",&n)
#define inpl(n) scanf("%lld",&n)
#define inp2(n,m) inp(n), inp(m)
#define inp2l(n,m) inpl(n), inpl(m)


//cost
#define MOD 1000000007
#define MOD_INV 1000000006
#define MAX 100009
#define INF 999999999
#define mp make_pair
typedef long long ll;
typedef pair< pair<ll,ll>,ll > pairs;

int ans[1000010];
int main(){

	freopen("inp.in","r",stdin);
    freopen("oup.out","w",stdout);
    
	ans[0]=-1;
	for(int i=1;i<=1000000;++i){
		int val=i,k=1,j;
		int anss;
		int hash[10]={0};
		while(1){
			int temp=val*k;
			anss=temp;
			while(temp){
				hash[temp%10]++;
				temp/=10;
			}
			for(j=0;j<10;j++){
				if(hash[j]==0)
					break;
			}
			if(j==10)
				break;
			k++;
		}
		ans[i]=anss;
	}
	//cout<<"here "<<endl;
	int t,k=1;
	inp(t);
	while(t--){
		int n;
		inp(n);
		if(n>0)
        	printf("Case #%d: %d\n",k,ans[n]);
        else
        	printf("Case #%d: INSOMNIA\n",k);
        k++;
	}
	return 0;
}
