#include<iostream>
using namespace std;

int main()
{
	int t,i,j,ans,count,s;
	cin >> t;
	char str[1005];
	for(i=1;i<=t;i++)
	{
		cin >> s;
		cin >> str;
		j=1;
		count=str[0]-48;
		//cout << count;
		ans=0;
		while(str[j]!='\0')
		{
			if(j>count)
			{
				count++;
				ans++;
			}
			count+=str[j]-48;
			j++;
		}
		cout << "Case #" << i << ": " << ans  << endl;
	}
	return 0;
}