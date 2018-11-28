#include<iostream>
#include <stdio.h>

using namespace std;

int main()
{
     freopen ("b.in","r",stdin);
     freopen ("b.sal","w",stdout);
     
     int n;
	
	cin>>n;
	
	for (int i = 0; i<n;i++)
	{
    
            int w,h;
            int grass[109][109], up[109], side[109];
            cin>>w>>h;
            cout<<"Case #"<<(i+1)<<": ";
            for (int j = 0; j <w; j ++)
            {
                up[j]  = 0;
                for (int k = 0; k <h; k ++)
                {
                    cin>>grass[j][k];
                    side[k]=0;
                }
            }
            
            for (int j = 0; j <w; j ++)
            {
                for (int k = 0; k <h; k ++)
                {
                     if (grass[j][k] > up[j])
                       up[j] = grass[j][k];
                    if (grass[j][k] > side[k])
                      side[k] = grass[j][k];
                }
            }
            bool posible = true;
            for (int j = 0; j <w; j ++)
            {
                for (int k = 0; k <h; k ++)
                { 
                     if (grass[j][k] < up[j] && grass[j][k]<side[k])
                         {
                             posible = false;
                             break; 
                          }
                }
            }
            
            if (posible == true)
            {
                cout<<"YES"<<endl;
                }else{  
                    cout<<"NO"<<endl;
                }
/*            for (int j = 0; j <w; j ++)
            {
                for (int k = 0; k <h; k ++)
                {
                    cout<<grass[j][k]<<" ";
                }
                cout<<endl;
            }*/
            
        }
}