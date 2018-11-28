#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <iomanip> 
using namespace std;

void outPut(const vector<char>& nArrR, int nr, int nc, bool bSwap)
{
     if (!bSwap)
     {
        for (int i = 0; i < nr; i++)
        {
            for (int j = 0; j < nc; j++)
            {
                cout << nArrR[i*nc+j];
            }
            cout << endl;
        }           
     }
     else
     {
        for (int i = 0; i < nc; i++)
        {
            for (int j = 0; j < nr; j++)
            {
                cout << nArrR[j*nc+i];
            }
            cout << endl;
        }    
     }    
}


void solve(int nr, int nc, int nm)
{
     vector<char> nArrR;    
     
     bool bswap = false;
     if (nr < nc)
     {
        bswap = true;
        std::swap(nr, nc);
     }
     if (nm == 0)
     {
          nArrR.resize(nr*nc, '.');
          nArrR[0] = 'c';
          return outPut(nArrR, nr, nc, bswap);
     }
     if (nc==1)
     {
        nArrR.resize(nr, '.');
        nArrR[0] = 'c';
        for (int i = 0; i < nm; i++)
        {
            nArrR[nr-i-1] = '*';
        }
        return outPut(nArrR, nr, nc, bswap);       
     }
     
     if (nr*nc-nm  == 1)
     {
        nArrR.resize(nr*nc, '*');
        nArrR[0] = 'c';
        return outPut(nArrR, nr, nc, bswap);
     }
     
     if (nr*nc-nm < 4)
     {
         cout << "Impossible" << endl;
         return;   
     }
     
     if (nc==2)
     {
        if (nm%2 != 0)
        {
            cout << "Impossible" << endl;
            return;
        }
        nArrR.resize(nr*nc, '.');
        nArrR[0] = 'c';
        for (int i = 0; i < nm; i++)
        {
            nArrR[nr*nc-i-1] = '*';
        }
        return outPut(nArrR, nr, nc, bswap);
     }
     
     int nNoM = nr*nc-nm;
     nArrR.resize(nr*nc, '*');
     //要把没有雷的地方分解一下
     for (int i = 2; i < nc; i++)
     {
         for (int j = i; j < nr; j++)
         {
             if (i*j > nNoM)
             {
                break;
             }
             if ((i+1)*(j+1) <= nNoM)
             {
                continue;
             }
             //这是一个可能的分解
             int nFenpei = nNoM-i*j;
             if (nFenpei == 1)
             {
                 continue;
             }
             bool bJump = true;
             int ni = 0; 
             int nj = 0;
             if (nFenpei == 0)
             {
               bJump = false;
             }
             else if (nFenpei <= j)
             {
               bJump = false;
               nj = nFenpei;  
             }
             else if (nFenpei >= 4)
             {
               bJump = false;
               ni = nFenpei/2;
               if (ni>i)
               {
                  ni = i;         
               }
               nj = nFenpei - ni; 
             }
             
             if (bJump)
             {
                continue;
             }
             //分解成功 
             
             for (int m = 0; m < i; m++)
             {
                 for (int n = 0; n < j; n++)
                 {
                     nArrR[n*nc+m] = '.';
                 }                 
             }
             for (int m = 0; m < ni; m++)
             {
                 nArrR[j*nc+m] = '.';
             }
             for (int m = 0; m < nj; m++)
             {
                 nArrR[m*nc+i] = '.';
             }
             
             nArrR[0] = 'c';
             return outPut(nArrR, nr, nc, bswap);
         }
     }     
     cout << "Impossible" << endl;
     return;
}

int main()
{
	freopen("in.txt", "r", stdin);
    //cout<<setiosflags(ios::fixed)<< setiosflags(ios_base::showpoint)<< setprecision(10);
	freopen("out.txt", "w", stdout);

	int TestCase;
	cin >> TestCase;
	for (int CaseID = 1; CaseID <= TestCase; CaseID ++)
	{
        int nr, nc, nm;
        cin >> nr >> nc >> nm;
		cout << "Case #" << CaseID << ":" /* << nr << " " << nc << " " << nm*/<< endl;
    	
		solve(nr, nc, nm); 
	}
	return 0;
}

