#include<iostream>
#include<cstdio>
#include<cmath>
using namespace std;
int main()
{
    int t,k,i,j,c1,c2,arr[4][4],barr[4][4],count,ans[16],found,x;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        cin>>c1;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>arr[i][j];
            }    
        }
        
        cin>>c2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>barr[i][j];
            }    
        }        
        
        
        count=0;
        for(i=0;i<16;i++)
        ans[i]=0;
        
        for(i=0;i<4;i++)
        {
            x=arr[c1-1][i];
            ans[x-1]=1;
        }
        
        found=0;
       // for(i=0;i<16;i++)
        //cout<<ans[i];
        
        for(i=0;i<4;i++)
        {
            if(ans[(barr[c2-1][i])-1]==1)
            {
                found=1;
                count++;
                x=barr[c2-1][i];
            }    
        }
        //cout<<found<<"    "<<count;
                      
        cout<<"Case #"<<k<<": ";         
        if(found==0)
        cout<<"Volunteer cheated!\n";
        else if(count>1)
        cout<<"Bad magician!\n";
        else cout<<x<<endl;
    }    


return 0;
}
