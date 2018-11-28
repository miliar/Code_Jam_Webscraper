#include<iostream>
#include<set>
using namespace std;
int main()
{
	ios_base::sync_with_stdio(0);
	int t;
	cin>>t;
	int l=1;
	long long n,k,z;
	while(t--)
	{
		set<long long> s;
		cin>>n;
		 if(n>0)
		 {
		 
		 z=1;
		 while(1)
		 {
		 	k=z*n;
		 while(k>0)
		 {
		 	s.insert(k%10);
		 	k=k/10;
		 }
		 if(s.size()==10)
		 break;
		 else
		 z++;
		 }
		
		cout<<"Case #"<<l<<": "<<z*n<<"\n";
	    }
	    else
	    cout<<"Case #"<<l<<": "<<"INSOMNIA"<<"\n";
	    l++;
	    s.clear();
	    
	}
}

