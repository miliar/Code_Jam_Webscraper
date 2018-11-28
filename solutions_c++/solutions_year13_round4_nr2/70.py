#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T;
int N;
string P;

vector<int> tobit(const string &s, int n, int add)
{
	vector<int> orig, ret;
	for(int i=0; i<(int)s.length(); i++)
	{
		orig.push_back(s[i]-'0');
	}
	orig.back() += add;
	for(int i=(int)orig.size()-1; i>0; i--)
	{
		if(orig[i]<0)
		{
			orig[i] += 10;
			orig[i-1]--;
		}
	}

	for(int i=0; i<n; i++)
	{
		ret.push_back(orig.back()%2);
		int carry = 0;
		//for(int j=0; j<(int)orig.size(); j++)cout<<orig[j];cout<<endl;
		for(int j=0; j<(int)orig.size(); j++)
		{
			if(carry)orig[j] += 10;
			carry = orig[j]%2;
			orig[j] /= 2;
		}
	}

	//for(int i=0; i<(int)ret.size(); i++)cout<<ret[i];cout<<endl;
	return ret;
}

int main()
{
    ios_base::sync_with_stdio(0);

	//string s;
    //while(cin>>s)tobit(s, 10, 0);

    cin>>T;
    for(int t=1; t<=T; t++)
	{

		cin>>N>>P;
		vector<int> retm = tobit(P, N, -1), ret = tobit(P, N, 0);
		cout<<"Case #"<<t<<": ";
		bool anyone = false;
		for(int i=0; i<N; i++)if(ret[i])anyone = true;

		if(!anyone)
		{
			P.back()--;
			for(int i=(int)P.length()-1; i>0; i--)
			{
				if(P[i]<'0')
				{
					P[i] += 10;
					P[i-1]--;
				}
			}
			cout<<P<<" "<<P<<endl;
			continue;
		}

		int mcontone = 0;
		for(int i=N-1; i>=0; i--)
		{
			if(retm[i])mcontone++;
			else break;
		}

		int contone = 0;
		for(int i=N-1; i>=0; i--)
		{
			if(ret[i])
			{
				contone = i;
				break;
			}
		}

		//cout<<"M "<<mcontone<<" C "<<contone<<endl;

		vector<int> ans1, ans2;
		ans1.resize(N);
		ans2.resize(N);

		ans1[0] = 2;
		for(int i=0; i<mcontone; i++)
		{
			int carry = 0;
			for(int j=0; j<N; j++)
			{
				ans1[j] = ans1[j]*2 + carry;
				carry = ans1[j] / 10;
				ans1[j] %= 10;
			}
		}
		while(ans1.size()>1 && ans1.back()==0)ans1.pop_back();
		ans1[0] -= 2;
		for(int i=(int)ans1.size()-1; i>=0; i--)cout<<ans1[i];cout<<" ";

		ans2[0] = 0;
		for(int i=0; i<N; i++)
		{
			int carry = 0;
			for(int j=0; j<N; j++)
			{
				ans2[j] = ans2[j]*2 + carry;
				carry = ans2[j]/10;
				ans2[j] %= 10;
			}
			if(i<contone)ans2[0]++;
		}
		while(ans2.size()>1 && ans2.back()==0)ans2.pop_back();
		for(int i=(int)ans2.size()-1; i>=0; i--)cout<<ans2[i];cout<<endl;
	}

    return 0;
}
