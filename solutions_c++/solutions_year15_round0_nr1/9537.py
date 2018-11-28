#include <fcntl.h>
#include <iostream>
#include <unistd.h>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <sys/wait.h>
#include <vector>


using namespace std;


int main()
{
	int t,i;
	cin >> t;

	for(int j=1;j<=t;j++){
		int smax;
		cin >> smax;

		string audience;
		cin >> audience;

		
		int scount=0;
		int needed=0;

		
		for (i = 0; i < smax+1; ++i)
		{
			if(scount < i){ 
				needed++;
				scount++;
			}
			scount += audience[i] - '0';
		}

		cout << "Case #" << j << ": " << needed << endl;

	}

}