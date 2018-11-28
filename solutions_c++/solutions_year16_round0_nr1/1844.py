#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int aa[10];
int main(int argc, char** argv){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf(" %d", &tt);
	for (int qq = 1; qq <= tt; qq++){
		for (int i = 0; i < 10; i++) aa[i] = 0;
		long long int n;
		scanf(" %lli", &n);
		if (n == 0) printf("Case #%d: INSOMNIA\n", qq);
		else {
			long long int dn = n;
			int ct = 0;
			long long int it = 0;
			while (it < 1e9){
				long long int tn = n;
				while(tn > 0) {
					if (aa[tn % 10] == 0){
						aa[tn % 10] = 1;
						ct++;
					}
					tn = tn / 10;
				}
				if (ct == 10) break; 
				n += dn;
				it++;
			}
			if (it >= 1e9) printf("Case #%d: INSOMNIA\n", qq);
			else printf("Case #%d: %lli\n", qq, n);
		}
	}
	return 0;
}
