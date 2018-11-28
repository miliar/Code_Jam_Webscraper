#include <bits/stdc++.h>
using namespace std;

int main() {
	long long int k,j,x,t,td,n,m,i,a[100005],res[100005],start,end;
	string s;
	char ans[4000];
	cin>>t;
	td=t;
	while(t--)
	{
	    k=0;
	    memset(a,0,sizeof(a));
	    memset(res,0,sizeof(res));
	    cout<<"Case #"<<td-t<<": ";
	    cin>>n;
	    for(i=0;i<2*n-1;i++)
	    {
	        for(j=0;j<n;j++)
	        {
	            cin>>x;
	            a[x]++;
	        }
	        
	    }
	    //for(i=0;i<10;i++)
	    //cout<<a[i]<<" ";
	    //cout<<endl;
	    for(i=0;i<3000;i++)
	    {
	        if(a[i]%2==1)
	        res[k++]=i;
	    }
	    sort(res,res+k);
	    for(i=0;i<k;i++)
	    cout<<res[i]<<" ";
	    cout<<endl;
	}
	return 0;
}
