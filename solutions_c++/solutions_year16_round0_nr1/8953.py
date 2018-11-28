#include <iostream>
using namespace std;

int main() {
	int t, n, nd, nc, tmp;
	bool dg[10];
	cin >> t;
	for(int tc=1; tc<=t; tc++)
	{
	    cin >> n;
	    if(n == 0)
	    {
	        cout << "Case #" << tc << ": INSOMNIA" << endl;
	        continue;
	    }
	    nd = nc = 0;
	    for(int i=0; i<10; i++)
	        dg[i] = false;
	    while(nd < 10)
	    {
	        nc += n;
	        tmp = nc;
	        while(tmp)
	        {
	            if(!dg[tmp % 10])
	            {
	                nd++;
	                dg[tmp % 10] = true;
	            }
	            tmp /= 10;
	        }
	    }
	    cout << "Case #" << tc << ": " << nc << endl;
	}
	return 0;
}
