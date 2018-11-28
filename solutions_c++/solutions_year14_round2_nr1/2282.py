#include "iostream"
#include "string"
#include "vector"
using namespace std;
//std::vector<string> v;

int f(string &s1 , string &s2,int &l1,int &l2,int &i,int ans)
{
	if(i>=l1 && i>=l2 && l1==l2)
	{
		return ans;
	}else
	{
		if(s1[i]==s2[i])
		{
			i++;
			return f(s1,s2,l1,l2,i,ans);
		}else
		{
			if(l1<=l2)
			{
				if(s2[i]==s2[i-1])
				{
					s2.erase(s2.begin()+i);
					l2=s2.length();
					ans++;
					return f(s1,s2,l1,l2,i,ans);
				}else if(s1[i]==s1[i-1])
				{
					s1.erase(s1.begin()+i);
					l1=s1.length();
					ans++;
					return f(s1,s2,l1,l2,i,ans);
				}else
				{
					return -1;
				}
			}else
			{
				return f(s2,s1,l2,l1,i,ans);
			}
		}
	}
}

int main(int argc, char const *argv[])
{
	int t;
	int counter =1;
	cin>>t;
	while(t--)
	{
		//v.clear();
		int n;
		cin>>n;
		string s1;
		string s2;
		cin>>s1;
		cin>>s2;
		int step = 0;
		int len1 = s1.length();
		int len2 = s2.length();
		int i=0;
		if(s1[i]==s2[i])
		{
			i++;
			step = f(s1,s2,len1,len2,i,0);
		}else
		{
			step = -1;
		}

		if(step >= 0)
		{
			cout<<"Case #"<<counter++<<": "<<step<<endl;
		}else
		{
			cout<<"Case #"<<counter++<<": "<<"Fegla Won"<<endl;
		}

	}
	return 0;
}