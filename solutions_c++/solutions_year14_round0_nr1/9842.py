#include <iostream>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main()
{
    int i,j,k1,k2,fl,l,t,test,lt,a[4][4],b[4][4];
    
    //freopen("A-small-practice.in","r",stdin);
    freopen("A-small-attempt3.in","r",stdin);
    freopen("ot.out","w",stdout);
    cin>>test;
           
    for(i=1; i<=test; i++)
    {
    	fl=0;
    	
    	cin>>k1;
    	for(j=0; j<4;j++)
    		for(l=0; l<4; l++)
    			cin>>a[j][l];
    		
    	
    	
    	cin>>k2;
    	for(j=0; j<4;j++)
    		for(l=0; l<4; l++)
    			cin>>b[j][l];
        
        k1--; k2--;
        
        for(j=0; j<4; j++)
        {
          for(l=0; l<4; l++)
		  {	
        	if(a[k1][j]==b[k2][l])
			{
				fl++;lt=a[k1][j];
			}
		  }
        }
        
        cout<<"Case #"<<i<<": ";
        if(fl==1) 
            cout<<lt<<endl;
        else if(fl==0)
    		cout<<"Volunteer cheated!\n";
    	else 
    		cout<<"Bad magician!\n";
    }
   
   
   

    return 0;
}
