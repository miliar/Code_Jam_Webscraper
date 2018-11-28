#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cmath>
#include <map>
#include <iterator>
using namespace std;

#define lli long long int
#define mod 1e9+7
#define f(i,x,n) for(i=0;i<n;i++)

int main()
{
	std::ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	int v;
	for(int v=1;v<=t;v++)
	{
	    cout<<"Case #"<<v<<": ";
	    int n,i;
	    cin>>n;
	    int a[n];
	    f(i,0,n)
	    {
	        cin>>a[i];
	    }
	    int maxm=a[0],index2=0,index=-1,max2=-1;
	   //cout<<"max"<<maxm<<" "<<max2<<endl;
	   for(i=0;i<n;i++)
	    {
	        if(maxm<a[i])
            {
                maxm=a[i];
                index2=i;
                // cout<<"maxm "<<maxm<<endl;
            }
	    }
	    for(i=0;i<n;i++)
	    {
	        if(max2<a[i] && a[i]<=maxm && i!=index2)
            {
                max2=a[i];
                // cout<<"max2 "<<max2<<endl;
                index=i;
            }
	    }
	   // cout<<maxm<<" "<<max2;
	    int diff=maxm-max2;
	    while(diff!=0)
	    {
	        if(diff%2!=0)
	        {
	            char ch=97+index2;
	            cout<<ch<<" ";
	            diff--;
	            a[index2]--;
	        }
	        else
	        {
	            char ch=97+index2;
	            cout<<ch<<ch<<" ";
	            diff-=2;
	            a[index2]-=2;
	        }
	    }
	    
	    for(i=0;i<n;i++)
	    {
	        if(i!=index && i!=index2)
	        {
	            while(a[i]!=0)
	            {
	            char ch=97+i;
	            cout<<ch<<" ";
	            a[i]--;
	                
	            }
	        }
	    }
	    int g=index2;
	    int h=index;
	    while(a[index2]!=0)
	    {
	        char c=97+g;
	        char ch=97+h;
	        cout<<c<<ch<<" ";
	        a[index2]--;
	    }
	    cout<<endl;
	}
	return 0;
}
