#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

int main()
{
     
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	
	int t,i,j=1;
	cin>>t;
	
	while(t--){
		int s_max;
		cin>>s_max;
		char a[s_max+1];
		cin>>a;
		
		
			
		int invite_friend=0,clap_guy=(a[0] -'0');
		for(i=1;i<s_max+1;i++)
		{
			if(a[i]!='0'){
			
			if(clap_guy>=i)
			{
				clap_guy+=(a[i])-'0';									
			}
			else{
				
				invite_friend+=i-clap_guy;
				clap_guy+=invite_friend+a[i]-'0';
															
			}					
		}
			
		}		
		
		cout<<"Case "<<"#"<<j<<": "<<invite_friend<<endl;
		j++;
		
	}
        
	
 return 0;
                        
}
