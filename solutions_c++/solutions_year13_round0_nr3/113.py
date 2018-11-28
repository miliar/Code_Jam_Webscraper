#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

const string large = "10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
int ans = 0;
vector <string> events;
vector <int> sum, cnt;

// a <= b
int compare(string a, string b)
{
	if ( a.length() != b.length() )	return a.length() < b.length();
	for (int i = 0; i < a.length(); i++)
		if ( a[i] != b[i] )
			return a[i] < b[i];
	return true;
}

void find(string a)
{
	int l = 0, r = events.size() - 1;
	while (r - l > 1)
	{
		int m = (l+r) >> 1;
		if (compare(events[m],a))	l = m;
		else r = m;
	}
	sum[l]++;
	if ( events[l] == a)	cnt[l]++;
}

string mult(string a, string b)
{
	vector <int> v(a.length()+b.length()+5);
	for (int i = 0; i < a.length(); i++)
		for (int j = 0; j < b.length(); j++)
		{
			v[i+j] += (int)(a[i]-'0') * (int)(b[j]-'0');
			int pos = i+j;
			while (v[pos] > 9)	v[pos+1] += v[pos] / 10, v[pos] %= 10, pos++;
		}
	string ans;
	int l;
	for ( l = v.size() - 1; v[l] == 0; l--);
	for (int i = 0; i <= l; i++)
		ans  = (char)('0'+v[i]) + ans;
	return ans;
}

bool pal(string a)
{
	for (int i = 0; i < a.length(); i++)
		if (a[i] != a[a.length()-1-i])	return false;
	return true;
}

void go(string s, int c, int o)
{
	string a = s, b = s;
	for (int i = 0; i < s.length(); i++)
		a += s[s.length()-1-i];
	for (int i = 1; i < s.length(); i++)
		b += s[s.length()-1-i];
	string a2 = mult(a,a), b2 = mult(b,b);	
	if ( !compare(b2,large) )	return;
	if ( pal(b2))	find(b2);
	if ( pal(a2))	find(a2);
	if (c > 0 && o > 1 || c > 1)	return;
	go( s + '0',c,o);
	if (o < 5)	go(s+'1',c,o+1);
	go(s+'2',c+1,o);
}

int main(void)
{
	int T; 
	cin >> T;
	vector <string> ax,bx;
	for (int C = 1; C <= T; C++)
	{
		string A,B;
		cin >> A >> B;
		ax.push_back(A),bx.push_back(B);
		events.push_back(A);
		events.push_back(B);
	}
	events.push_back(large+"0");
	events.push_back("");
	sort(events.begin(),events.end(),compare);
	sum = vector<int>(events.size());
	cnt = vector<int>(events.size());
	go("1",0,1);
	go("2",1,0);
	for (int C = 1; C <= T; C++)
	{
		int l = 0, r = events.size() - 1;
		while (r - l > 1)
		{
			int m = (l+r) >> 1;
			if (compare(events[m],ax[C-1]))	l = m;
			else r = m;
		}
		int ans = 0;
		for (int k = l; k+1 < events.size(); k++)
			if ( events[k] == bx[C-1] && events[k+1] != bx[C-1] )
			{
				ans += cnt[k];
				break;
			} else ans += sum[k];
		if ( compare("9",bx[C-1]) && compare(ax[C-1],"9"))	ans++;
		cout << "Case #" << C << ": " << ans << endl;
	}
	return 0;
}
