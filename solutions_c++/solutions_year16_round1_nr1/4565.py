#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("Input.in", "r", stdin);
	freopen("Output.out", "w", stdout);
	int i, t;
	cin >> t;

	for(i=1; i<=t; i++)
	{
		int j, k;
		string s, temp = "";
		cin >> s;

		if(s.size() == 1)
			cout << "Case #" << i << ": " << s << endl;
		else
		{
			stack<string> s1;
			stack<string> s2;
			
			temp += s[0];
			temp += s[1];
			s1.push(temp);

			temp = "";
			temp += s[1];
			temp += s[0]; 	
			s1.push(temp);

			
			for(j=2; j<s.size(); j++)
			{
				while(!s1.empty())
				{
					temp = s1.top();
					temp = temp + s[j];
					s2.push(temp);

					temp = s1.top();
					temp =s[j] + temp;
					s2.push(temp);
					s1.pop();
				}

				while(!s2.empty())
				{
					s1.push(s2.top());
					s2.pop();
				}
			}

			string ans[100000];
			int size = s1.size();

			for(j=0; j<size; j++)
			{
				ans[j] = s1.top();
				s1.pop();
			}


			sort(ans, ans+size);

			cout << "Case #" << i << ": "<<ans[size-1] << endl;
		}
	}
	return 0;
}