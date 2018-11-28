#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
        int te,j,i;
        float c,f,x,r,t;
        float farm[10000];
        scanf("%d",&te);
        i=0;
        while(te--) {
                cin>>c>>f>>x;
		r = 2.0;
		t = 0.0;
		for(j=0;j<100005;j++) {
			farm[j] = t + x/r;
			t += c/r;
			r += f;
			if(j && farm[j]>farm[j-1]) break;
		}
		printf("Case #%d: %.7lf\n",++i,farm[j-1]);
        }
        return 0;
}

