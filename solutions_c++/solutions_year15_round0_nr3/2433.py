#include <bits/stdc++.h>
using namespace std;

int main()
{
	ifstream fin("inp3.in");
	ofstream fout("out3.txt");
	int tc;
	fin>>tc;
	for(int co = 1;co <= tc;co++)
	{
		int l,x;
		fin>>l>>x;
		string s;
		fin>>s;
		
		string p = s;
		int a[5][5] = {{0,0,0,0,0},
			       {0,1,2,3,4},
			       {0,2,-1,4,-3},
			       {0,3,-4,-1,2},
			       {0,4,3,-2,-1}};
		for(int i = 1;i < x;i++)
			s = s + p;
		//cout<<s<<endl;
	        int multi_f[l*x];
		multi_f[0] = s[0] - 'i' + 2;
       	       	int len = s.length();
		for(int i = 1;i < len;i++)
		{
			int value = a[abs(multi_f[i - 1])][s[i] - 'i' + 2];
			if(multi_f[i - 1] < 0)
				multi_f[i] = -1*value;
			else
				multi_f[i] = value;
		}
		int multi_b[l*x];
		//cout<<"1"<<endl;
		multi_b[l*x - 1] = s[len - 1] - 'i' + 2;
		//cout<<"1"<<endl;
		for(int i = len - 2;i >= 0;i--)
		{
			int value = a[s[i] - 'i' + 2][abs(multi_b[i + 1])];
			
		//	cout<<i<<endl;
			if(multi_b[i + 1] < 0)
				multi_b[i] = -1*value;
			else
				multi_b[i] = value;
		}
	//	cout<<"1"<<endl;
		int flag = 0;
		for(int i = 0;i <= len - 3;i++)
		{
			if(multi_f[i] == 2)
			{
				int value = s[i + 1] - 'i' + 2;
				if(value == 3)
				{
					if(multi_b[i + 2] == 4)
					{
						flag = 1;
						break;
					}
				}
				for(int j = i + 2;j <= len - 2;j++)
				{
					int temp = a[abs(value)][s[j] - 'i' + 2];
					if(value < 0)
						value = -1*temp;
					else
						value = temp;
					if(value == 3)
					{
						if(multi_b[j + 1] == 4)
						{
							flag = 1;
							break;
						}
					}
				}
			}
			if(flag == 1)
				break;
		}
	//	cout<<"1"<<endl;
	//	for(int i = 0;i < l*x;i++)
	///		cout<<multi_b[i]<<" ";
	//	cout<<endl;
	//	for(int i = 0;i < l*x;i++)
	//		cout<<multi_f[i]<<" ";
	//	cout<<endl;
		if(flag == 1)
			fout<<"Case #"<<co<<": "<<"YES"<<endl;
		else
			fout<<"Case #"<<co<<": "<<"NO"<<endl;
	}
}
