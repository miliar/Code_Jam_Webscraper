#include <iostream>
#include <vector>
using namespace std;

int main() {
	// your code goes here
	int testcase;
	cin >> testcase;
	string s;
	getline(cin, s);
	for (int test = 1; test <= testcase; test++)
	{
		getline(cin,s);
		//cout <<"input:#"<<s<<"#"<<endl;
		int slen = s.length();
		int f[slen][2];
		f[0][0] = s[0] == '-' ? 0 : 1;//f[0-]
		f[0][1] = s[0] == '+' ? 0 : 1;//f[0+]
		int pre0 = s[0] == '-' ? 0 : -1;
		int pre1 = s[0] == '+' ? 0 : -1;
		//cout << "pre:"<< pre0 <<" " << pre1<<endl;
		for (int i = 1; i < slen; i++)
		{
			if (s[i] == '-')
			{
				f[i][0] = f[i-1][0];
				if (pre1 == -1)
				{
					f[i][1] = 1;
				}
				else
				{
					//cout <<"pre1:"<<f[pre1][0]<<endl;
					f[i][1] = f[pre1][0] + 1;
				}
			}
			else //s[i] = '+'
			{
				f[i][1] = f[i-1][1];
				if (pre0 == -1)
				{
					f[i][0] = 1;
				}
				else
				{
					//cout <<"pre0:"<<f[pre0][1]<<endl;
					f[i][0] = f[pre0][1] + 1;
				}
			}
			
			pre0 = s[i] == '-' ? i : pre0;
			pre1 = s[i] == '+' ? i : pre1;
			//cout << "pre:"<< pre0 <<" " << pre1<<endl;
			//cout<<"F["<<i<<"]="<<f[i][0]<<"--"<<f[i][1]<<endl;
		}
		cout <<"Case #" << test <<": "<<f[slen-1][1]<<endl;
	}
	return 0;
}