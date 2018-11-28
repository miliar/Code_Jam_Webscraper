#include<bits/stdc++.h>

using namespace std ; 

string str ; 

bool isBlank()
{
	int sz = str.size() ; 
	for(int i=0;i<sz;i++)
		if(str[i]=='+')return false ; 
	
	return true ; 
}

int main()
{
	freopen("B-large.in","rt",stdin);
    freopen("B-large.out","wt",stdout);
	int t , cnt = 1   ; 
	cin>>t ;  
	
	while(t--)
	{
		cin>>str ;
		int sz = str.size() ;
		if(isBlank()){printf("Case #%d: 1\n",cnt ) ; cnt++ ; continue ; }
		long long ans = 0 ;  
		for(int i=0;i<sz-1;i++)
		{
			if(str[i]=='+'){
				if(str[i+1]=='-'){
					while(str[i+1]=='-' && i<sz-1){
						str[i+1] = '+' ; 
						i++ ; 
					}
					ans+=2 ; 
				}
			}
			else
			{
				if(str[i+1]=='+'){
					str[i] = '+' ; 
					ans++ ; 
				}
				else
				{
					while(str[i+1]=='-' && i<sz-1){
						str[i+1] = '+' ; 
						i++ ; 
					}
					ans++ ; 
				}
				
			}
		}
		printf("Case #%d: %lld\n",cnt , ans) ;
		
		cnt++ ; 
	}
}
