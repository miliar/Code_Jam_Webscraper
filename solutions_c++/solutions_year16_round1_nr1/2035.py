#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int l=1;l<=t;l++)
	{
		string s;
		cin >> s;
		char a[2*s.size()];
		a[(s.size())]='A';
		int i=0,j=0,k=(s.size());
		for(i=(s.size());j<s.size();j++)
		{
			if(s[j]>=a[k])
			{
				k--;
				a[k]=s[j];	
			}
			else
			{
				a[i]=s[j];
				i++;
			}
		}
		cout << "Case #" << l <<": ";
		for(int p=k;p<i;p++)
			cout << a[p];
		cout << endl;
	}
}
