#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <deque>
#include <iostream>
#include <iomanip>
#include <limits>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef vector <int> vi;
typedef vector <string> vs;
typedef istringstream iss;
typedef ostringstream oss;

int main(){
	#ifndef ONLINE_JUDGE
 		freopen("A-small-attempt0.in", "r", stdin);
		freopen("vd.out", "w", stdout);
	#endif
	ios_base::sync_with_stdio(false);
	int t, n;
	string s1, s2;
	int a1[102], a2[102];
	char t1[102], t2[102];
	int l1, l2, i, j, k;
	cin >> t;
	string s, so;
	s = "Fegla Won";
	for(int t0 = 1; t0 <= t; t0++){
		cin >> n;
		string a[n];
    	string b[n];
    	for(i=0;i<n;i++){
        	cin>>a[i];
        	b[i]+=a[i]+'=';
    	}
    	cout << "Case #" << t0 <<": ";
    	int pp=0;
    	string z;
    	for(j=0;j<b[0].size();j++){
            if(b[0][j]!=b[0][j+1]){
                z+=b[0][j];
            }
    	}
    	for(i=1;i<n;i++){
            string x;
            for(j=0;j<b[i].size();j++){
                if(b[i][j]!=b[i][j+1]){
                x+=b[i][j];
                }
            }
        	if(x.size()!=z.size()){
            	pp=1;
            	break;
        	}
        	else{
            	for(j=0;j<z.size();j++){
                	if(z[j]!=x[j]){
                    	pp=1;
                  	  break;
                	}
            	}
            	if(pp==1){
                	break;
            	}
        	}
    	}
    	if(pp==1){
        cout << s << endl;
    	}
    	else{
        	long long  int m1=0,m2=100000000;
        	long int aa[n][100];
        	for(i=0;i<n;i++){
            	for(j=0;j<100;j++){
                	aa[i][j]=0;
            	}
        	}
        	for	(i=0;i<n;i++){
                int k=0;
                string qw=a[i]+'=';
            	for(j=0;j<qw.size();j++){
                	if(a[i][j]==a[i][j+1]){
                    	aa[i][k]++;
            		}
                	else		{aa[i][k]++;k++;}
            }
        }
        for(i=0;i<n;i++){
            m1=0;
            for(j=0;j<n;j++){
                for(k=0;k<a[i].size();k++){
                    m1+=abs(aa[i][k]-aa[j][k]);
                }
            }
            m2=min(m1,m2);
        }
        string x=a[0]+'=';
        int ff=0;
    	for(i=0;i<a[0].size()-1;i++){
       	if(a[0][i]!=a[0][i+1])
        ff++;
    	}
	    ff++;
	    m1=0;
	    for(i=0;i<n;i++){
	        int o=a[i].size();
	        m1+=abs(o-ff);
	    }
	    //cout<<m1<<' ';
	    m2=min(m1,m2);
	    cout << m2 << endl;
		m2=100000000;
	    }
		//cout << "Case #" <<  k <<  ": " << 0 << endl; 
	}
	return 0;
}



