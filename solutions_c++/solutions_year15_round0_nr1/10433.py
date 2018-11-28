
#include <cstring>
#include <string.h>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>

using namespace std;


int n;
int N;

#define SMALL
//#define LARGE
int main() {
	freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif


	cin >> N;
	for(int nn=1;nn<=N;nn++) {
		cin>>n;
		string s;
		cin>>s;
		int f=0;
		int pre = s[0]-'0';
		for(int i=1;i<=n;i++){
			int x  = s[i]-'0';
			if(x>=1 && pre<i){
				f += (i-pre);
				pre += f;
			}
			pre += x;
		}
		printf("Case #%d: ", nn);
		cout<<f<<endl;
	}
	return 0;
}


