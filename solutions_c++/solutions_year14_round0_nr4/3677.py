#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("D-large.in","r",stdin);
	freopen("aaout.txt","w",stdout);
	
	//std::ios_base::sync_with_stdio(false);
	int t,cnt,n,cc,i,j;
	cin >> t;
	cnt=0;
	float naomi[1010],ken[1010];
	
	while(t--)
	{
		cnt++;
		scanf("%d",&n);
		
		for(i=0;i<n;i++)
		cin >> naomi[i];
		 
		for(i=0;i<n;i++)
		 cin >> ken[i];
		 
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		
		
		cc=0;
		i=0,j=0;
		
		
		
		for(i = 0; i < n ; i++)
		{
			for(; j < n ;)
			{
				if( naomi[j++] < ken[i] )
				  cc++; 
				 else
				  break; 
			 }
		 }
         
         cout << "Case #" << cnt <<": " << n-cc;
         
         
         cc=0;
         
         for(i=0,j=0;j<n ; j++)
		 {	 
				 if(naomi[i] < ken[j] )
				  {
					  cc++;
					  i++;
				  }
				  
				 
		}	
				  
        cout << " " << n-cc << endl; 
         
      }
      
      return 0;
}         
              			 
			
		
		 
		  
		 
		 
		
		
	


