#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <ctime>
#define MAXN 300
#define DBL double
using namespace std;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, it=1;
    cin>>T;
    while(T--){
		DBL c, f, x;
		cin>>c>>f>>x;
		DBL d=2, ans=0;
		while(c/d+x/(d+f)<x/d){
			ans += c/d;
			d += f;
			//cout << d << " " <<ans<<endl;
		}
		ans += x/d;
		printf("Case #%d: %.7f\n", it++, ans);
	}
    
    return 0;
}

