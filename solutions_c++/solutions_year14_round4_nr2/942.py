#include<bits/stdc++.h>
#define sc(n) scanf("%d",&n)
#define pn(n) printf("%d\n",n)
#define slc(n) scanf("%lld",&n)
#define pln(n) printf("%lld\n",n)
#define ps(n) printf("%d ",n) //
using namespace std;
int a[1010], b[1010];
int n;

int sl(int l, int r){
    for(int i = r; i >= l + 1; i--){
        int temp = b[i];
        b[i] = b[i-1];
        b[i-1] = temp;
    }
}
int sr(int r, int j){
    for(; j <= r - 1; j++){
        int temp = b[j];
        b[j] = b[j + 1];
        b[j + 1] = temp;
    }
}

int fun(){
	int l = 1, r = n,ans=0;
	int i,j;
    sort(a + 1, a + n + 1);
    for(i = 1; i <= n; i++){
        int x = a[i];
        for(j = 1; j <= n; j++){
            if(x == b[j]) 
			break;
        }
        if(j - l <= r - j){
            sl(l, j);
            ans += j - l;
            l ++;
        }
        else{
            sr(r, j);
            ans += r - j;
            r --;
        }
    }
    return ans;
}
int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t,test = 1;
    cin>>t;
    while(t--){
	    cin>>n;
	    for(int i = 1; i <= n; i++){
			cin>>a[i];
			b[i] = a[i];
	    }
    	cout<<"Case #"<<(test++)<<": "<<fun()<<endl;
    }
    return 0;
}


