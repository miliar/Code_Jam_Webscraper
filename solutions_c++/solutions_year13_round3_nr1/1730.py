#include <iostream>
#include <math.h>
#include <string>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;
const int MNAX = 1000000;

char ss[MNAX] = {0}; 
int s[MNAX] = {0}; 
int ans[MNAX] = {0}; 
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int n,i,j;
	int test;
	cin>>test;
	
	for (int t=1;t<=test;++t){
		scanf("%s",  &ss);
		scanf("%d",  &n);
		int len = strlen(ss);
		for (i=0;i<len;++i){
			ans[i] = 0;
			if (ss[i]=='a' || ss[i]=='e' || ss[i]=='i' || ss[i]=='o' || ss[i]=='u'){
				s[i] = 0;
			}
			else{
				s[i] = 1;
			}
		}

		int lastStart = -1;
		int num1 = 0;
		for (i=0;i<len;++i){
			if (s[i] == 1){
				++num1;
				if (num1>=n){
					lastStart = i-n+1;

					if (i>0){
						ans[i] = ans[i-1] + lastStart + 1;
					}
					else{
						ans[i] = lastStart + 1;
					}

				}
				else{
					if (i>0){
						ans[i] = ans[i-1] + lastStart+1;
					}
					else{
						ans[i] = lastStart+1;
					}
				}

			}
			else{
				num1 = 0;
				if (i>0){
					ans[i] = ans[i-1] + lastStart+1;
				}
				else{
					ans[i] = lastStart+1;
				}
			}
		}


		cout<<"Case #"<<t<<": "<<ans[len-1]<<'\n';
	}

	return 0;
}