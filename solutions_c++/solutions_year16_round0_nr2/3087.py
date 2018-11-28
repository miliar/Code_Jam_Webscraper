#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <fstream>
#define mod 1000000007
#define size 1000007
#define ll long long
#define INF LLONG_MAX
#define fr(i,a,b) for(i=a;i<=b;i++)
using namespace std;

char str[1000];

char swap(char ch){
    if(ch=='+')
        return '-';
    return '+';
}

void flip(int j){
    for(int i=0;i<j/2;i++){
        char temp = str[i];
        str[i] = swap(str[j-i-1]);
        str[j-i-1] = swap(temp);
    }
    if(j%2)
        str[j/2] = swap(str[j/2]);
}

int main() {
    freopen("inp.txt","r",stdin);
	freopen("out.txt","w",stdout);
    ios::sync_with_stdio(0);
    int tc,i,count,n;
	ll ans;
    cin>>tc;
    for(int t=1;t<=tc;t++){
		cin>>str;
		ans = 0;
		n = strlen(str);
		while(1){
            for(i=n-1;i>=0;i--){
                if(str[i]=='+')
                    n--;
                else
                    break;
            }
            if(!n) break;
            count = 0;
            for(i=n-1;i>=0;i--){
                if(str[i]=='-')
                    count++;
                else
                    break;
            }
            if(count==n){
                ans++;
                break;
            }
            if(str[0]=='+'){
                flip(i+1);
                ans++;}
            flip(n);
            //cout<<str;
            ans++;
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	return 0;
}
