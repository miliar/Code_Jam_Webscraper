#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <string.h>
#include <stdlib.h>
#include <ctime>
#define DBL double
#define MAXN 1005
using namespace std;

int main()
{
    freopen("D-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T, it=1;
    cin>>T;
    while(T--){
		int n;
		DBL a[MAXN], b[MAXN];
		cin >> n;
		for(int i=0; i<n; i++)
			cin >> a[i];
		for(int i=0; i<n; i++)
			cin >> b[i];
		sort(a, a+n);
		sort(b, b+n);
		int cnt1=0, cnt2=0;
		int h=0, t=n-1;
		for(int i=0; i<n; i++){
			if(a[i]<b[h])
				t--;
			else
				cnt1++, h++;
		}	
		h=0, t=n-1;
		for(int i=n-1; i>=0; i--){
			if(a[i]<b[t])
				t--;
			else
				cnt2++, h++;
		}
		printf("Case #%d: %d %d\n", it++, cnt1, cnt2);
	}
    
    return 0;
}

