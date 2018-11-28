#include <bits/stdc++.h>
#define ll long long
using namespace std;


int pos;
int neg;
int nn;
int ans;
char y[1000];

int main(){
    //freopen("E:/h.in","r",stdin);
    //freopen("E:/h3.txt","w",stdout);
    scanf("%d",&nn);
    int t = 1;
    while(nn-->0){
        scanf("%s",y);
        int endpoint = -1;
        neg = 0;
        pos = 0;
        ans = 0;
        int n = strlen(y);
        for(int c = n-1;c>=0;c--){
            if(y[c] == '-'){
                endpoint = c;
                break;
            }
        }

        if(y[0] == '-') neg = 1;
        else pos = 1;
        for(int c = 1;c<=endpoint;c++){
            if(y[c] == '-' and neg){

            }
            else if(y[c] == '-' and pos){
                pos = 0;
                neg = 1;
                ans++;
            }
            else if(y[c] == '+' and neg){
                pos = 1;
                neg = 0;
                ans++;
            }
            else if(y[c] == '+' and pos){

            }
        }
        if(neg) ans++;
        printf("Case #%d: %d\n",(t++),ans);
    }

	return 0;
}
