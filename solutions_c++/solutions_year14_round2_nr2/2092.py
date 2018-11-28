# include <iostream>
# include <string.h>
# include <vector>
# include <utility>
# include <algorithm>
# include <sstream>
using namespace std;

int main()
{	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n_cases;cin>>n_cases;
	for(int id=0;id<n_cases;id++)
	{   int a,b,k;cin>>a>>b>>k;
	    int count=0;
	    for(int i=0;i<a;i++)
	        for(int j=0;j<b;j++)
	            if((i&j)<k)
	                count++;
		cout <<"Case #"<<id+1<<": "<<count<<endl;
	}
}
	        
