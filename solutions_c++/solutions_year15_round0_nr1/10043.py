#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

const int MAXN = 1000;
int T, n;
int a[MAXN]={0,};
string input="";
int main() {
	freopen ("test.in","r",stdin);
	freopen ("1.out","w",stdout);
    scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        cin >> n >>input;
        int Answer = 0;
        int standup = 0;
        for (int i=0 ;i < n+1; i++){
        	a[i] = input[i]-'0';
		}
        for (int i=0 ; i <=n; i++){
        	if(standup>=i){
        		standup+=a[i];
        		
			}else if(a[i]>0) {
				Answer += i-standup;
				standup=i+a[i];
			}
		}
        cout << "Case #" << t << ": " << Answer<<endl;
    }
    return 0;
}
