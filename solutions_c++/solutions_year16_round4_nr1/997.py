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
		int n,p,r,s;
		cin>>n>>r>>p>>s;
		if(abs(p-r)>1 || abs(p-s)>1 || abs(s-r)>1) {
            cout<<"IMPOSSIBLE"<<endl;
            continue;
		}
		string s1 = "P",s2 = "R",s3 = "S";
		int total = (1<<n);
		while(total!=1) {
            //cout<<p<<" "<<r<<" "<<s<<endl;
            //cout<<s1<<" "<<s2<<" "<<s3<<endl;
            total/=2;
            string s6 = s1;
            s1+=s2;
            string s4 = s2;
            s2.clear();
            s2 = s6+s3;
            string s5 = s3;
            s3.clear();
            s3 = s4+s5;
            if(p%2 == 0) {
                p/=2;
                r = p;
                s = total-p-r;
            }
            else if(r%2 == 0) {
                p = s = r/2;
                r = total-p-s;
            }
            else if(s%2 == 0) {
                s/=2;
                r = s;
                p = total-s-r;
            }
		}
		//cout<<p<<" "<<r<<" "<<s<<endl;
		if(p)
            cout<<s1;
        else if(r)
            cout<<s2;
        else if(s)
            cout<<s3;
        cout<<endl;
	}
	return 0;
}
