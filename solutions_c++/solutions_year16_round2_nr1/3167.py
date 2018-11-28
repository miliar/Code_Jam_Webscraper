#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, x=0, b[10];
	cin >> t;
	while(t--)
	{
		x++;
		for(int j=0; j<15; j++)
			b[j]=0;
		string s;
		cin >> s;
		int l=s.length();
		for(int i=0; i<l; i++)
		{
			if(s[i]=='G')b[8]++;
			if(s[i]=='H')b[3]++;
			if(s[i]=='N')b[9]++;
			if(s[i]=='O')b[1]++;
			if(s[i]=='S')b[7]++;
			if(s[i]=='U')b[4]++;
			if(s[i]=='V')b[5]++;
			if(s[i]=='W')b[2]++;
			if(s[i]=='X')b[6]++;
			if(s[i]=='Z')b[0]++;
		}
		b[1]=b[1]-(b[0]+b[2]+b[4]);
		b[7]=b[7]-b[6];
		b[5]=b[5]-b[7];
		b[9]=(b[9]-(b[1]+b[7]))/2;
		b[3]=b[3]-b[8];
		cout << "Case #" << x << ": " ;
		for(int i=0; i<10; i++)
			for(int j=b[i]; j>0; j--)
				cout << i;
		/*for(int k=0; k<10; k++)
		{
			cout << b[k] << " ";
		}*/
		cout << "\n";
	}
	
	return 0;
}