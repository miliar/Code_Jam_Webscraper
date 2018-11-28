#include<bits/stdc++.h>
using namespace std;
#define MAXN 2000005
#define mod 1000000007
#define ll long long
#define ull unsigned long long
ull gcd(ull a,ull b){
	ull r;
	while(1){
		r=a%b;
		if(r==0) return b;
		a=b;
		b=r;
	}
	return r;
}
ll inp[27];

int  main(){
    ll n,m,t;
	ll x,ca=1;
	string s;
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	
    cin>>t;
    ll ans[11];
    while(t--){
    	cin>>s;
    	//cout<<s[0]-'A'<<endl;
    	//cout<<s<<endl;
    	n = s.size();
    	for(int i=0;i<n;i++){
    		inp[s[i]-'A']++;
    	}
    	cout<<"Case #"<<ca<<": ";
    	ans[0] = min(inp[25],min(inp[4],min(inp[17],inp[14])));
    	inp[25]-=ans[0];
    	inp[4]-=ans[0];
    	inp[17]-=ans[0];
    	inp[14]-=ans[0];
    	while(ans[0]--) cout<<0;
    	
    	ans[2] = min(inp[19],min(inp[22],inp[14]));
    	inp[19]-=ans[2];
    	inp[22]-=ans[2];
    	inp[14]-=ans[2];
    	
    	ans[4] = min(inp[5],min(inp[14],min(inp[20],inp[17])));
    	
    	inp[5]-=ans[4];
    	inp[14]-=ans[4];
    	inp[20]-=ans[4];
    	inp[17]-=ans[4];
    	
    	ans[6] = min(inp[18],min(inp[8],inp[23]));
    	inp[18]-=ans[6];
    	inp[8]-=ans[6];
    	inp[23]-=ans[6];
    	
    	ans[8] = min(inp[4],min(inp[8],min(inp[6],min(inp[7],inp[19]))));
    	inp[4]-=ans[8];
    	inp[8]-=ans[8];
    	inp[6]-=ans[8];
    	inp[7]-=ans[8];
    	inp[19]-=ans[8];
    	
    	ans[5] = min(inp[5],min(inp[8],min(inp[21],inp[4])));
    	inp[5]-=ans[5];
    	inp[8]-=ans[5];
    	inp[21]-=ans[5];
    	inp[4]-=ans[5];
    	
    	ans[7] = min(inp[18],min(inp[4]/2,min(inp[21],inp[13])));
    	inp[18]-=ans[7];
    	inp[4]-=ans[7];
    	inp[4]-=ans[7];
    	inp[21]-=ans[7];
    	inp[13]-=ans[7];
    	
    	ans[3] = min(inp[19],min(inp[7],min(inp[17],inp[4]/2)));
    	inp[19]-=ans[3];
    	inp[7]-=ans[3];
    	inp[17]-=ans[3];
    	inp[4]-=ans[3];
    	inp[4]-=ans[3];
    
    	
    	ans[9] = min(inp[13]/2,min(inp[8],inp[4]));
    	inp[13]-=ans[9];
    	inp[13]-=ans[9];
    	inp[8]-=ans[9];
    	inp[4]-=ans[9];
    	
    	
    	ans[1] = min(inp[14],min(inp[13],inp[4]));
    	inp[14]-=ans[1];
    	inp[13]-=ans[1];
    	inp[4]-=ans[1];
    	while(ans[1]--) cout<<1;
    	while(ans[2]--) cout<<2;
    	while(ans[3]--) cout<<3;
    	while(ans[4]--) cout<<4;
    	while(ans[5]--) cout<<5;
    		while(ans[6]--) cout<<6;
    	while(ans[7]--) cout<<7;
    	while(ans[8]--) cout<<8;
    	while(ans[9]--) cout<<9;
    	cout<<endl;
    	ca++;
    	for(int i=0;i<27;i++) inp[i] = 0;
    }
    
    return 0;
}
