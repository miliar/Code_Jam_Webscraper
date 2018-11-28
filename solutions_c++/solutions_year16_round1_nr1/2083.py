#include <stdio.h>
#include <string.h>
#include <string>
using namespace std;

char str[1010];

int main (){
	freopen ("F:\\GCJ\\R1\\A-large.in", "r",stdin);
	freopen ("F:\\GCJ\\R1\\A-large.out", "w",stdout);
	
	int cas = 1;
	int T;scanf ("%d",&T);
	while (T--){
		printf ("Case #%d: ",cas++);
		scanf ("%s", str);
		int len = strlen (str);
		string ans = "";
		for (int i = 0; i < len; i++){
			if (i == 0)	ans += str[i];
			else{
				if (str[i] > ans[0]){
					ans = str[i] + ans;
				}
				else if (str[i] < ans[0]){
					ans = ans + str[i];
				}
				else{
					string tmp1 = str[i] + ans;
					string tmp2 = ans + str[i];
					if (tmp1 > tmp2)	ans = tmp1;
					else				ans = tmp2;
				}
			}
		}
		printf ("%s\n",ans.c_str());
	}
	return 0;
}