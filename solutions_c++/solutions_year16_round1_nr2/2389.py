#include <bits/stdc++.h>
using namespace std;

int main()
{long long int test,i,j,k=1;
scanf("%lld",&test);
while(test--){
    int no,s,r=0,g[2510],m[55];
    scanf("%lld",&no);
    memset(g,0,sizeof(g));
    for(i=0;i<2*no-1;i++){
			for(j=0;j<no;j++)
			{scanf("%lld",&s);
			g[s]++;}
    }
    for(i=0;i<2510;i++){
			if(g[i]&1)
			m[r++]=i;
    }
    printf("Case #%d: ",k);
    for(i=0;i<no;i++)
    cout<<m[i]<<" ";
    printf("\n");
    k++;
}return 0;}
