#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
using namespace std;

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    cin>>t;
	for (int j = 0; j < t; ++j)
	{
		int x, r, c;
		cin>>x>>r>>c;
		string res = "RICHARD";
		if (r * c % x == 0 && (x < 3 || min(r, c) > x/2 && max(r, c) >= x))
			res = "GABRIEL";
		cout<<"Case #"<<j + 1<<": "<<res<<endl;		
	}
    return 0;
}