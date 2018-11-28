      /*  Sourav Verma (Swerve7)
            Code @ CodeJam 2016  */

#include <bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb  push_back
#define mp  make_pair
#define pic pair<int ,char>
#define F  first
#define S  second

int fn1(int* a, int b) {
    int x=-1,y=-1;
    for(int i=0;i<b;i++) {
        if(x<a[i]) {
            x=a[i]; y=i;
        }
    }
    return y;
}

bool fn2(int* a, int b) {
    int x=-1,sum=0;
    for (int i=0;i<b;i++) {
        sum+=a[i];
        x=max(x,a[i]);
    }
    return x*2<=sum;
}

int main() {
	int tc; scanf("%d",&tc);
	for(int t=1;t<=tc;t++){
		int n,sum=0,x,y; scanf("%d",&n);
        int p[1005];
        for(int i=0;i<n;i++) {
        	scanf("%d",&p[i]);
            sum+=p[i];
        }
        cout<<"Case #"<<t<<": ";
        for(int i=0;i<sum;i++) {
            x=fn1(p,n); p[x]--;
            if(!fn2(p,n)) {
                y=fn1(p,n);
                p[y]--; i++;
                cout<<(char)('A'+x)<<(char)('A'+y)<<" "; 
            } 
            else  cout<<(char)('A'+ x)<<" ";
        }
        cout<<"\n";
	}
	// your code goes here
	return 0;
}