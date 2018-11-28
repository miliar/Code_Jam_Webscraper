#include <iostream>
#include <vector>
#include <algorithm>
#include<string>
using namespace std;

long long nwd(long long x, long long y)
{
    if (x == 0)
        return y;
    if (y == 0)
        return x;

    long long k=0;
    while(!((x | y) & 1))
    {
        x>>=1; y>>=1;
        k++;
    }

    while (!(x & 1))
    x>>=1;
    do {
        while (!(y & 1))
        y>>=1;
        if (x > y)
            swap(x, y);
        y=y-x;
    } while (y != 0);
    return (x<<k);
}

bool checker(long long Q) {
    while(Q%2 == 0)
        Q/=2;
    if(Q==1)
        return true;
    else
        return false;
}

int main () {
    ios_base::sync_with_stdio(0);
    int T;
	cin>>T;
	for(int tt=0; tt<T; tt++)
	{
		long long P, Q;
		char slash;
		cin>>P>>slash>>Q;

		long long f=nwd(max(P, Q), min(P, Q));
		P=P/f;
		Q=Q/f;
		bool check=checker(Q);

		cout<<"Case #"<<tt+1<<": ";

		if(check) {
            int x=0, d=2;

			while(d*P<Q)
			{
				x++;
				d*=2;
			}
			x++;
			cout<<x<<endl;
		}
		else
        {
            cout<<"impossible"<<endl;
        }

	}
    return 0;
}
