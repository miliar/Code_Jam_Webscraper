#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<time.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
#define ull long long
ull BigMod(ull B,ull P,ull M){  ull R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define MAX 10000000 // maximum of primes upto to generate
#define MAXH MAX/2

ull pwr[15][20];
map<ull,ull>MP[10];
char pr[MAX/16+10];
vector<ull>primes;
void seive()
{
	int lim = (int)sqrt(MAX),i,j;
	for ( i = 3; i <= lim; i += 2){
		if ( !(pr[i>>4]&(1<<( (i>>1)&0x7))) )
		{
			for (j = i*i/2; j <= MAXH; j+=i) pr[j>>3] |= (1<<(j&0x7));
		}
	}
}

int isprime(int n)
{
	if ( n < 2) return 0;
	if ( n == 2) return 1;
	if ( n%2 == 0) return 0;
	if ( !(pr[n>>4]&(1<<( (n>>1)&0x7))) ) return 1;
	return 0;
}
void prepow()
{
    seive();
    primes.push_back(2);
    for(ull i=3;i<=MAX;i+=2){
        if(isprime(i))
            primes.push_back(i);
    }
    for(ull i=2;i<=10;i++){
        pwr[i][0]=1;
        pwr[i][1]=i;
    }

    for(ull i=2;i<=10;i++){
        ull nm=i;
        for(ull j=1;j<=16;j++){
            pwr[i][j]=nm;
            nm=nm*i;
        }
    }
}

ull factorize(ull a){
    if(a%2==0)return 2;
    for(int i=3;i<=sqrt(a);i++){
        if(a%i==0)return i;
    }
    return -1;

    if(a<=MAX && isprime(a))return -1;
    for(int i=0;i<primes.size();i++){
        if(primes[i]>sqrt(a))return -1;
        if(a%primes[i]==0)return primes[i];
    }
    return -1;
}

ull factorize2(string num,ull B){

    ull S=MAX;
    bool brk=0;
    if(num.size()<=16){
        S=0;
        for(int i=0;i<num.size();i++){
                if(num[i]=='0')continue;
                else{
                    S=S+pwr[B][i];
                }
        }
        S=sqrt(S);
    }
    for(int j=0;j<=primes.size();j++){
        if(primes[j]>min(S,1000000ll))return -1;
        if(primes[j]==S*S)continue;
//        cout<<primes.size()<<" "<<j<<endl;
        ull bmres=0;
        for(int i=0;i<num.size();i++){
            if(num[i]=='1')
            bmres=(bmres%primes[j]+BigMod(B,i,primes[j])%primes[j])%primes[j];
        }
        if(bmres==0)return primes[j];
    }
    return -1;
}
ull len;
int totalcnt;
int koyta;
void gen(ull pos,string str){
    if(totalcnt==koyta)return;
    if(pos==len+1){
        ull sum[20];
        memset(sum,0,sizeof(sum));
        for(int i=0;i<len;i++){
            if(str[i]=='0')continue;
            else{
                for(int j=2;j<=10;j++){
                    sum[j]=sum[j]+pwr[j][i];
                }
            }
        }
        ull fac[20];
        bool hobena=0;
        for(int i=2;i<=10;i++){
//            cout<<str<<" "<<sum[i]<<" ";cout<<endl;
            fac[i]=factorize2(str,i);
//            ull f2=factorize2(str,i);
//            if(fac[i]!=f2)cout<<"MILENAI "<<str<<" "<<i<<" "<<sum[i]<<" "<<fac[i]<<" "<<f2<<endl;
            if(fac[i]==-1){
                hobena=1;
                break;
            }

        }
        if(hobena==0){
            reverse(str.begin(),str.end());
            cout<<str;
            for(int i=2;i<=10;i++)
                cout<<" "<<fac[i];
            cout<<endl;
            totalcnt++;
        }

        return;
    }
    else if(pos==1 || pos==len){
        string nstr=str+"1";
        gen(pos+1,nstr);
    }
    else{
        string nstr=str+"0";
        gen(pos+1,nstr);

        nstr=str+"1";
        gen(pos+1,nstr);
    }
}

int main()
{
    in("in.txt");
    out("out.txt");
     int t,n,caseno=1;
    prepow();
    cin>>t;
    cin>>len>>koyta;
    ull num[20];
    ull sum[20];
    string str;
    memset(sum,0,sizeof(sum));
    cout<<"Case #"<<t<<":"<<endl;;
    gen(1,str);

//    scanf("%d",&t);
//    while(t--){
//        printf("Case %d: ",caseno++);
//    }
    return 0;
}
