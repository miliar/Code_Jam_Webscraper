#include<bits/stdc++.h>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	int t;
	cin>>t;
	for ( int k=1;k<=t;k++ ) {
        string s;
        cin>>s;
        int len=s.length();
        int ans=0;
        for ( int i=len-1;i>=0;i-- ) {
            if ( s[i]=='-' ) {
				int j=-1;
                while ( s[j+1]=='+' ) {
					j++;
                }
                if ( j!=-1 ) {
                    for ( int m=0;m<=j;m++ ) {
						s[m]='-';
                    }
                    ans++;
                }
                int l=0,r=i;
                while ( l<=r ) {
                    char ch1=s[l];
                    char ch2=s[r];
                    if ( ch1=='-' ) {
                        s[r]='+';
                    }
                    else {
						s[r]='-';
                    }
					if ( ch2=='-' ) {
                        s[l]='+';
                    }
                    else {
						s[l]='-';
                    }
                    l++;
                    r--;
                }
                ans++;
            }
        }
        cout<<"Case #"<<k<<": "<<ans<<"\n";
	}
	return 0;
}
