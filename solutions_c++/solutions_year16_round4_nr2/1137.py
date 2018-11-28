#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <cmath>

using namespace std;

typedef long long ll;
int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};

#define in(x,y) ( (x)>=0 && (y)>=0 && (x)<n && (y)<m )
#define MOD 1000000007
#define INF 2147483647
#define PI 3.1415926535897932384626433832795
#define all(cont) cont.begin(),cont.end()
#define init(a,val) memset(a,val,sizeof(a))
#define F first
#define S second
#define mp make_pair
#define MAX 300


int main()
{
	freopen("b.in","r",stdin);
	//freopen("b.out","w",stdout);
	
	double yesp[MAX],b[MAX],maxval,totmax,ps[MAX];
	int n,k,ch,kbits,temp,i,j,ind;

//_______________________________________________
	int test_cases,tesT;

	cin>>test_cases;
	for(tesT=0;tesT<test_cases;tesT++){
		cout<<"Case #"<<tesT+1<<": ";
//_______________________________________________
		cin>>n>>k;
		

		for(i=0;i<n;i++){
			cin>>ps[i];
		}
		maxval=0;
		for(ch=0;ch<(1<<n);ch++){
			temp=ch;
			kbits=0;
			while(temp){
				kbits+=temp&1;
				temp>>=1;
			}
			if(kbits!=k)continue;

			temp=ch;
			yesp[0]=1.0;
			for(i=0,ind=0;i<n;i++){
				if(!(temp&(1<<i)))continue;

				for(j=0;j<=ind+1;j++)b[j]=0;
				for(j=0;j<=ind;j++){
					b[j]+=(1-ps[i])*yesp[j];
					b[j+1]+=ps[i]*yesp[j];
				}
				for(j=0;j<=ind+1;j++)yesp[j]=b[j];
				ind++;
			}
			maxval=max(yesp[k>>1],maxval);
		}
		printf("%.12f",maxval);

		

//_______________________________________________
		done:
		cout<<endl;
	}

	cerr<<endl;
	return 0;
}