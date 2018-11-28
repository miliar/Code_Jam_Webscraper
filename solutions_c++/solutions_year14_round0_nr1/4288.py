#include <cstdio>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>

#define gc getchar_unlocked

using namespace std;

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}

int main()
{
	int T ,c1,c2,temp,common,commonCount;
	int a[4];
	scanint(T);
	for(int t =0; t<T;t++) {
		common = 0;
		commonCount = 0;
		scanint(c1);
		for(int i=0;i<(4*c1-4);i++) {
			scanint(temp);
		}
		for(int i=0;i<4;i++) {
			scanint(a[i]);
		}
		for(int i=16;i>4*c1;i--) {
			scanint(temp);
		}

		scanint(c2);
		for(int i=0;i<(4*c2-4);i++) {
			scanint(temp);
		}
		for(int i=0;i<4;i++) {
			scanint(temp);
			for(int j=0;j<4;j++) {
				if(a[j] == temp) {
					common = temp;
					commonCount++;
					break;
				}
			}
		}
		for(int i=16;i>4*c2;i--) {
			scanint(temp);
		}

		if(commonCount>0) {
			if(commonCount>1) {
				printf("Case #%d: Bad magician!\n",t+1);
			}
			else {
				printf("Case #%d: %d\n",t+1,common );
			}
		} else {
			printf("Case #%d: Volunteer cheated!\n",t+1);
		}
	}
	return 0;
}
