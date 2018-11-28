#include<bits/stdc++.h>
#define int long long int
using namespace std;
#define int int
int main(){
	#define int long long int
	freopen("A-large.in","r",stdin);
	freopen("ans.txt","w",stdout);
	int t;
	cin>>t;
	int f=0;
	while(t--){
		f++;
		int n; cin>>n;
		int a[n+1];
		for(int i=0; i<n; i++) cin>>a[i];
        int sum1=0, sum2=0;
		for(int i=1; i<n; i++){
            if(a[i]<a[i-1]){
                sum1=sum1+a[i-1]-a[i];
            }
        }
        int maxx=0;
        for(int i=1; i<n; i++){
            maxx=max(maxx,a[i-1]-a[i]);
        }
        for(int i=0; i<n-1; i++){
           if(a[i]>maxx) sum2+=maxx;
            else sum2+=a[i];
           
        }
		cout<<"Case #"<<f<<": "<<sum1<<" "<<sum2<<endl;
	}
}
