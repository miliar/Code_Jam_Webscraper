#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <math.h>
#include <stdint.h>


using namespace std;
typedef  long long  LL;


main() {


  FILE *fin = freopen("D-small-attempt0.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("D-small-attempt0.out", "w", stdout);
	int T,k,c,s;

	cin >> T;

	for(int t = 1; t <= T; t++){
        cin>>k>>c>>s;
        cout << "Case #" << t << ": ";
        if(k==1)
        {
            cout<<k;
        }
        else{

            if(c==1 )
            {
                if(s==k)
                for(int i=1; i<=k;i++) cout<<i<<" ";
                 else cout<<"IMPOSSIBLE";
            }
            else{

                if(s < k-1) cout<<"IMPOSSIBLE";
                else{
                    for(int i=2; i<=k;i++) cout<<i<<" ";
                }
            }

        }

        cout<<"\n"<< endl;


	}
	exit(0);
}
