#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int count[26];
	char first , second;
	int t,n;
	cin>>t;
	int m = t;
	while(t--)
	{
		int sum = 0;
		cin>>n;
		int n1 = n;
		for(int i = 0; i < n; ++i)
		{
			cin>>count[i];
			sum+=count[i];
			if(count[i] == 0)
				n1--;
		}
		cout<<"Case #"<<m-t<<": ";
		while(n1!=0){
		int m1=0, m2=0;
		for(int i = 1; i < n; ++i)
		{
			if(count[i] > count[m1])
				m1 = i;
		}
		cout<<(char)('A' + m1);
		count[m1]--;
		if(count[m1] == 0) n1--;

		for(int i = 1; i < n; ++i)
		{
			if(count[i] > count[m2])
				m2 = i;
		}
		if(n1 != 2)
		{
			cout<<(char)('A'+m2);
			count[m2]--;
			if(count[m2] == 0) n1--;
		}
		else
		{
			if(count[m2] - 1 != 0)
			{
					cout<<(char)('A'+m2);
					count[m2]--;
					if(count[m2] == 0) n1--;		
			}
		}
		cout<<" ";
		}
		cout<<endl;
	}
	return 0;
}