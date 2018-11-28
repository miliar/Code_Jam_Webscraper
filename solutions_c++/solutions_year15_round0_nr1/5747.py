#include <iostream>
#include <cstdlib>
#include <array>
#include <string>
#include <cmath>
using namespace std;
int l(char c)
{
    return c-'0';
}
int main() {
    long long t;
    cin >> t;
    int q=t;
	while(t--)
	{
	    long long n,sum=0,p=0;
	    cin >> n;
	    string s;
	    cin >> s;
	    //cout << l(s.at(0));
	    for(long long i=0;i<=n;i++)
	    {
	        if(sum<i)
	        {
	        p=p+i-sum;
	        sum=i;
	        }
	        sum=sum+l(s.at(i));
	        
	    }
	    cout << "Case #"<<q-t<<": " <<p <<endl;
	}
	return 0;
}
