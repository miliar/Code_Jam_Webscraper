#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_input2.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2016/A_output2.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);
	for(int tt=1;tt<=cases;tt++){
		string inp,ans;
		VI f(26,0);
		VI r(10,0);
		cin>>inp;
		int sz = inp.size();
		for(int i=0;i<sz;i++){
			f[inp[i]-'A']++;
		}
		int idx = 0;
		r[idx] = f['Z'-'A'];
		f['Z'-'A'] -= r[idx]; f['E'-'A'] -= r[idx]; f['R'-'A'] -= r[idx]; f['O'-'A'] -= r[idx];

		idx = 6;
		r[idx] = f['X'-'A'];
		f['S'-'A'] -= r[idx]; f['I'-'A'] -= r[idx]; f['X'-'A'] -= r[idx];

		idx = 8;
		r[idx] = f['G'-'A'];
		f['E'-'A'] -= r[idx]; f['I'-'A'] -= r[idx]; f['G'-'A'] -= r[idx]; f['H'-'A'] -= r[idx]; f['T'-'A'] -= r[idx];

		idx = 2;
		r[idx] = f['W'-'A'];
		f['T'-'A'] -= r[idx]; f['W'-'A'] -= r[idx]; f['O'-'A'] -= r[idx];

		idx = 4;
		r[idx] = f['U'-'A'];
		f['F'-'A'] -= r[idx]; f['O'-'A'] -= r[idx]; f['U'-'A'] -= r[idx]; f['R'-'A'] -= r[idx];

		idx = 3;
		r[idx] = f['R'-'A'];
		f['T'-'A'] -= r[idx]; f['H'-'A'] -= r[idx]; f['R'-'A'] -= r[idx]; f['E'-'A'] -= r[idx]; f['E'-'A'] -= r[idx];

		idx = 1;
		r[idx] = f['O'-'A'];
		f['O'-'A'] -= r[idx]; f['N'-'A'] -= r[idx]; f['E'-'A'] -= r[idx];

		idx = 7;
		r[idx] = f['S'-'A'];
		f['S'-'A'] -= r[idx]; f['E'-'A'] -= r[idx]; f['V'-'A'] -= r[idx]; f['E'-'A'] -= r[idx]; f['N'-'A'] -= r[idx];

		idx = 5;
		r[idx] = f['V'-'A'];
		f['F'-'A'] -= r[idx]; f['I'-'A'] -= r[idx]; f['V'-'A'] -= r[idx]; f['E'-'A'] -= r[idx];

		idx = 9;
		r[idx] = f['I'-'A'];
		f['N'-'A'] -= r[idx]; f['I'-'A'] -= r[idx]; f['N'-'A'] -= r[idx]; f['E'-'A'] -= r[idx];

		bool good = true;
		for(int i=0;i<26;i++){
			if(f[i] > 0){
				good = false;
			}
		}
		if(!good){
			printf("not good\n");
		}

		for(int i=0;i<10;i++){
			for(int j=0;j<r[i];j++){
				ans = ans + char('0'+i);
			}
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
    return 0;
}
