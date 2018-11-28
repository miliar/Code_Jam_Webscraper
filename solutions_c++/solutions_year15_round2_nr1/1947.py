#include<iostream>
#include<algorithm>
#include<cmath>
#include<map>
#include<cstring>
#include<cstdio>
#include<stdbool.h>
#include<vector>
using namespace std;
 
#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long
 
//end of definitions
 
 
//fast input
 
int scan_d()    {int ip=getchar_unlocked(),ret=0,flag=1;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
ld scan_ld()    {int ip=getchar_unlocked(),flag=1;ld ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
lld scan_lld()    {int ip=getchar_unlocked(),flag=1;lld ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
llu scan_llu()    {int ip=getchar_unlocked();llu ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked());for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return ret;}
 
//end of fast input
 
//fast output
 
//no line break
void print_d(int n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=10;char output_buffer[10];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<10);}
void print_ld(ld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=11;char output_buffer[11];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<11);}
void print_lld(lld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<21);}
void print_llu(llu n)     {int i=21;char output_buffer[21];do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<21);}
 
//new line
void println_d(int n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=10;char output_buffer[11];output_buffer[10]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<11);}
void println_ld(ld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=11;char output_buffer[12];output_buffer[11]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<12);}
void println_lld(lld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=21;char output_buffer[22];output_buffer[21]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<22);}
void println_llu(llu n)     {int i=21;char output_buffer[22];output_buffer[21]='\n';do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<22);}
 
//special char
char sp;
void printsp_d(int n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=10;char output_buffer[11];output_buffer[10]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<11);}
void printsp_ld(ld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=11;char output_buffer[12];output_buffer[11]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<12);}
void printsp_lld(lld n)     {if(n<0){n=-n;putchar_unlocked('-');}int i=21;char output_buffer[22];output_buffer[21]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<22);}
void printsp_llu(llu n)     {int i=21;char output_buffer[22];output_buffer[21]=sp;do{output_buffer[--i]=(n%10)+'0';n/=10;}while(n);do{putchar_unlocked(output_buffer[i]);}while(++i<22);}
 
//end of fast output
 
lld pow(lld a, lld b, lld M) {
lld x = 1, y = a;
    while(b > 0) {
        if(b%2 == 1) {
            x=(x*y);
            if(x>M) x%=M;
        }
        y = (y*y);
        if(y>M) y%=M;
        b /= 2;
    }
    return x;
}
lld countSetBits(lld n)
{
    lld count = 0;
    while (n)
    {
      n &= (n-1) ;
      count++;
    }
    return count;
}
 string ip()
{
    string i="";
    int temp=getchar_unlocked();
    while(temp<'a'||temp>'z')
        temp=getchar_unlocked();
    while(temp>='a'&&temp<='z')
    {
        i+=(char)temp;
        temp=getchar_unlocked();
    }
    return i;
}
long long SmallC(lld n, lld r, lld M)
{
    vector< vector<long long> > C(2,vector<long long> (r+1,0));
 
    for (int i=0; i<=n; i++)
    {
        for (int k=0; k<=r && k<=i; k++)
            if (k==0 || k==i)
                C[i&1][k] = 1;
            else
                C[i&1][k] = (C[(i-1)&1][k-1] + C[(i-1)&1][k])%M;
    }
    return C[n&1][r];
}
 
long long Lucas(lld n, lld m, lld p)
{
    if (n==0 && m==0) return 1;
    lld ni = n % p;
    lld mi = m % p;
    if (mi>ni) return 0;
    return Lucas(n/p, m/p, p) * SmallC(ni, mi, p);
}
 
long long C(lld n, lld r, lld M)
{
    return Lucas(n, r, M);
}
lld g(lld l,lld p)
{
 
    if(p==0)
       return l;
    else
       return g(p, l%p);
}
bool is_perfect_cube(lld n) {
    lld root(round(cbrt(n)));
    return n == root * root * root;
}

lld minVal(lld x, lld y) { return (x < y)? x: y; }
 
lld getMid(lld s, lld e) {  return s + (e -s)/2;  }
 
lld RMQUtil(lld *st, lld ss, lld se, lld qs, lld qe, lld index)
{
    if (qs <= ss && qe >= se)
        return st[index];
    if (se < qs || ss > qe)
        return 1000000000000000;
 
    lld mid = getMid(ss, se);
    return minVal(RMQUtil(st, ss, mid, qs, qe, 2*index+1),
                  RMQUtil(st, mid+1, se, qs, qe, 2*index+2));
}
 
lld RMQ(lld *st, lld n, lld qs, lld qe)
{
   
    if (qs < 0 || qe > n-1 || qs > qe)
    {
        printf("Invalid Input");
        return -1;
    }
 
    return RMQUtil(st, 0, n-1, qs, qe, 0);
}
 
lld constructSTUtil(lld arr[], lld ss, lld se, lld *st, lld si)
{
    if (ss == se)
    {
        st[si] = arr[ss];
        return arr[ss];
    }
    lld mid = getMid(ss, se);
    st[si] =  minVal(constructSTUtil(arr, ss, mid, st, si*2+1),
                     constructSTUtil(arr, mid+1, se, st, si*2+2));
    return st[si];
}
 

lld *constructST(lld arr[], lld n)
{
    lld x = (lld)(ceil(log2(n)));
    lld max_size = 2*(lld)pow(2, x) - 1; 
    lld *st = new lld[max_size];
    constructSTUtil(arr, 0, n-1, st, 0);
 
  
    return st;
}
int isPrime(lld x) {
    lld s = sqrt(x);
    for (lld i = 2; i <= s; i++) {
        if (x % i == 0) {
            return 0;
        }
    }
    return 1;
}
void Num(lld x, lld & a, lld & b) {
    for (lld i = 2; i <= x / 2; i++) {
        if (isPrime(i) && isPrime(x - i)) {
            a = i;
            b = x - i;
            return;
        }
    }
}

bool isSubsetSum(long long int set[],long long int n, long long int sum)
{
    bool subset[sum+1][n+1];
    for (long long int i = 0; i <= n; i++)
      subset[0][i] = true;
    for (long long int i = 1; i <= sum; i++)
      subset[i][0] = false;
 
     for (long long int i = 1; i <= sum; i++)
     {
       for (long long int j = 1; j <= n; j++)
       {
         subset[i][j] = subset[i][j-1];
         if (i >= set[j-1])
           subset[i][j] = subset[i][j] || subset[i - set[j-1]][j-1];
       }
     }
     return subset[sum][n];
}

int dp[1000010];
 
void rev() {
	memset(dp,63,sizeof dp);
	dp[1] = 1;
	for(int i = 1; i < 1000000; ++i) {
		string tmp = to_string(i);
		reverse(tmp.begin(), tmp.end());
		int reverse =stoi(tmp);
		dp[i+1] =min(dp[i+1], dp[i] + 1);
		dp[reverse] =min(dp[reverse], dp[i] + 1);
	}
}
 
int main() {
	rev();
	int n;
	n=scan_d();
	int cas = 1;
	while(n--) {
		int num;
		num=scan_d();
		printf("Case #%d: %d\n", cas++, dp[num]);
	}
	return 0;
}