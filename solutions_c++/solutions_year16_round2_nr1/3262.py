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
	long long int t,n,dt,i,j,res,ans,a[100005],temp,mini,maxi,m,q,cnt[26];
	string s;
	cin>>t;
	dt=t;
	while(t--)
	{
	    for(i=0;i<26;i++)
	    cnt[i]=0;
	    cin>>s;
	    n=s.length();
	    for(i=0;i<n;i++)
	    {
	        cnt[s[i]-'A']++;
	    }
	    long long int zero=(cnt[25]);
	    if(zero!=0)
	    {
	        cnt[4]-=zero;
	        cnt[17]-=zero;
	        cnt[14]-=zero;
	    }
	    long long int two= cnt[22];
	    if(two)
	    {
	        cnt[19]-=two;
	        cnt[14]-=two;
	    }
	    long long int four=cnt[20];
	    if(four)
	    {
	        cnt[5]-=four;
	        cnt[14]-=four;
	        cnt[17]-=four;
	    }
	    long long int six=cnt[23];
	    if(six)
	    {
	        cnt[18]-=six;
	        cnt[8]-=six;
	    }
	    long long int eight=cnt[6];
	    if(eight)
	    {
	        cnt[4]-=eight;
	        cnt[8]-=eight;
	        cnt[7]-=eight;
	        cnt[19]-=eight;
	    }
	    long long int five=cnt[5];
	    if(five)
	    {
	        cnt[8]-=five;
	        cnt[21]-=five;
	        cnt[4]-=five;
	    }
	    cout<<"Case #"<<dt-t<<": ";
	    for(i=0;i<zero;i++)
	    cout<<"0";
	    for(i=0;i<cnt[14];i++)
	    cout<<"1";
	    for(i=0;i<two;i++)
	    cout<<"2";
	    for(i=0;i<cnt[17];i++)
	    cout<<"3";
	    for(i=0;i<four;i++)
	    cout<<"4";
	    for(i=0;i<cnt[5];i++)
	    cout<<"5";
	    for(i=0;i<six;i++)
	    cout<<"6";
	    for(i=0;i<cnt[21];i++)
	    cout<<"7";
	    for(i=0;i<eight;i++)
	    cout<<"8";
	    for(i=0;i<cnt[8];i++)
	    cout<<"9";
	    cout<<endl;
	    
	    
	}
	return 0;
}
