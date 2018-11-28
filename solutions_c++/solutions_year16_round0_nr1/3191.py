#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int tracker[10];

void track()
{
    for(int i=0; i<10;i++)
    tracker[i] = 10;
}



main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert( fin!=NULL );
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;

	cin >> T;



	for(int t = 1; t <= T; t++){
            track();
		LL N,NN;
		cin>>N;
		if(N==0)
        {
        cout << "Case #" << t << ": ";
        cout <<"INSOMNIA"<< endl;
        }
        else{
		NN=N;
		for(int i=1; ;i++)
        {
            NN = N*i;
            int n = NN, ck=1;
            while(n>0)
            {
                int a;
                a  = n%10;
                tracker[a] = a;
                n /= 10;
            }

            for(int j=0;j<10;j++)
            {
                if(tracker[j] == 10)
                {
                    ck = 0;
                    break;
                }
            }
            if(ck==1)  break;
        }
		cout << "Case #" << t << ": ";
		cout << NN<< endl;

	}
	}
	exit(0);
}
