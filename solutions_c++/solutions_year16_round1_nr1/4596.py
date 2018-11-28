#include<bits/stdc++.h>
using namespace std;

int main (void)
{
	freopen("A.in","r",stdin);
	freopen("output_file.out","w",stdout);
	int test;
	scanf ("%d", &test);

	int a;
	
	for (a = 1; a <= test; a++) {
		string str;
		char ans[10000];
		cin>>str;
		
		int i = 1;
		int ctr = 1 ;
		ans[0] = str[0];
		while (str[i] != '\0') {
			//printf("%c\n", str[i]);
			if (str[i] < ans[0]) {
				ans[ctr] = str[i];
				//printf("%c\n", ans[ctr]);
				ctr++;
			} else {
				int j = 0;
				for (j = ctr ; j > 0;j--) {	
					ans[j] = ans[j-1];
					//printf("%c\n", ans[j+1]);
				}
				ctr++;
				ans[0] = str[i];
			}
			i++;
			//printf("%d\n",ctr);
		}
		//printf("%d---\n", ctr);
		ans[ctr] = '\0';
		printf("Case #%d: %s\n", a,ans);
		
	}
	return 0;
}
