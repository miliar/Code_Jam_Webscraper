#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<cstdio>
#include<vector>
#include<map>
using namespace std;
 
#define MOD 1000000007
#define llu long long unsigned
#define lld long long
#define ld long
#define getchar_unlocked getchar
#define putchar_unlocked putchar
//end of definitions
 
 
//fast input
 
int scan_d()    {int ip=getchar_unlocked(),ret=0,flag=1;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
ld scan_ld()    {int ip=getchar_unlocked(),flag=1;ld ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
lld scan_lld()    {int ip=getchar_unlocked(),flag=1;lld ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked())if(ip=='-'){flag=-1;ip=getchar_unlocked();break;}for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return flag*ret;}
llu scan_llu()    {int ip=getchar_unlocked();llu ret=0;for(;ip<'0'||ip>'9';ip=getchar_unlocked());for(;ip>='0'&&ip<='9';ip=getchar_unlocked())ret=ret*10+ip-'0';return ret;}
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

lld getMid(lld s, lld e) {  return s + (e -s)/2;  }
 
lld getSumUtil(lld *st, lld ss, lld se, lld qs, lld qe, lld index)
{
   
    if (qs <= ss && qe >= se)
        return st[index];
    if (se < qs || ss > qe)
        return 0;
    lld mid = getMid(ss, se);
    return getSumUtil(st, ss, mid, qs, qe, 2*index+1) +
           getSumUtil(st, mid+1, se, qs, qe, 2*index+2);
}
 

void updateValueUtil(lld *st, lld ss, lld se, lld i, lld diff, lld index)
{
    if (i < ss || i > se)
        return;
 
    
    st[index] = st[index] + diff;
    if (se != ss)
    {
        lld mid = getMid(ss, se);
        updateValueUtil(st, ss, mid, i, diff, 2*index + 1);
        updateValueUtil(st, mid+1, se, i, diff, 2*index + 2);
    }
}
 

void updateValue(lld arr[], lld *st, lld n, lld i, lld new_val)
{
    
    if (i < 0 || i > n-1)
    {
        printf("Invalid Input");
        return;
    }
 
   
    lld diff = new_val;
 
    
    arr[i] = arr[i]+new_val;
 
    
    updateValueUtil(st, 0, n-1, i, diff, 0);
}
 

lld getSum(lld *st, lld n, lld qs, lld qe)
{
    
    if (qs < 0 || qe > n-1 || qs > qe)
    {
        printf("Invalid Input");
        return -1;
    }
 
    return getSumUtil(st, 0, n-1, qs, qe, 0);
}
 
lld constructSTUtil(lld arr[], lld ss, lld se, lld *st, lld si)
{
    
    if (ss == se)
    {
        st[si] = arr[ss];
        return arr[ss];
    }
 
    
    lld mid = getMid(ss, se);
    st[si] =  constructSTUtil(arr, ss, mid, st, si*2+1) +
              constructSTUtil(arr, mid+1, se, st, si*2+2);
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
long long int max (long long int i, long long int j) {
	if (i > j) {
		return i;
	}
	return j;
}

lld g(lld l,lld p)
{
 
    if(p==0)
       return l;
    else
       return g(p, l%p);
}
 
 long long pow(lld a, lld b, lld M)
{
    long long x=1,y=a; 
    while(b > 0)
    {
        if(b%2 == 1)
        {
            x=(x*y);
            if(x>M) x%=M;
        }
        y = (y*y);
        if(y>M) y%=M; 
        b /= 2;
    }
    return x;
}
 
int main ()
{
	long long int t,i,n,x,y,ans,j,a,b,c,k=1,m;
	cin>>t;
	string str;
	while(t--)
	{
		long long int arr[1005]={};
		cin>>n;
		int max=0;
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			if(arr[i]>max)
			max=arr[i];
		}
		long long int min=max;
		
	    for(i=1;i<max;i++)
	    {
	    	ans=i;
	    	for(j=0;j<n;j++)
	    	{
	    		if(arr[j]>i)
	    		{
	    			if(arr[j]%i==0)
	    			   ans+=(arr[j]/i-1);
	    			else
	    				ans+=(arr[j]/i);
	    		}
	    	}
	    	if(ans<min)
	    	{
	    		min=ans;
	    	}
	    }
		cout<<"Case #"<<k<<": "<<min<<endl;
		k++;
	}
	return 0;
}
