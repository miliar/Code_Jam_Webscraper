#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <cmath>
#include <queue>

#define ll long long int
#define pll pair<long long, long long>
#define pii pair<int, int>
#define pb push_back
#define mp make_pair
#define getchar_unlocked getchar
#define F first
#define S second

using namespace std;

int getint();
long long getlint();

int main() {
    int testcases;
	cin>>testcases;
	for(int t=1;t<=testcases;t++) {
		int n;
		cin>>n;
		vector < pii > p;
		int total =0;
		for(int i=0;i<n;i++) {
			int a;
			cin>>a;
			p.pb(mp(a, i));
			total += p[i].F;
		}
		priority_queue <pii > pq;
		for(int i=0;i<n;i++) {
			pq.push(p[i]);
		}
		string ans="";
		while(!pq.empty()) {
			pii a = pq.top();
			pq.pop();
			pii b = pq.top();
			pq.pop();
			if(a.F<=2 || a.F-2 <= b.F) {
				pq.push(a);
				pq.push(b);
				break;
			}
			pq.push(b);
			/**************
			if(a.F ==  2) {
				ans+=a.S+'A';
				ans+=a.S+'A';
				ans+=" ";
			}
			else if(a.F == 1) {
				ans+=a.S+'A';
				ans+=" ";
			}
			**************/
			if(false){}
			else {
				a = mp(a.F -2, a.S);
				ans+=a.S+'A';
				ans+=a.S+'A';
				ans+=" ";
				pq.push(a);
				total-=2;
			}
		}
		
		if(total%2 == 1) {
			pii a = pq.top();
			pq.pop();
			ans+='A'+a.S;
			ans+=" ";
			if(a.F != 1) {
				pq.push(mp(a.F-1, a.S));
			}
			total-=1;
		}

		while(!pq.empty()) {
			//printf("Stuck >Here Really\n");
			pii a = pq.top();
			pq.pop();
			pii b = pq.top();
			pq.pop();
			ans+=a.S+'A';
			ans+=b.S+'A';
			ans+=" ";
			if(a.F>1) {
				pq.push(mp(a.F-1, a.S));
			}
			if(b.F>1) {
				pq.push(mp(b.F-1, b.S));
			}
		}
		
		printf("Case #%d: %s\n", t, ans.c_str());
	}
	return 0;
}

int getint()
{
    int c,num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}

long long int getlint()
{
    int c;
    long long num=0;
    while((c=getchar_unlocked())==' ' || c=='\n')
    ;
    long long int sign;
    if(c=='-'){
        sign=-1;
    }
    else{
        sign=+1;
    }
    if(c=='-' || c=='+'){
        c=getchar_unlocked();
    }
    while(c!=' ' && c!='\n' && c!=EOF){
        num=(num<<1)+(num<<3)+(c-'0');
        c=getchar_unlocked();
    }
    return num*sign;
}
