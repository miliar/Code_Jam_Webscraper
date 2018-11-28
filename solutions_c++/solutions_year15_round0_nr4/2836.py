#include <vector>
#include <iostream>
#include <string>
#include <math.h>

using namespace std;

int main()
{
    int N,i,j,k=0; cin>>N;
    string rich="RICHARD";
    string gabe="GABRIEL";

    for(i=0; i<N; i++)
    {
        int x,r,c;cin>>x>>r>>c;
        string winner=rich;

        if(x<7) {
            if(r*c%x == 0)
            {
                //cout << x << " " << r << " " << c << endl;
                winner=gabe;

                if(x>2)
                {
                    int s = min(r,c);
                    if(s>(x/2))
                        winner=gabe;
                    else
                        winner=rich;
                }
            }
        }
        
        cout << "Case #" << ++k << ": " << winner << endl;
    }

    return 0;
}

