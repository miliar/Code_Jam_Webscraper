#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("inputlarge.txt","r",stdin);
	freopen("1L.txt","w",stdout);
	int t;
	cin >> t;
	int count=0;
	while(count<t)
	{
		map<int,int> m;
		count++;
		cout << "Case #" << count << ": ";  
		int n;
		cin >> n;
		bool flag=0;
		if(n==0)
			cout << "INSOMNIA" << endl;
		else
		{
			int val;
			int k=1;
			while(flag==0)
			{
				int tmp;
				val=k*n;
//				cout << val << endl;
				while(val>0)
				{
					tmp=val%10;
					val/=10;
					m[tmp]=1;
				}
				k++;
				if(m.size()>=10)
				{
					flag=1;
					break;
				}
				else
					flag=0;
			}
			cout << (k-1)*n << endl;
		}
		m.clear();
	}
	return 0;
}
