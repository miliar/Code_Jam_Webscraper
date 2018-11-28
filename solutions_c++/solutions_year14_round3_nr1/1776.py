#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std ;

int main() {
    freopen("A-small-attempt0.in","r",stdin) ;
    freopen("A.out","w",stdout) ;
    int Test ; cin >> Test ;
    for ( int i = 1 ; i <= Test ; i ++ ) {
        int p,q;
		scanf("%d/%d",&p,&q);
		double ans=(double)p/q;
		int ret=0;int j=0;
		while(ans-0.0>0.00000001 || ans-0.0<-0.00000001) {
			ans=ans*2;
			j++;
			if(ans-1.0>-0.00000001) {
				if(!ret) ret=j;
				ans=ans-1.0;
			}
			if(j>40) break;
		}
		cout << "Case #" << i << ": " ;
		if(j<=40 && ret) cout<<ret<< "\n" ;
		else cout<<"impossible\n";
    }
}
