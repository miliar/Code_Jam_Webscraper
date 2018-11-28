#include<bits/stdc++.h>
using namespace std;

#define LL long long int
#define ULL unsigned long long int
#define MP make_pair
#define PB push_back
#define LD long double
#define MOD 1000000007

void input(){
	freopen("A-large.in","r",stdin);
   	freopen("A-large.out","w",stdout);
}




int main(){
input();
LL t,i,n,m,x,ans,a[10],ts=1,j;

cin>>t;
while(t--){
	cout<<"Case #"<<ts<<": ";ts++;
	cin>>n;
	if(n==0){
		cout<<"INSOMNIA"<<endl;
		continue;
	}

	for(i=0;i<10;i++) a[i]=0;
	j=1;
	while(j<1000005){
	
		m=j*n;
		ans=m;	
		while(m!=0){
			x=m%10;
			a[x]=1;
			m/=10;
		}
		j++;
		for(i=0;i<10;i++){
			if(a[i]==0) break;
		}
		if(i==10) break;
	}

	if(j>1000000)
	cout<<"INSOMNIA"<<endl;
	else
	cout<<ans<<endl;


}
		
		







	











return 0;
}
