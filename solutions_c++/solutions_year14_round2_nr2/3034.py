#include<cstdlib>
#include<cstdio>
#include <iostream>   // std::find
#include <vector>       // std::vector

using namespace std;
int solve(int a,int b,int k){
int cnt=0;
for(int i=0;i<a;i++){
    for(int j=0;j<b;j++){
          //  cout<<(i&j)<<endl;
            if((i&j)<k)
            {cnt++;
            }
}
}
return cnt;
}
int main() {
	freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-small-attempt0.in", "rt", stdin);
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
        int a,b,k;
        cin>>a>>b>>k;
		cout << "Case #" << i + 1 << ": "<<solve(a,b,k)<< endl;
	}
		return 0;
}

