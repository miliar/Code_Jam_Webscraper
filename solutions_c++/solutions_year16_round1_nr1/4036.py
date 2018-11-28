#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("ALarge.in","r",stdin);
    freopen("Output2.out","w",stdout);
	int t;	cin >> t;
	for(int k=1 ; k<=t ; k++)
	{
		string str,words="";	cin >> str;
		char interval[2]={str[0],str[0]};
		for(int i=0 ; i<str.size() ; i++)
		{
			if(interval[0]<=str[i])	interval[0]=str[i];
			else interval[1]=str[i];
		}
		words+=str[0];
		for(int i=1 ; i<str.size() ; i++)
		{
			if(str[i]>=words[0])
			{
				reverse(words.begin(),words.end());
				words+=str[i];
				reverse(words.begin(),words.end());
			}
			else words+=str[i];
		}
		
		cout << "Case #" << k << ": " << words << endl;
	}
	
}
