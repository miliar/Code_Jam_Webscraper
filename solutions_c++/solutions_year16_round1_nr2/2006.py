#include<bits/stdc++.h>
using namespace std;

int main()
{
    
    int t,n;
    
    cin>>t;
    for(int k=1;k<=t;k++)    
    	{
           cin>>n;
           int sz=2*n-1;
           int arr[sz][n];
            int fin[n*sz];
            for(int i=0,k=0;i<sz;i++)
            {
                for(int j=0;j<n;j++)
                    {
                        cin>>arr[i][j];
                        fin[k]=arr[i][j];
                        k++;
                    }
            }
            for(int w=0;w<n*sz;w+=n)
            {
                for(int idx=(w+n);idx<n*sz;idx+=n)
                {
                    if(fin[w]==fin[idx])
                    {
                        for(int x=w;x<(w+n);x++)
                        {
                            for(int y=idx;y<(idx+n);y++)
                            {
                                if(fin[x]==fin[y])
                                {
                                    fin[x]=-1;
                                    fin[y]=-1;
                                }
                            }
                        }
                    }
                }
            }
            for(int sd=0;sd<n*sz;sd++)
            {
                if(fin[sd]!=-1)
                for(int index=sd+1;index<n*sz;index++)
                {
                        if(fin[sd]==fin[index])
                        {
                            fin[sd]=-1;
                            fin[index]=-1;
                        }
                
                }
            }
            int ans[n],aidx=0;
             for(int sd=0;sd<n*sz;sd++)
             {
                 if(fin[sd]!=-1)
                 {
                     ans[aidx]=fin[sd];
                     aidx++;
                 }
             }
             cout<<endl;
             sort(ans,ans+n);
             cout<<"Case #"<<k<<": ";
             for(int pos=0;pos<n;pos++)
                cout<<ans[pos]<<" ";
                cout<<endl;
        }
  
	return 0;
}