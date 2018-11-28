//Author : pakhandi
//
using namespace std;

#include<bits/stdc++.h>

#define wl(n) while(n--)
#define fl(i,a,b) for(i=a; i<b; i++)
#define rev(i,a,b) for(i=a; i>=b; i--)
#define scan(n) scanf("%d", &n)
#define scans(s) scanf("%s", s)
#define scanc(c) scanf("%c", &c)
#define scanp(f) scanf("%f", &f)
#define print(n) printf("%d\n", n)
#define prints(s) printf("%s\n", s)
#define printc(c) printf("%c\n", c)
#define printp(f) printf("%f\n", f)
#define nline printf("\n")
#define mclr(strn) strn.clear()
#define ignr cin.ignore()
#define MOD 1000000007
#define ll long long int
#define u64 unsigned long long int

#define PB push_back
#define SZ size
#define MP make_pair

vector<int> v;

int rec(int ans, std::vector<int> v)
{
	int maxx = *max_element(v.begin(), v.end());
	if(maxx <= 2)
		return ans+maxx;

	int i, j, k;

	/*fl(i,0,v.SZ())
		cout<<v[i]<<" ";
	nline;*/

	int temp = maxx;
	v.erase(max_element(v.begin(), v.end()));
	int curr = INT_MAX;
	int limit = sqrt(maxx);
	fl(i,2,1+(limit))
	{
		if(maxx%i!=0) continue;
		std::vector<int> t,o;
		o = v;
		t = v;
		t.PB(i);
		t.PB(temp-i);
		o.PB(maxx/i);
		o.PB(temp-(maxx/i));
		curr = min(curr, rec(ans+1,t));
		curr = min(curr, rec(ans+1,o));
	}
	fl(i,0,v.SZ())
		v[i]--;
	v.PB(maxx-1);
	return min(curr, rec(ans+1,v));

}

int main()
{
	freopen("input2.txt","r",stdin);
    freopen("output2.txt","w",stdout);
	int i, j, k;
	int cases;
	int n;
	k=1;
	cin>>cases;
	wl(cases)
	{
		cin>>n;
		v.clear();
		int temp;
		fl(i,0,n)
		{
			cin>>temp;
			v.PB(temp);
		}
		sort(v.begin(), v.end());
		reverse(v.begin(), v.end());
		/*int c = 0;
		int ans = INT_MAX;
		while(1)
		{
			ans=min(ans,c+v[0]);
			cout<<c<<" : ";
			fl(i,0,v.SZ())
				cout<<v[i]<<" ";
			nline;
			if(v[0]==1)
				break;
			if(v[0]%2)
			{
				//cout<<"*"<<v[0]/2<<" ";
				v[0]/=2;
				v.PB(v[0]+1);
			}
			else
			{
				v[0]/=2;
				v.PB(v[0]);
			}
			sort(v.begin(), v.end());
			reverse(v.begin(), v.end());
			
			c++;
		}*/
		cout<<"Case #"<<k++<<": ";
		cout<<rec(0,v);
		nline;
	}

	return 0;
}