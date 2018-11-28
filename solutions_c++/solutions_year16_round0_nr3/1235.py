#include "stdio.h"
#include "math.h"
#include "cstdlib"
#include "iostream"
#include "complex"
#include "vector"
#include "algorithm"
#define Complex complex<long double>
#define lowbit(x) (((x)^(x-1))&(x))
using namespace std;
vector<vector<string> > d(11,vector<string>(33));
bool check(string s);
string conversion(string s,int b);
long long isprime(string x);
string increment(string s);
string addition(string a,string b);
string multiply(string a,string b);
vector<Complex> FFT_multiply(vector<Complex> &P,vector<Complex> &Q);
void FFT(vector<Complex> &A,int s);
bool mod(string s,int k);
string to_string(long long k);
string resizestr(string a,int sizex);
long long B=1000;
int D=3,t;
int main(){
    freopen("C-large.in","r",stdin);
    freopen("big_solutionxxx.txt","w",stdout);
    int n,k;
    scanf("%d",&n);
    scanf("%d %d",&n,&k);
    string s="1";
    string temp(n-2,'0');
    temp+="1";
    s+=temp;
    int countx=0;
    for(int i=2;i<=10;i++){
        d[i][0]="1";
        for(int j=1;j<=32;j++) d[i][j]=multiply(d[i][j-1],to_string(i));
    }
    printf("Case #1:\n");
    while(countx!=k){
        if(check(s)) countx++;
        do s=increment(s);
        while(s[s.length()-1]=='0');
    }
}
bool check(string s){
    vector<long long> ans;
    for(int i=2;i<=10;i++){
        long long temp=isprime(conversion(s,i));
        if(temp==-1) return false;
        ans.push_back(temp);
    }
    cout<<s<<" ";
    for(int i=0;i<ans.size();i++) printf("%lld ",ans[i]);
    printf("\n");
    return true;
}
string conversion(string s,int b){
    string ans="0";
    for(int i=0;i<s.length();i++){
        if(s[i]=='1') ans=addition(ans,d[b][s.length()-1-i]);
    }
    return ans;
}
long long isprime(string x){
    string k="1000000";
    long long limit=1000000;
    k=resizestr(k,max(k.length(),x.length()));
    x=resizestr(x,max(k.length(),x.length()));
    if(k.compare(x)>0) limit=atoll(x.data())-1;
    for(long long i=2;i<=limit;i++){
        if(mod(x,i)) return i;
    }
    return -1;
}
string increment(string s){
    for(int i=s.length()-1;i>=0;i--){
        if(s[i]=='0'){
            s[i]='1';
            break;
        }
        else s[i]='0';
    }
    return s;
}
string addition(string a,string b){
    a=resizestr(a,max(a.length(),b.length()));
    b=resizestr(b,max(a.length(),b.length()));
    string c;
    int r=0;
    for(int i=a.length()-1;i>=0;i--){
        c.insert(c.end(),((a[i]-'0')+(b[i]-'0')+r)%10+'0');
        r=((a[i]-'0')+(b[i]-'0')+r)/10;
    }
    reverse(c.begin(),c.end());
    if(r!=0){
        string temp;
        temp.insert(temp.begin(),r+'0');
        return temp+c;
    }
    else return c;
}
string multiply(string a,string b){
    vector<Complex> P,Q,ans;
    vector<long long> N;
    int len1=a.length();
    int len2=b.length();
    P.clear();
    Q.clear();
    int x;
    for(int i=len1-1;i>=0;i-=D){
        x=0;
        for(int j=D-1;j>=0;j--) if(i>=j) x=x*10+(a[i-j]-'0');
        P.push_back(Complex(x,0));
    }
    for(int i=len2-1;i>=0;i-=D){
        x=0;
        for(int j=D-1;j>=0;j--) if(i>=j) x=x*10+(b[i-j]-'0');
        Q.push_back(Complex(x,0));
    }
    ans=FFT_multiply(P,Q);
    int L=ans.size();
    N.clear();
    for(int i=0;i<L;i++) N.push_back((long long)round(real(ans[i])));
    while(L>1&&N[L-1]==0){
        N.pop_back();
        L--;
    }
    for(int i=0;i<L;i++){
        if(N[i]>=B){
            if(i==L-1){
                N.push_back(N[i]/B);
                L++;
            }
            else N[i+1]+=N[i]/B;
            N[i]%=B;
        }
    }
    string temp;
    for(int i=L-1;i>=0;i--){
        if(i<L-1){
            int d=0,aux=N[i];
            if(aux>0){
                while(aux>0){
                    aux/=10;
                    d++;
                }
            }
            else d=1;
            for(int j=d;j<D;j++) temp+="0";
        }
        temp+=to_string(N[i]);
    }
    return temp;
}
vector<Complex> FFT_multiply(vector<Complex> &P,vector<Complex> &Q){
    int n=P.size()+Q.size();
    while(n!=lowbit(n)) n+=lowbit(n);
    P.resize(n,0);
    Q.resize(n,0);
    FFT(P,1);
    FFT(Q,1);
    vector<Complex> R;
    for(int i=0;i<n;i++) R.push_back(P[i]*Q[i]);
    FFT(R,-1);
    return R;
}
void FFT(vector<Complex> &A,int s){
	int n=A.size(),p=0;
	while(n>1){
	    p++;
	    n/=2;
	}
	n=(1<<p);
	vector<Complex> a=A;
	for(int i=0;i<n;i++){
        int rev=0;
        for(int j=0;j<p;j++){
            rev*=2;
			rev|=((i>>j)&1);
        }
        A[i]=a[rev];
	}
	Complex w,wn;
	for(int i=1;i<=p;i++){
		int M=1<<i;
		int K=M>>1;
		wn=Complex(cos(s*2.0*M_PI/(double)M),sin(s*2.0*M_PI/(double)M));
		for(int j=0;j<n;j+=M){
			w=Complex(1.0,0.0);
			for(int l=j;l<K+j;l++){
				Complex t=w;
				t*=A[l+K];
				Complex u=A[l];
				A[l]+=t;
				u-=t;
				A[l+K]=u;
				w*=wn;
			}
		}
	}
	if(s==-1){
        for(int i=0;i<n;i++) A[i]/=(double)n;
    }
}
bool mod(string s,int k){
    int r=0;
    for(int i=0;i<s.length();i++) r=(r*10+(s[i]-'0'))%k;
    return r==0;
}
string to_string(long long k){
    string s;
    if(k==0) s.insert(s.end(),'0');
    else{
        while(k!=0){
            s.insert(s.end(),k%10+'0');
            k/=10;
        }
    }
    reverse(s.begin(),s.end());
    return s;
}
string resizestr(string a,int sizex){
    string temp(sizex-a.length(),'0');
    return temp+a;
}
