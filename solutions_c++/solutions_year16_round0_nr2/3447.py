#include <bits/stdc++.h>
using namespace std;

#define int long long
#define MOD 1000000007

char flip(char c){
	if(c=='+') return '-';
	return '+';
}
string s;
int calc(int l, int r, char c){
	if(l==r){
		if(s[l]==c) return 0;
		return 1;
	}
	if(l<r){
		if(s[r] == c){
			while(r>=l && s[r]==c) r--;
			if(r<l) return 0;
			return calc(l,r,c);
		}
		else{
			while(r>=l && s[r]!=c) r--;
			if(r<l) return 1;
			return calc(l,r,flip(c))+1;
		}
	}
	else{
		if(s[r] == c){
			while(r<=l && s[r]==c) r++;
			if(r>l) return 0;
			return calc(l,r,c);
		}
		else{
			while(r<=l && s[r]!=c) r++;
			if(r>l) return 1;
			return calc(l,r,flip(c))+1;
		}
	}
}

signed main(){
	freopen("a.txt","r",stdin);
	ios_base::sync_with_stdio(false);
	freopen("out.txt","w",stdout);
	cin.tie(0);
	int tt;
	cin >> tt;
	for(int t = 1;t<=tt;t++){
		cout << "Case #" << t << ": ";
		
		cin >> s;
		cout << calc(0,s.length()-1,'+') << "\n";
		continue;
		string r = s;
		reverse(r.begin(),r.end());
		int n = s.length();
		int d[n][n][2];
		int dd[n][n][2];
		for(int i=0;i<n;i++){
			d[i][i][0] = 1;
			d[i][i][1] = 1;
			if(s[i]=='-') d[i][i][0]=0;
			else d[i][i][1]=0;
		}
		for(int i=0;i<n;i++){
			dd[i][i][0] = 1;
			dd[i][i][1] = 1;
			if(r[i]=='-') dd[i][i][0]=0;
			else dd[i][i][1]=0;
		}
		for(int j=1;j<n;j++){
			for(int i=0;i+j<n;i++){
				for(int k=0;k<2;k++){
					d[i][i+j][k] = 1e9;
					for(int l=i;l<i+j;l++){
						d[i][i+j][k] = min(d[i][i+j][k],d[i][l][k]+dd[n-1-i-j][n-1-(l+1)][k]+2);
						if((i==0) && (j==(n-1))) cout << d[0][n-1][0] << " " << d[0][n-1][1] << " " << l << endl;
						if(dd[l+1][i+j][k]==0) d[i][i+j][k] = min(d[i][i+j][k],d[i][l][k]+dd[n-1-l-1][n-1-i-j][k]);
						d[i][i+j][k] = min(d[i][i+j][k],d[i][l][1-k]+dd[n-1-l-1][n-1-i-j][1-k]+1);
						if((i==0) && (j==(n-1))) cout << d[0][n-1][0] << " " << d[0][n-1][1] << " " << l << endl;
					}
					dd[i][i+j][k] = 1e9;
					for(int l=i;l<i+j;l++){
						dd[i][i+j][k] = min(dd[i][i+j][k],dd[i][l][k]+d[n-1-i-j][n-1-(l+1)][k]+2);
						if(d[l+1][i+j][k]==0) dd[i][i+j][k] = min(dd[i][i+j][k],dd[i][l][k]+d[n-1-l-1][n-1-i-j][k]);
						dd[i][i+j][k] = min(dd[i][i+j][k],dd[i][l][1-k]+d[n-1-l-1][n-1-i-j][1-k]+1);
					}
				}
			}
		}
		cout << d[0][n-1][1] << "\n";
	}
	
	return 0;
}
