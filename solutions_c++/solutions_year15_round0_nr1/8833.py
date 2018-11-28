#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;

int main() {

	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );

	int tt,t;
	cin >> tt;
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d:", t );
        int maxShy;
        string audience;
        cin>>maxShy>>audience;
        int must=0,total=0;
        for (int i = 0; i <= maxShy; ++i)
        {
        	int diff = 0;
        	if(total<i){
        		diff = i-total;
        		must+=diff;
        	}
        	total += audience[i]-'0'+diff;
        }
        cout<<" "<<must<<endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}