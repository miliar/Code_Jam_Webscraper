#include <iostream>
#include <set>

using namespace std;

int main() {
	int t;
	long int n,i,tmp,j=0,number;
	cin>>t;
	while(t--)
	{
		cin>>n;
		j++;
		i = 2;
		set<int> ans;
		number = n;
		while (number > 0)
		{
			int digit = number%10;
    		number /= 10;
		    ans.insert(digit);
		}
		while(true)
		{
		    tmp = n*i;
		    i++;
		    if(tmp == n)
		    {
		    	cout<<"Case #"<<j<<": INSOMNIA"<<endl;
		    	break;
		    }
		    number = tmp;
		    while (number > 0)
			{
    			int digit = number%10;
    			number /= 10;
			    ans.insert(digit);
			}
			if(ans.size() ==10)
			{
				cout<<"Case #"<<j<<": "<<tmp<<endl;
		    	break;
			}
		}
	}
	return 0;
}