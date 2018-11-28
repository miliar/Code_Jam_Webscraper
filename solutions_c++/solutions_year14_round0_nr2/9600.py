#include <iostream>
#include <string.h>
#include <set>
#include <stdio.h>
#include <algorithm>
using namespace std;
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out", "w", stdout);
	int t;
	cin >> t;
	for (int tt = 0; tt < t; tt++)
	{
		double c,f,x;
		double inc=2.0;
		cin>>c>>f>>x;
		cout<<"Case #"<<tt+1<<": ";
		if(x<c)
        {
            cout<<x/inc<<endl;
            continue;
        }
        double last = x/inc;
        double time=0.0;
        double ret = 10000000.0;
        for(int i=0;i<=100000;i++)
        {
            ret=min(ret,last);
            time+=c/inc;
            inc+=f;
            last = time+(x/inc);
           // cout<<i<<" "<<last<<" "<<time<<endl;
        }
        printf("%.7f\n",ret);
	}
	return 0;
}

