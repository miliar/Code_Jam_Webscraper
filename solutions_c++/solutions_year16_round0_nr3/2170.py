#include <iostream>
#include <string>
#include <bitset>
#include <math.h> 
using namespace std;



string cc;

int tt,anscount(0),anslimit(500);//limit = 50 or 500
long long cur, ans, ccc, pr[11];
bool justgo(true);



int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);

   cout<<"Case #1:"<<endl;

   
    for ( cur = 0x8001; cur <= 0xFFFF && anscount < anslimit; cur += 0x0002) //0xFFFF
    {   justgo = true;
        bitset<16> bs(cur);

        
        for (tt = 2; tt <11 && justgo; ++tt)
        {   
            ccc = 0;
            for (int ii = 0; ii < 16; ++ii)  ccc += pow (tt, ii) * bs[ii];
                
            for(int jj = 3; jj <= sqrt(static_cast<double>(ccc)); jj+=2)
                {
                    if (0 == ccc % jj )
                   {
                        justgo = true;
                        pr[tt]=jj;                        
                        break;

                    }
                    justgo = false;
                }

           // cout<<ccc<< " "<<sqrt(static_cast<double>(ccc))<<endl;
        }
        if (justgo)
            {   anscount++;
                cout<<bs<<bs<<" ";
                for (int mm = 2; mm<11;++mm) cout<<pr[mm]<<" ";
                cout<<endl;
            }
       

    }


	return 0;
}
