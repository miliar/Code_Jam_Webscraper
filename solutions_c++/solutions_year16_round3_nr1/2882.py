#include <bits/stdc++.h>
using namespace std;

long long int gcd (long long int a,long long int b )
{
  long long int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}


long long int power(long long int x,long long int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}

int main() {
    char chr[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','0','P','Q','R','S','T','U','V','W','X','Y','Z'};
	long long int t,n,dt,i,j,res,ans,a[100005],temp,mini,max1,max2,m,q,cnt[26],sum,pos1,pos2,posi,maxi;
	string s;
	cin>>t;
	dt=t;
	while(t--)
	{
	    cout<<"Case #"<<dt-t<<": ";
	    for(i=0;i<26;i++)
	    cnt[i]=0;
	    cin>>n;
	    sum=0;
	    for(i=0;i<n;i++)
	    {
	        cin>>cnt[i];
	        sum+=cnt[i];
	    }
	    if(sum%2==1)
	    {
	        maxi=-1;
	        for(i=0;i<26;i++)
	        {
	            if(maxi<cnt[i])
	            {
	                maxi=cnt[i];
	                posi=i;
	            }
	        }
	        //cout<<maxi<<endl;
	        cout<<chr[posi]<<" ";
	        cnt[posi]-=1;
	        sum-=1;
	    }
	    //cout<<"here"<<endl;
	    while(sum>0)
	    {
	        max1=max2=-1;
	        for(i=0;i<26;i++)
	        {
	            if(max1 < cnt[i])
	            {
                    max2 = max1;
                    pos2 = pos1;
                    max1 = cnt[i];
                    pos1 = i;
                } 
                else if(max2 < cnt[i])
                {
                    max2 = cnt[i];
                    pos2 = i;
                }
	        }
	        cnt[pos1]-=1;
	        cnt[pos2]-=1;
	        sum-=2;
	        cout<<chr[pos1]<<chr[pos2]<<" ";
	    }
	    cout<<endl;
	    
	}
	return 0;
}
