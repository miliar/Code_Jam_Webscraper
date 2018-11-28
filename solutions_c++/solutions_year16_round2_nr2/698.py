#include <bits/stdc++.h>
using namespace std;
#define ll long long

ll diff=-1,A=-1,B=-1;
bool flag;
int a[20],b[20],n;

void rec (int i=0, ll a1=0, ll b1=0){
	if(a1<b1)
		return;
	if(i==n){
		if(diff==-1 || diff>a1-b1){
			diff=a1-b1;
			A=a1,B=b1;
		}
		else if(diff==a1-b1 && a1<A)
			A=a1,B=b1;
	}
	else if(a[i]==-1 && b[i]==-1){
		if(a1>b1)
			rec(i+1,a1*10,b1*10+9);
		else{
			rec(i+1,a1*10,b1*10);
			rec(i+1,a1*10+1,b1*10);
		}
	}
	else if(a[i]==-1){
		if(a1>b1)
			rec(i+1,a1*10,b1*10+b[i]);
		else{
			rec(i+1,a1*10+b[i],b1*10+b[i]);
			if(b[i]<9)
				rec(i+1,a1*10+b[i]+1,b1*10+b[i]);
		}
	}
	else if(b[i]==-1){
		if(a1>b1)
			rec(i+1,a1*10+a[i],b1*10+9);
		else{
			rec(i+1,a1*10+a[i],b1*10+a[i]);
			if(a[i]>0)
				rec(i+1,a1*10+a[i],b1*10+a[i]-1);
		}
	}
	else if(a[i]<b[i] && a1==b1)
		return;
	else
		rec(i+1,a1*10+a[i],b1*10+b[i]);
}
ll fa,fb,fd;
void force(int i=0, ll a1=0, ll b1=0){
	if(i==n){
		ll f_df=max(a1,b1)-min(a1,b1);
		if(fd==-1 || fd>f_df){
			fd=f_df;
			fa=a1,fb=b1;
		}
		else if(fd==f_df && a1<fa)
			fa=a1,fb=b1;
		return;
	}
	for(int j=0;j<10;j++)
		for(int k=0;k<10;k++)
			if(a[i]==-1 || a[i]==j)
				if(b[i]==-1 || b[i]==k)
					force(i+1,a1*10+j,b1*10+k);
}

char s1[20],s2[20];

int main() {
	pair<ll, pair<ll,ll> > res[2];
	int tt,t,i;
	cin >>tt;
	for(t=1;t<=tt;t++) {
		cin >> s1>>s2;
		n=strlen(s1);
		for(i=0;i<n;i++){
			a[i]=(s1[i]=='?'?-1:(s1[i]-'0'));
			b[i]=(s2[i]=='?'?-1:(s2[i]-'0'));
		}

		fd=-1;
	//	force();
	//	printf("Case #%d: %0*lld %0*lld\n",t,n,fa,n,fb);
		flag=0;
		diff=-1;
		rec();
		res[0].first=diff,res[0].second.first=A,res[0].second.second=B;
		for(i=0;i<n;i++)
			swap(a[i],b[i]);
		swap(A,B);
		flag=1;
		diff=-1;
		rec();
		res[1].first=diff,res[1].second.second=A,res[1].second.first=B;
		sort(res,res+2);
		if(res[0].first<0)
			swap(res[0],res[1]);
		A=res[0].second.first;B=res[0].second.second;
		printf("Case #%d: %0*lld %0*lld\n",t,n,A,n,B);
		//fflush(stdout);
		for(i=n-1;i>=0;i--){
			if(a[i]!=-1 && a[i]!=(B%10))
				assert(0);
			B/=10;
			if(b[i]!=-1 && b[i]!=(A%10))
				assert(0);
			A/=10;
		}
	}
	return 0;
}