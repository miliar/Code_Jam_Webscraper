#include <bits/stdc++.h>
#define ll long long int
#define debug 0
#define pi 3.1415926535897
#define ff first
#define ss second
#define loop(a,b) for(a=0;a<b;a++)
#define test() while(t--)
 
using namespace std;
 

 
const ll N=1000005;
const ll MOD = 1000000007LL;
int phi[N];
ll sum[N],ans[N];
 
ll fact[1000006];
ll ifact[1000006];
ll power2[1000006];
 
inline ll powr (ll a, ll  b)
{
    if (b == 0)
        return 1;
    long long int x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x)%MOD;
    else
        return (((x*x)%MOD)*a)%MOD;
}
 
inline ll inv(ll x) {
  return powr(x, MOD - 2);
}
 
inline ll mulMod(ll a, ll b) {
  return (a%MOD * b%MOD) % MOD;
}
 
inline void process() {
  fact[0] = 1;
  power2[0] = 1;
  for(int i = 1; i < 100003; i++) {
    fact[i] = mulMod(fact[i - 1], i);
    power2[i] = mulMod(power2[i - 1], 2);
  }
  ifact[100002] = inv(fact[100002]);
  for(int i = 100002 - 1; i >= 0; i--) {
    ifact[i] = mulMod(ifact[i + 1], i + 1);
  }
}
 
inline ll ncr(ll n, ll r) {
  if(n < r) return 0;
  return mulMod(fact[n], mulMod(ifact[r], ifact[(n - r)]));
}
 
inline void calc()
{
    ll i,j;
    for(i=1;i<N;i++) phi[i]=i;
    for(i=2;i<N;i++){
        if(phi[i]==i){
            for(j=i;j<N;j+=i){
                phi[j]/=i;
                phi[j]*=i-1;
            }
        }
    }
     
    for(i=1;i<N;i++){
        for(j=i;j<N;j+=i){
            sum[j]=sum[j]+1LL*i*phi[j/i];
        }
    }
    for(i=1;i<N;i++) sum[i]-=i;
    ans[0]=0;
    for(i=1;i<N;i++){
        ans[i]=ans[i-1]+sum[i];
    }
}
 
inline long double power(ll a, ll b)
{
    if (b == 0)
        return 1;
    ll x = powr(a, b/2);
    if (b % 2 == 0)
        return (x*x);
    else
        return (((x*x))*a);
}
 
 
int main() {
	// your code goes here
	ios_base::sync_with_stdio(false);
	cin.tie(0),cout.tie(0);
	if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
ll t,j,flag,i,g,k,c;
	cin>>t;
	if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	g=0;
	while(t--)
	{
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    g++;
	    c=0;
	    char s[4000];
	   cout<<"Case #"<<g<<": ";
	   cin>>s;
	   if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	   int pos[strlen(s)+5];
	   if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	   int push1[strlen(s)+5];
	   if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    for(j=0;j<strlen(s);j++)
	    pos[j]=0;
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    int c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0,c10=0;
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    for(j=0;j<strlen(s);j++)
	    {
	        if(s[j]=='Z')
	        c1++;
	        if(s[j]=='X')
	        c2++;
	        if(s[j]=='G')
	        c3++;
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	        if(s[j]=='H')
	        c4++;
	        if(s[j]=='U')
	        c5++;
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	        if(s[j]=='W')
	        c6++;
	        if(s[j]=='F')
	        c7++;
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	        if(s[j]=='V')
	        c8++;
	        if(s[j]=='I')
	        c9++;
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	        if(s[j]=='O')
	        c10++;
	    }
	    char str2[]="SIX";
	    for(i=1;i<=c2;i++)
	    {
	        for(k=0;k<strlen(str2);k++)
	        {
	            for(j=0;j<strlen(s);j++){
	            if((str2[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;
	            }}
	        }
	    }
	    char str1[]="ZERO";
	    for(i=1;i<=c1;i++)
	    {
	        for(k=0;k<strlen(str1);k++)
	        {
	            for(j=0;j<strlen(s);j++){
	            if((str1[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	               break;
	            }}
	        }
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	     char str3[]="EIGHT";
	     if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    for(i=1;i<=c3;i++)
	    {
	        for(k=0;k<strlen(str3);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str3[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	               break;
	            }}
	        }
	        if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	     char str4[]="THREE";
	    for(i=1;i<=c4-c3;i++)
	    {
	        for(k=0;k<strlen(str4);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str4[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	               break;}
	            }
	        }
	    }
	    char str5[]="FOUR";
	    for(i=1;i<=c5;i++)
	    {
	        for(k=0;k<strlen(str5);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str5[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	     char str6[]="TWO";
	    for(i=1;i<=c6;i++)
	    {
	        for(k=0;k<strlen(str6);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str6[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	     char str7[]="FIVE";
	    for(i=1;i<=c7-c5;i++)
	    {
	        for(k=0;k<strlen(str7);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str7[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    char str8[]="SEVEN";
	    for(i=1;i<=c8-c7+c5;i++)
	    {
	        for(k=0;k<strlen(str8);k++)
	        {
	            for(j=0;j<strlen(s);j++){
	            if((str8[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	     char str9[]="NINE";
	    for(i=1;i<=c9-(c2+c3+c7-c5);i++)
	    {
	        for(k=0;k<strlen(str9);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str9[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	     char str10[]="ONE";
	    for(i=1;i<=c10-(c1+c5+c6);i++)
	    {
	        for(k=0;k<strlen(str10);k++)
	        {
	            if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	            for(j=0;j<strlen(s);j++){
	            if((str10[k]==s[j])&&(pos[j]==0))
	            { pos[j]=1;
	            // cout<<s[j];
	               break;}
	            }
	        }
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	    if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	   for(i=0;i<10;i++)
	   {
	       c=0;
	       if(i==0)
	       {
	           for(j=1;j<=c1;j++)
	           cout<<i;
	           continue;
	       }
	       else
	        if(i==6)
	       {
	           for(j=1;j<=c2;j++)
	           cout<<i;
	           continue;
	       }
	       else
	        if(i==8)
	       {
	           for(j=1;j<=c3;j++)
	           cout<<i;
	           if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	           continue;
	       }
	       else
	        if(i==3)
	       {
	           for(j=1;j<=c4-c3;j++)
	           cout<<i;
	           if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	           continue;
	       }
	       else
	       if(i==4)
	       {
	           for(j=1;j<=c5;j++)
	           cout<<i;
	           continue;
	       }
	       else
	       if(i==1)
	       {
	           for(j=1;j<=c10-(c1+c5+c6);j++)
	           cout<<i;
	           continue;
	       }
	        else
	       if(i==9)
	       {
	           for(j=1;j<=c9-(c2+c3+c7-c5);j++)
	           cout<<i;
	           continue;
	       }
	        else
	       if(i==7)
	       {
	           for(j=1;j<=c8-c7+c5;j++)
	           cout<<i;
	           if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	           continue;
	       }
	       else
	       if(i==5)
	       {
	           for(j=1;j<=c7-c5;j++)
	           cout<<i;
	           if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	           continue;
	       }
	        else
	       if(i==2)
	       {
	           for(j=1;j<=c6;j++)
	           cout<<i;
	           if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	           continue;
	       }
	      
	   }
	   if(debug)
	    {
	        for(int i=0;i<5;i++)
	        cout<<"ok\n";
	    }
	   
	    cout<<"\n";
	    
	}
	return 0;
}