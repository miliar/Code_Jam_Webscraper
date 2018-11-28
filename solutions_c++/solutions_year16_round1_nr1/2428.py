#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main()
{
	int t;
	cin>>t;
	string test[t];
	for (int i = 0; i < t; i++)
	{
		cin>>test[i];
	}
	for (int i = 0; i < t; i++)
	{
		int len=test[i].length();
		char* word= new char [len+1];
		strcpy(word,test[i].c_str());

		char* ans= new char [2*len+1];
		char curr=word[0];
		ans[len-1]=curr;
		int left=len-2,right=len;
		for (int j = 1; j < len; j++)
		{
			if (word[j]>=curr)
			{
				ans[left]=word[j];
				curr=word[j];
				// cout<<ans[left]<<' ';
				left--;
				continue;
			}
			ans[right]=word[j];
			// cout<<ans[right]<<' ';
			right++;
		}
		cout<<"Case #"<<i+1<<": ";
		for (int j = left+1; j < right; j++)
		{
			cout<<ans[j];
		}
		cout<<endl;

	}
	return 0;
}