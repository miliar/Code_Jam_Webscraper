#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>
#include <algorithm>
#include <iomanip>

#define OUT out
#define GETC ;

#ifndef OUT
#define OUT cout
#endif

#ifndef GETC
#define GETC getchar();
#endif

using namespace std;

int main()
{
    ifstream in("files/file.in");
    ofstream out("files/file.out");

    int ncases=0;
    in >> ncases;

    for(int ncase=1; ncase<= ncases; ++ncase)
    {
        OUT << "Case #" << ncase << ": ";
        int nrows=0, nrow, ncols=0, ncol, fixedrate=-1, tmp=-1, ret2num=0;
		long long ret1=0, ret2=0;
		vector<int> nums;
        
        in >> ncols;
        nrows = 1;

        for (nrow=0; nrow < nrows; ++nrow)
        {
            for (ncol=0; ncol < ncols; ++ncol) 
            {
                int n;
                in >> n;

				fixedrate = max(fixedrate, tmp-n);
				nums.push_back(n);
				if(tmp > n) ret1 += tmp - n;
				tmp = n;
            }
        }
		fixedrate = max(0, fixedrate);

		for (ncol=0; ncol < ncols-1; ++ncol) 
			ret2 += min(nums[ncol],fixedrate);

		OUT << ret1 << " " << ret2;
            
        if(ncase != ncases) OUT << endl;
    }
    in.close();
    out.close();
    
    GETC
    return 0;
}
