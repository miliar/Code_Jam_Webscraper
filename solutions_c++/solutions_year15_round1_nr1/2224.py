#include <bits/stdc++.h>
using namespace std;

int main() {

	freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);

	long long int t;
	cin>>t;
	for(int j=1;j<=t;j++){
    long long int n,i,y=0,z=0,p=0;
    cin>>n;
    long long int a[n];
    for(i=0;i<n;i++){
      cin>>a[i];
    }


    for(i=0;i<n-1;i++){
        if(a[i+1]<a[i]){
             y+=a[i]-a[i+1];
             p=max(p,a[i]-a[i+1]);
        }
    }
    for(i=0;i<n-1;i++){
        z+=min(p,a[i]);
    }

		cout<<"Case #"<<j<<": "<<y<<" "<<z<<endl;

	}
	return 0;
}

