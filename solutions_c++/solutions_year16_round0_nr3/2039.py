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
		int n,j;
		cin>>n>>j;
		cout<<endl;
		int m = 15;
		int temp = (1<<m);
		ford(k,temp-1,0) {
		    string s = "1";
            ford(i,14,0) {
                int t2 = (1<<i);
                if((t2&k)!=0) {
                    s+='1';
                }
                else {
                    s+='0';
                }
            }
            string s2 = s;
            reverse(all(s2));
            s+=s2;
            cout<<s<<" ";
            fore(i,2,11)
            {
                if(i%2 == 0)
                    cout<<i+1<<" ";
                else
                    cout<<2<<" ";
            }
            cout<<endl;
            j--;
            if(j == 0) {
                break;
            }
		}
	}
	return 0;
}
