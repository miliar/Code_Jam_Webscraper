#include <iostream>
#include <cstdio>
#include <string.h>
using namespace std;

int ans1[4];
int ans2[4];


int main() {
	int t;int test = 0;
//	FILE *fp = fopen("A-small-attempt0","r");
 //   FILE *ft = fopen("output.txt","w");
  //  cout<<"entering\n";
scanf("%d", &t);
    //cout<<"entering\n";
	while(t--) {
		test++;
		bool check[17];
		memset(check,false,sizeof(check));
		int n,m,temp,ans,count = 0;
		scanf("%d", &n);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &temp);
				if(i+1 == n) check[temp] = true;
			}
		}
		scanf("%d", &m);
		for(int i = 0; i < 4; i++) {
			for(int j = 0; j < 4; j++) {
				scanf("%d", &temp);
				if(i+1 == m && check[temp] == true) {
						count++; ans = temp;
				}
			}
		}
		if(count == 0) printf("Case #%d: Volunteer cheated!\n",test);
		else if(count == 1) printf("Case #%d: %d\n",test,ans);
		else printf("Case #%d: Bad magician!\n",test);
	}
	return 0;
}
