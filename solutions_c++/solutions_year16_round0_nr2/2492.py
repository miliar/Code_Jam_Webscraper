#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include<iomanip>
using namespace std;

typedef long long ll;
typedef vector <int> vi;
typedef pair< int ,int > pii;
#define pb push_back
#define sz size()
#define ln length()
#define fore(i,a,b) for(int i=a;i<b;i++)
#define fores(i,a,b) for(int i=a;i<=b;i++)
#define ford(i,a,b) for(int i=a;i>=b;i--)
#define all(a) a.begin(),a.end()
#define mp make_pair
#define ff first
#define ss second
#define sc(a) scanf("%d",&a)
#define md 1000000007

int main() {
	freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	fore(z,0,t)
	{
		printf("Case #%d: ",z+1);
		string s;
		cin>>s;
		int fa = 0;
		while(true) {
            bool mins = false;
            int ind = -1;
            ford(i,s.ln-1,0) {
                if(s[i] == '-') {
                    ind = i;
                    mins = true;
                    break;
                }
            }
            if(!mins)
                break;
            int cnt = 0;
            fore(i,0,s.ln) {
                if(s[i] == '-')
                    break;
                cnt++;
                s[i] = '-';
            }
            if(cnt!=0) {
                fa++;
                //cout<<s<<endl;
            }
            reverse(s.begin(),s.begin() + ind +1);
            fore(i,0,ind+1)
            {
                if(s[i] == '-')
                    s[i] = '+';
                else
                    s[i] = '-';
            }
            fa++;
            //cout<<s<<endl;
		}
		cout<<fa<<endl;
	}
	return 0;
}
