#include<bits/stdc++.h>
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define res resize
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
vector<bool>licz;
void aktualizuj(int n){
    while(n){
        licz[n%10]=true;
        n/=10;
    }
}
bool policzone(){
    for(int i=0;i<10;i++)
        if(!licz[i])
            return false;
    return true;
}
void solve(int n){
    if(n==0){
        puts("INSOMNIA");
        return;
    }
    licz.clear(); licz.res(10);
    aktualizuj(n);
    int N,i=2;
    while(!policzone()){
        N=n*i; i++;
        aktualizuj(N);
    }
    printf("%d\n",N);
}
int main(){
    int t; scanf("%d",&t);
    for(int i=1;i<=t;i++){
        int n; scanf("%d",&n);
        printf("Case #%d: ",i); solve(n);
    }
	return 0;
}
