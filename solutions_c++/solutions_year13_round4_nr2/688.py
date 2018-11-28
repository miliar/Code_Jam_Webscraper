#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

long long mypow(int N)
{
     long long c = 1;
     if (N == 0) return c;
     for (int i = 0 ; i < N ; i++)
         c = c*2;     
     return c;
}

long long mynewpow(int N)
{
     long long c = 1;
     if (N == 0) return 0;
     if (N == 1) return 1;
     for (int i = 1 ; i < N ; i++)
         c = c*2;     
     return c;
}
   
int main()
{
 //  ifstream fin("B-small-attempt2.in");
 //  ofstream fout("B-small-attempt2.out");
    ifstream fin("B-large.in");
    ofstream fout("B-large.out");

    int T; fin >> T; int N; long long P;
        
        
    for (int t = 1 ; t <= T; t++)
    {  
		fout << "Case #" << t << ": ";
		
		long long maxN = 0;
        long long minN = 0;
        
		fin >> N >> P;
		long long total = mypow(N);
		long long temp = total;
		int c = 0;
		while (P < temp) {c++; temp = temp/2;}
        maxN = (total-1)-(mypow(c)-1);

        temp = total;
        long long tempP = P;
        c = 0;
        if (P == total) minN = total-1;
        else
        {        
        while (true) 
        {
              temp = temp/2; 
              if (tempP <= temp) break; 
              c++; 
              tempP = tempP-temp;
        }
        if (c == 0) minN = 0;
        else
        {
            for (int k = 0 ; k < c ; k++)
                minN += mypow(k+1);
        }
        }
         fout << minN << " " << maxN << endl;
    }
}
