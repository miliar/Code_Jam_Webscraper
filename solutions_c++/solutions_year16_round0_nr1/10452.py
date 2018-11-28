// GCJ 16 Qualification A

#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))

int main(){
  	freopen("A-large.in", "r", stdin);
  	freopen("out.txt", "w", stdout);
	long long int n,t,tmp,x,y,z,it,i,ans;
	cin>>t;
	for(i=1;i<=t;i++){
		int arr[10] = {0};
		cin>>n;
		x = it = y = 0;
		while (x != 10 and it < 500) {
			y++;
			ans = tmp = n*y;
			while(tmp>0){
				z = tmp%10;
				tmp /= 10;
				if (arr[z] == 0)	x++;
				arr[z] = 1;
			}
			it++;
		}
//		cout<<n<<endl;
		if (it>=500)	cout<<"Case #"<<i<<": INSOMNIA\n";
		else 		cout<<"Case #"<<i<<": "<<ans<<endl;
	}
	return 0;
}
