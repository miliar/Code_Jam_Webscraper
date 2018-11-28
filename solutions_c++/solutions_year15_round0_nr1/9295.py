#include <iostream>
#include <string> 

using namespace std;

int main()
{
	int t,k,tmp,count,add;
	string c;
	cin >> t;
	
	for(int j=1;j<=t;j++)
	{
		cin >> k;
		cin >> c;
		count = 0;
		add = 0;
		for(int i=0;i<=k;i++)
		{
			tmp = c[i] - '0';
			
			if(count >= i){
				count += tmp;	
			}else{
				add += i -  count;
				count += i - count;
				count += tmp;	
			}
		}

		cout << "Case #" << j << ": " << add << endl;
	}	

	return 0;
}
