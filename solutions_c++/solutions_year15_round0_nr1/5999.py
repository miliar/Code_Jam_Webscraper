#include <iostream>
using namespace std;

int countGuests(int smax,string s)
{
	int count=0;
	int n=0;
	int val;
	for(int i=0;i<smax+1;i++)
	{
		val=s[i]-48;
		if(i>count)
		{
			n+=(i-count);
			val+=(i-count);
		}
		if(val!=0)
			count+=val;
	}
	return n;
} 

int main()
{
    int cases, a,n=0; 
	string b;	            
	cin >> cases;                    
	for(int c=1; c<=cases; c++)      
	{
		cin >> a; cin >> b;                                 
		n = countGuests(a,b); 
		cout<<"Case #"<<c<<": "<<n<<endl;  
	}
    return 0;                        
}
