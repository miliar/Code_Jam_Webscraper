#include <iostream>
using namespace std;
int tot, cases, le, x,y,z;
int main() {cin >> cases;
	for(int le=1; le<=cases; le++){scanf("%d%d%d",&x,&y,&z);
	tot=0;
	for(int i=0; i<x; i++){for(int j=0; j<y; j++){if ((i&j)<z){tot++;}}} printf("Case #%d: %d\n",le,tot);
	}return 0;
}
