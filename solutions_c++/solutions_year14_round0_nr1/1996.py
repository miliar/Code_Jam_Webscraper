#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
#include<cstdlib>
using namespace std;

int arr[16],select;

int main() {
	int test,z,i,j,r,k;
	int tmp;

	freopen("A-small-attempt3.in","r",stdin);
	freopen("a.txt","w",stdout);
	scanf("%d",&test);
	for ( z=1; z<=test; z++ ) {
		//init
		for ( i=0; i<16; i++ ) arr[i]=0;
		//body
		scanf("%d",&select);
		for ( i=1; i<=4; i++ ) {
			if ( select==i ) {
				for ( j=0; j<4; j++ ) {
					scanf("%d",&tmp);
					arr[tmp-1]++;
				}
			}
			else {
				for ( j=0; j<4; j++ ) 
					scanf("%d",&tmp);
			}
		}
		scanf("%d",&select);
		for ( i=1; i<=4; i++ ) {
			if ( select==i ) {
				for ( j=0; j<4; j++ ) {
					scanf("%d",&tmp);
					arr[tmp-1]++;
				}
			}
			else {
				for ( j=0; j<4; j++ ) 
					scanf("%d",&tmp);
			}
		}

		int cnt=0;
		for ( i=0; i<16; i++ ) {
			if ( arr[i]==2 ) {
				r=i+1;
				cnt++;
			}
		}

		printf("Case #%d: ",z);
		if ( cnt==1 ) printf("%d\n",r);
		else if ( cnt==0 ) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
	}
}