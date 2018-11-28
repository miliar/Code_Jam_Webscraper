#include <cstdio>
#include <iostream>
#define fr(i,m,n) for(i=m;i<n;i++)
#define ifr(i,m,n) for(i=m;i>n;i--)
#define ll long long
#define sc scanf
#define pf printf
#define var(x) x i=0,j=0,k=0,tmp1=0,tmp2=0,tmp3=0,tmp=0,tmp4=0,tmp5=0,flag=0
#define pb push_back
#define vi vector<int>
#define vii vector<pair<int,int> >
#define vl vector<ll>
#define vll vector<pair<ll,ll> >
using namespace std;

string swapAndInv(string inp, int l, int r) {
	var(int);
	int N = inp.length();
	j=r;
	fr(i,l,r+1) {
		swap(inp[i],inp[j]);
		j--;
	}
	fr(i,l,r+1) {
		if(inp[i]=='-') inp[i]='+';
		else inp[i]='-';
	}
	return inp;
}

int main() {
	var(int);
	int T;
	string inp;
	sc("%d",&T);
	fr(k,0,T) {
		cin>>inp;
		int l,r,ans=0;
		l=0;
		r=inp.length()-1;
		while(r>=0) {
			if(inp[r]=='+') r--;
			else {
				if(inp[0]=='-') {
					inp = swapAndInv(inp,0,r);
					// cout<<inp<<endl;
					ans++;
				}
				else {
					while(inp[l]=='+') l++;
					inp = swapAndInv(inp,0,l-1);
					// cout<<inp<<endl;
					ans++;
					inp = swapAndInv(inp,0,r);
					// cout<<inp<<endl;
					ans++;
				}
			}
		}
		pf("Case #%d: %d\n",k+1,ans);
	}
	return 0;
}