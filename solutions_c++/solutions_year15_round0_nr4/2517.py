/*
                ================================
                Author : Adnaan 'Zohran' Ahmed
                Handle: adnaan1703
                Heritage Institute of Technology
                ================================
*/

#include <bits/stdc++.h>

#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
#define INF LONG_MAX
#define X first
#define Y second
#define pb push_back

using namespace std;

typedef vector<int> vint;
typedef vector<long long int> vlint;
typedef vector<vector<int> > vvint;
typedef vector<vector<long long int> > vvlint;
typedef long long int lint;

void solve(int);

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

	
    	freopen("inD.in", "r", stdin);
    	freopen("outD.txt", "w", stdout);
	

    int t = 1;
    cin>>t;
    for(int i=0; i<t; i++)
        solve(i+1);
	return 0;
}

bool test_dimension(int x, int maxx, int minn)
{
	int maxl = x;
	int minl = 1;
	bool flag = true;
	while(maxl>=minl)
	{
		if(maxl > maxx || minl > minn)
		{
			flag = false;
			break;
		}
		maxl--;
		minl++;
	}
	return flag;
}

bool test_area(int x, int r, int h)
{
	int area = r*h;
	if(area%x == 0)
		return true;
	else
		return false;
}

void solve(int test)
{
	int x,r,h,minn,maxx;
	cin>>x>>r>>h;
	minn = min(r,h);
	maxx = max(r,h);
	bool flag = true;

	switch(x)
	{
		case 1:
			flag = true;
			break;

		case 2:
			flag = test_area(x, r, h);
			break;

		case 3:
			flag = test_dimension(x, maxx, minn) && test_area(x, r, h);
			break;
		case 4:
			flag = test_dimension(x, maxx, minn) && test_area(x, r, h);
			if(minn == 2)
				flag = false;
			break;
		case 5:
			flag = test_dimension(x, maxx, minn) && test_area(x, r, h);
			if(minn == 2 || minn == 3)
				flag = false;
			break;
		case 6:
			flag = test_dimension(x, maxx, minn) && test_area(x, r, h);
			if(minn == 2 || minn == 3 || minn == 4)
				flag = false;
			break;
		default:
			flag = false;
	}

	string ans = (flag) ? "GABRIEL" : "RICHARD";
	cout<<"Case #"<<test<<": "<<ans<<endl;
}