#include <iostream>
#include <string>
#include <string.h>
#include <fstream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cmath>
#include <gmpxx.h>
using namespace std;

int main()
{
    ifstream input;
    input.open("small1.in");
    ofstream output;
    output.open("output.txt");
    int cse=1;
    int t;
    input>>t;

    while(cse<=t)
    {
	int ans,r,c,w;
	input>>r>>c>>w;

	ans=0;
	int n=1;
	while(n*w+w-1<c){n++;}
	ans+=n;cout<<n<<endl;ans*=r;
	if(n*w==c){ans+=w-1;}
	else{ans+=w;}
        output<<"Case #"<<cse<<": "<<ans<<endl;
        cout<<"Case #"<<cse<<": "<<ans<<endl;
        cse++;
    }

    return 0;
}

