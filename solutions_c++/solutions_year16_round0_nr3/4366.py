#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
set<ll>myset;
int k,t;
ll n,temp,temp2;
void solve()
{
	 cin>>t;
	 k=1;
  while(t--)
  {
  		cin>>n;
  		temp=n;;
		if(n==0)
		{
  			cout<<"Case #"<<k<<": INSOMNIA\n";
  	     }
        else{
  		for(ll ct=1;;ct++)
  		{
  		  temp2=n;
  		  while(temp2>0)
		{
			myset.insert(temp2%10);
			temp2/=10;
		}

  		 if(myset.size() == 10)
			{
				cout<<"Case #"<<k<<": "<<n<<"\n";
				break;
			}

		else
			n=temp*ct;


		}
	}
	k+=1;
	myset.clear();
  }

}
int main()
{
  freopen("C:/Users/SHIVAM/Desktop/inp3.in","r",stdin);
   freopen("C:/Users/SHIVAM/Desktop/out3.txt","w",stdout);
   solve();
  return 0;
}



