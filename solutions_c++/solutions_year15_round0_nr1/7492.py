# include <iostream>
# include <algorithm>
# include <vector>
# include <string>
# include <fstream>
# include <sstream>
using namespace std;

int main()
{
	ifstream cin("input.in");ofstream cout("output.out");
	int n_cases;cin>>n_cases;
	for(int case_id=1;case_id<=n_cases;case_id++)
	{	int len;string arr;cin>>len>>arr;len++;
		int xyz[1111];xyz[0]=0;int additional=0;
		for(int i=1;i<len;i++)
		{	int temp=(arr[i-1]-'0')+xyz[i-1];
			if(temp<i)
			{	additional+=i-temp;
				temp=i;
			}
			xyz[i]=temp;
		}
		cout << "Case #"<<case_id<<": "<<additional << "\n";
	}
}
		
