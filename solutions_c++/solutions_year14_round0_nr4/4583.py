#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;
int res[1020];
bool cmp(double x, double y) {
    return x > y;
}

int race(double a[], double b[], int n) {
    memset(res,0,sizeof(res));
    int ret = 0;
    int ft = n-1, fq = n-1;
    for(int i = 0 , j= 0 ; i < n&&j<=ft;i++) {
	if(a[j]>b[i]) {
	    res[i] = j;
	    j++;
	    ret ++;
	} else if (a[j] < b[i] ) {
	    ft--;
	} else {
	    cout <<"!"<<endl;
	    for(int m = fq , k = ft; k >= j ; m--,k--) {
		if(a[k] > b[m]) {
		    ret++;
		    fq--,ft--;
		} else {
		    if(a[k] < b[i]);
		    ft = k-1;
		    fq = m;
		    break;
		}
	    }
	}
    }
    return ret;
}

int main() {
    freopen("D-large.in","r",stdin);
    freopen("D.out","w",stdout);
    double a[1020],b[1020];

    int t;
    cin >> t;
    int cas = 1;
    while(t--) {
	int n;
	cin >> n;
	memset(a,0,sizeof(a));
	memset(b,0,sizeof(b));
	for(int i = 0 ; i < n  ; i++) {
	    cin >> a[i];
	}
	for(int i = 0 ; i < n ; i++) {
	    cin >> b[i];
	}
	sort(a,a+n,cmp);
	sort(b,b+n,cmp);
	cout << "Case #" << cas++ << ": " <<race(a,b,n) <<" " << n-race(b,a,n) << endl;
    }
    
    
    return 0;
}
