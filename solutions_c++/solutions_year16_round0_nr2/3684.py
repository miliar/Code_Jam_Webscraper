#include <iostream>
#include <string>
#include <map>
#include <queue>
using namespace std;

priority_queue < pair < int , string > > q;
map < string , int > mp;
string S;
	int mxsz = 0;
int solve()
{
	mp.clear();
	while(!q.empty())q.pop();
	pair < int , string > temp;
	string dest  = "";
	int len = S.length();
	for(int i=0;i<len;i++) dest+="+";
	q.push(make_pair(-1,S));

	while(!q.empty())
	{
		temp = q.top();
		q.pop();
		temp.first = -temp.first;
	
		if(mp[temp.second]!=0) continue;
		if(temp.second == dest) return temp.first;
		mp[temp.second] = -temp.first;
		string reverse = "";
		for(int i = len - 1 ; i >= 0 ; i--)
		{
			if(temp.second[i] == '+')
				reverse+='-';
			else
				reverse+='+';
		}
		string res="";
		for(int i = 0; i < len ; i++)
		{
			 res+=reverse[len-1-i];
			 
			 if(i!=len-1)
			 {
			  q.push(make_pair(-temp.first-1,res + temp.second.substr(i+1)));
			 //s cout << S << ' ' << temp.second << ' ' << -temp.first-1 << 'x' << reverse << ' '<<  res + temp.second.substr(i+1) << endl;
			}else
			{
			  q.push(make_pair(-temp.first-1,res));
		//cout << S << ' ' << temp.second << ' ' << -temp.first-1 << ' '<<  res << endl;
			}
		}
	}
}
int main()
{
	
	  ios_base::sync_with_stdio(false);
    freopen("1.in","r",stdin);   freopen("1.out","w",stdout);
 int T;
 cin >> T;
 long long maxres=0;
 for(int i = 0 ; i <T ; i++)
 {
 
	cin >> S;
	int res = solve();

	cout << "Case #"<< i +1 <<  ": ";
	cout << res-1  << endl;
	}
//cout << maxres << endl;
	return 0;
}
