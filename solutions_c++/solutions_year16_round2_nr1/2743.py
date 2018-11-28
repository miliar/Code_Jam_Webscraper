#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define pb push_back
#define ft first
#define sd second

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for ( int k=1;k<=t;k++ ) {
        string s;
        cin>>s;
        int l=s.length();
        map<char,int> m;
        for ( int i=0;i<l;i++ ) {
            m[s[i]]++;
        }
		vector<int> phn;
		map<char,int>::iterator it;
        for ( it=m.begin();it!=m.end();it++ ) {
			int dig=-1;
			int c=it->sd;
			if ( (it->sd) > 0 ) {
				switch(it->ft){
					case 'Z':
						m['Z']-=c;
						m['E']-=c;
						m['R']-=c;
						m['O']-=c;
						dig=0;
						break;
					case 'W':
						m['T']-=c;
						m['W']-=c;
						m['O']-=c;
						dig=2;
						break;
					case 'U':
						m['F']-=c;
						m['O']-=c;
						m['U']-=c;
						m['R']-=c;
						dig=4;
						break;
					case 'G':
						m['E']-=c;
						m['I']-=c;
						m['G']-=c;
						m['H']-=c;
						m['T']-=c;
						dig=8;
						break;
					case 'X':
						m['S']-=c;
						m['I']-=c;
						m['X']-=c;
						dig=6;
						break;
					}
				}
                if ( dig!=-1 ) {
					while ( c-- ) {
						phn.pb(dig);
					}
                }
            }

            for ( it=m.begin();it!=m.end();it++ ) {
				int dig=-1;
				int c=it->sd;
				if ( (it->sd) > 0 ) {
					switch(it->ft){
					case 'O':
						m['O']-=c;
						m['N']-=c;
						m['E']-=c;
						dig=1;
						break;
					case 'T':
						m['T']-=c;
						m['H']-=c;
						m['R']-=c;
						m['E']-=c;
						m['E']-=c;
						dig=3;
						break;
					case 'F':
						m['F']-=c;
						m['I']-=c;
						m['V']-=c;
						m['E']-=c;
						dig=5;
						break;
					case 'S':
						m['S']-=c;
						m['E']-=c;
						m['V']-=c;
						m['E']-=c;
						m['N']-=c;
						dig=7;
						break;
					}
				}
				if ( dig!=-1 ) {
					while ( c-- ) {
						phn.pb(dig);
					}
                }
        }
        if ( m['N']!=0 ) {
            int n=m['N']/2;
            while( n-- ) {
				phn.pb(9);
            }
        }
        sort(phn.begin(),phn.end());
		cout<<"Case #"<<k<<": ";
		int sz=phn.size();
		for ( int i=0;i<sz;i++ ) {
            cout<<phn[i];
		}
		cout<<"\n";
	}
	return 0;
}
/*
*/
