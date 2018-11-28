#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <string>

using namespace std;

char buf[10024];

bool Judge(char buf[])
{
    int i = 0;
    while(buf[i++] != '\0');
    i -= 2;
    int j = 0;
    while(j <= i)
    {
	if(buf[j] != buf[i])
	    return false;
	++j;
	--i;
    }
    return true;
}
int main()
{
    //freopen("C-small-attempt0.in", "r", stdin);
    //freopen("cout.data", "w", stdout);
    int T;
    cin >> T;
    for(int iCase = 1; iCase <= T; ++iCase)
    {
	double beg, end;
	cin >> beg >> end;
	double sqrtBeg = floor(sqrt(beg));
	double sqrtEnd = floor(sqrt(end));
	//cout << "sqrtBeg = " << sqrtBeg << endl;
	//cout << "sqrtEnd = " << sqrtEnd << endl;

	if(sqrtBeg*sqrtBeg < beg)
	    sqrtBeg += 1.0;

	long long ans = 0;
	while(fabs(sqrtBeg-sqrtEnd-1) > 0.0000001)
	{
	    sprintf(buf, "%.0lf", sqrtBeg); 
	    if( Judge(buf) )
	    {
		sprintf(buf, "%.0lf", sqrtBeg*sqrtBeg);
		ans += (Judge(buf)?1:0);
	    }
	    sqrtBeg += 1.0;
	}
	cout << "Case #" << iCase << ": " << ans << endl;
    }
    return 0;
}
