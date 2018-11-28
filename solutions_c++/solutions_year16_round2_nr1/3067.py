#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef unsigned long long llu;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define fill(a,v) memset(a, v, sizeof a)
#define INF 1e9
#define EPS 1e-9
#define pb push_back
#define sz size()
#define ln length()
#define forf(i,a,b) for(int i=a;i<b;i++)
#define forfa(i,a,b) for(int i=a;i<=b;i++)
#define forr(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define mod 1000000007


int main() {
	int t;
	cin>>t;
	string s,sr;
	char c[10] = {'Z','W','U','X','G','F','V','H','I','O'};
	string ns2[10] = {"ZERO","TWO", "FOUR", "SIX", "EIGHT","FIVE","SEVEN","THREE","NINE","ONE"};
	int ns[10] = {0,2,4,6,8,5,7,3,9,1};
	forf(z,1,t+1)
	{
		cout<<"Case #"<<z<<": ";
		cin>>s;
		string t;
		t=s;
		forf(i,0,s.sz){
			t[i]='~';
		}
		vi ans;
		int k=0;
		while(s!=t){
			int f=0;
			string st = s;
			forf(i,0,st.sz){
				if(st[i]==c[k])
				{
					ans.pb(ns[k]);
					string ll = ns2[k];
					int l=0;
					forf(q,0,ll.sz){
						forf(lll,0,st.sz){
							if(st[lll] == ll[q]){
								st[lll] = '~';
								break;
							}
						}
					}
					f=1;
					break;
				}
				
			}
			if(f==0)
				k++;
			else
				s=st;
		}
		sort(all(ans));
		forf(i,0,ans.sz)
			cout<<ans[i];
		cout<<"\n";
		//cout<<s<<endl;
	}

	return 0;
}
