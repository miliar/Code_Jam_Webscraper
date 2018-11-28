#include<bits/stdc++.h>
using namespace std;
#define MAXN 200005
#define mod 1000000007
#define ll long long
#define ull unsigned long long
ll ans[55][11],J=1,j;
string str[55];
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
ll anyBasetoDecimal(ll num,ll b){
    ll rem,dec=0,base=1;
    while (num > 0)
    {
        rem = num % 10;
        dec = dec + rem * base;
        base = base * b;
        num = num / 10;
    }
    return dec;
}
ll stringtoDecimal(char s[],ll sz){
    //ll sz = s.size();
    ll num = 0,p = 1;
    for(int i=sz-1;i>=0;i--){
        num+=(s[i]-'0')*p;
        p*=10;
    }
    return num;
}
ll primeorNot(ll n){
    if(n%2 == 0)return 2;
    for(int i=3;i<=n/2;i+=2){
      if(n%i==0){
          return i;
      }
     if(i>10000000) return -1;
    }
    return 0;
}
void solve(char s[],ll ind,ll sz){
    if(ind<sz-1){
        s[ind] = '0';
        solve(s,ind+1,sz);
        //if(J == j+1) return;
        s[ind] = '1';
        solve(s,ind+1,sz);
    }
    else{
        if(J == j+1) return;
        ll num = stringtoDecimal(s,sz);
        ll flag = 0,temp;
        for(int i=2;i<=10;i++){
            temp = anyBasetoDecimal(num,i);
            
            ll tmp = primeorNot(temp);
            if(tmp == -1) return;
            else if(tmp) ans[J][i] = tmp,flag++;
            else{
                return;
            }
        }
        if(flag == 9){
            s[sz] = '\0';
            str[J] = s;
            //cout<<s<<endl;
            J++;
        } 

    }
}
int  main(){
    ll n,t,k,f,test = 1;
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	cin>>t;
    char s[20];
    //cout<<primeorNot(470184985873)<<endl;
    while(t--){
        cin>>n>>j;
        cout<<"Case #"<<test<<":"<<endl;
        s[0] = '1';
        s[n-1] = '1';
        solve(s,1,n);

        for(int i=1;i<=j;i++){
            cout<<str[i]<<" ";
            for(int k=2;k<=10;k++) cout<<ans[i][k]<<" ";
            cout<<endl;
        }
        test++;
    }
    
    return 0;
}
