#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

int main() {
	int TC, n, ans = 0;
	string s;
	scanf("%d", &TC);
	for(int i=1; i<=TC; i++){
                int ppl = 0;
                ans = 0;
                cin>>n>>s;
                for(int j=0; j<=n; j++){
                        int a = s[j] - '0';
                        if(a>0){
                                if(ppl>=j) ppl+=a;
                                else {
                                        ans += j-ppl;
                                        ppl = j+a;
                                }
                        }
                }
                printf("Case #%d: %d\n", i, ans);
	}
}
