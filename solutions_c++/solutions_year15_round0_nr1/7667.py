#include <iostream>
#include <string.h>
#include <stdio.h>
#include <bits/stdc++.h>
 

 
using namespace std;


 
int main()
{
 	ofstream fout;
 	fout.open("output.txt");
	std::ios_base::sync_with_stdio(false);
 
	int  t;
	cin>>t;
 
	for(int j=1;j<=t;++j)
	{
		int smax,ans=0,standing=0;

		string s;
		
		cin>>smax;
		cin>>s;
	
		for(int shy_level=0;shy_level<=smax;++shy_level)
		if(s[shy_level]!='0')
		{
			
			if(standing<shy_level )
				
			{
				ans+= 		shy_level-standing;
				standing+= 	(shy_level- '0')-(standing-'0');	
			}
			standing+=s[shy_level]- '0';

		}
								
		fout<<"Case #"<<j<<": "<<ans<<endl;
		
	}
			
 
}

 
