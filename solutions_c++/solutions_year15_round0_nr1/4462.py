#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <map>
#include <math.h>

using namespace std;

int main()
{
    int T,Smax;
    char Sarray[1001];
    int Scum[1001];
    int i,j,k,x;
    int s;
    int res;
    cin >> T;
    
    for (x=0;x<T;x++)
    {
        cin >> Smax;
        cin >> Sarray;
	for (i=0;i<Smax;i++)
		Scum[i]=0;
	Scum[0] = Sarray[0]-'0';
	res = 0;
	for (i=1;i<=Smax;i++)
	{
		int cnt = Sarray[i]-'0';
		if (Scum[i-1]>=i)
			Scum[i] = Scum[i-1]+cnt;
		else
		{
			res+=(i-Scum[i-1]);
			Scum[i] = i+cnt;
		}
	}
        
        printf("Case #%d: %d\n",x+1,res);

    }
}
