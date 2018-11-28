#include<bits/stdc++.h>

using namespace std ; 

int t , freq[11] ; 
long long n , step  ; 

void update(long long num )
{
	while(num)
	{
		freq[num%10]++ ; 
		num/=10 ; 
	}
}

bool check()
{
	for(int i=0;i<=9;i++)
		if(!freq[i])return false ; 
		
	return true ; 
}

int main()
{
	freopen("A-large.in","rt",stdin);
    freopen("A-large.out","wt",stdout);
    
	cin>>t ; 
	int cnt = 1 ;  
	while(t--)
	{
		cin>>n ; 
		memset(freq,0,sizeof freq) ; 
		step = 1 ; 
		if(!n){cout<<"Case #"<<cnt<<": INSOMNIA\n" ; cnt++ ; continue ; }
		while(!check())
		{
			update(n*step) ; 
			step++ ; 
		}
		step-- ; 
		printf("Case #%d: %lld\n",cnt , n*step) ;
		cnt++ ; 
	}
	return 0 ;
}
