#include <iostream>
#include <algorithm>
using namespace std;

int m[27];
int v[27];

bool comp(int a, int b) {
	return v[a] > v[b];
}

int main() {
    int T,n,x,y;
    char c,d;
    cin>>T;
    for (int ti = 1; ti <= T; ti++) {
        cout<<"Case #"<<ti<<": ";
        cin>>n;
        for (int i = 0; i < n; i++) {
        	m[i] = i;
        	cin>>v[i];
        }
        v[n] = 0;
        m[n] = n;
        // cout<<v[2]<<m[2];
        bool f = false;
        while(true)
        {
        	sort(m,m+n, comp);
        	x = v[m[0]];

        	if (!x) break;
        	c = m[0]+'A';
        	y = v[m[1]];
        	d = m[1]+'A';
        	if (f) cout<<" ";
        	if (x == y) {
        		v[m[0]]--;
        		cout<<c;
        		// cout<<v[m[2]];
        		if (!v[m[2]]) {
					v[m[1]]--;
        			cout<<d;
        		}
        	}
        	else {
        		v[m[0]]--;
        		cout<<c;
        		if (y && x - 1 == y) {
        			v[m[1]]--;
        			cout<<d;
        		}
        		
        	}
        	f = true;
        }
        cout<<endl;
    }
    return 0;
}
