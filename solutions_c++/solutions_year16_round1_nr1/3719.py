#include <iostream>
#include <deque> 
#include<string.h>
using namespace std;

  
int main() {
  unsigned long long int t, n, m;
    cin >> t; 
    char a[1103];
    deque<char> ans ; 
	for (int i = 1; i <= t; ++i) 
	{
    	cin>>a;
    	int len = strlen(a);
    	ans.push_back(a[0]);
    	
		for(int j=1; j<len; j++)
		{
					char back = ans.back();
					if( a[j] >= back )
					{
						
						ans.push_back(a[j]);
					}
					else
					{
						ans.push_front(a[j]);
					}
		}	
    	cout << "Case #" << i << ": " ;
		while(!ans.empty())
		{
			cout<<ans.back();
			ans.pop_back();
		}
		cout<<endl;
    }
}
