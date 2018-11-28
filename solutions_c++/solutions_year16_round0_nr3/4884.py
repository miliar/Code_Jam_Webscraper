#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
typedef long long ll;

ll primes[100000000];
ll cnt=0;

void sieve(ll n)
{
    ll i, j;
    for (i=0;i<n;i++)
        primes[i]=1; 
    primes[0]=0,primes[1]=0; 
    for (i=2;i<sqrt(n);i++) 
        for (j=i*i;j<n;j+=i) 
            primes[j] = 0;
}

int is_prime(int num)
{
     if (num <= 1) return 0;
     if (num ==2) return 1;
     for(int i = 3; i < floor(sqrt(num)); i+= 2)
     {
         if (num % i == 0)
             return 0;
     }
     return 1;
}


ll check(string s,int base)
{
	ll num=0;
	ll prev=1;
	for(int i=s.size()-1;i>=0;i--)
	{
		num+=((s[i]-'0')*prev); 
		prev*=base;
		//num%=MOD;
	}
	//cout<<num<<"number"<<endl;
	if(is_prime(num)==1) return 0;
	for(ll i=2;i<1000;i++)
	{
		if(num%i==0) return i;
	}
	return 0;
}

/*
int fun1(string s,int n)
{
	if(s.size()==n)
	{
		if(cnt==0) return -1;
		string tmp='1'+s+'1';
		ll buf[10]={0},ind=0;
		for(int i=2;i<10;i++)
		{
			ll temp=check(tmp,i);
			if(temp==0) return 0;
			buf[ind++]=temp;
		}
		cout<<tmp<<' ';
		for(int i=0;i<ind;i++)
			cout<<buf[i]<<' ';
		cout<<endl;
		cnt--;
		return 0;
	}
	if(fun(s+'0',n)==-1) return -1;
	if(fun(s+'1',n)==-1) return -1;
	return 0;
}*/

void fun(int n)
{
	time_t t;
	srand((unsigned) time(&t));
	string B="";
    {
        for(ll i = 0; i < pow(2,n) && cnt>0; i++)
        {
            B = "";
            int temp = rand()%65537;
            for (int j = 0; j < n; j++)
            {
                if (temp%2 == 1)
                    B = '1'+B;
                else
                    B = '0'+B;
                    temp = temp/2;
            }
            //cout<<B<<endl;
            string tmp='1'+B+'1';
			ll buf[10]={0},ind=0;
			for(int j=2;j<=10;j++)
			{
				ll temp1=check(tmp,j);
				if(temp1==0) goto as;
				buf[ind++]=temp1;
			}
			cout<<tmp<<' ';
			for(int j=0;j<ind;j++)
				cout<<buf[j]<<' ';
			cout<<endl;
			cnt--;
			as:;
         }
    } 
}
	
	



int main()
{
	//sieve(99999999);
	ll t;
	cin>>t;
	for(ll tt=1;tt<=t;tt++)
	{
		cout<<"Case #"<<tt<<": "<<endl;
		ll n,j;
		cin>>n>>j;
		cnt=j;
		string s="";
		fun(n-2);
	}
	return 0;
}
