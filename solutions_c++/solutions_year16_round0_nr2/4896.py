#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	int T,t=1,ans,j;
	string S,R;
	cin>>T;
	while(t<=T)
	{
		cin>>S;
		ans = 0;
		j = S.length();
		while(j>0&&S[j-1]=='+')
		{
			j--;
		}
		while(j!=0)
		{
			if(S[0]=='+')
			{
				for(int i=0;S[i]=='+';i++)
					S[i]='-';
				ans++;
			}
			R = S;
			for(int i=0;i<j;i++)
			{
				
				S[i] = (R[j-1-i]=='+')?'-':'+';
			}
			ans++;
			while(j>0&&S[j-1]=='+')
			{
				j--;
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
		t++;
	}
	return 0;
}