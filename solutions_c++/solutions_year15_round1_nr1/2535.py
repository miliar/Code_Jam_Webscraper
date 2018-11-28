#include <iostream>
#include <fstream>

//#define ifname "A-small-attempt0.in"
//#define ofname "A-small-attempt0.out"

#define ifname "A-large.in"
#define ofname "A-large.out"


using namespace std;

int m[10000];

int main()
{
    int T,N,x,y,z,i,max_interval;
    
    ifstream is;
    ofstream os;
    is.open(ifname);
    os.open(ofname);

    is  >> T;
    for(x = 1; x <= T; ++x) {
        //cout << "Case #" << x << ": ";
        //cout << endl;
        
        is >> N;
        for(i = 0; i < N; ++i)
            is >> m[i];
            
            
        // first method
        y = 0;
        max_interval = 0;
        for(i = 1; i < N; ++i) {
            if( m[i-1] > m[i] )
                y += m[i-1] - m[i];
            if( m[i-1] - m[i] > max_interval )
                max_interval = m[i-1] - m[i];
        }
        
        // second method
        z = max_interval * (N-1);
        for(i = 0; i < N-1; ++i) {
            if ( m[i] < max_interval )
                z -= (max_interval-m[i]);
        }

        //cout << "Case #" << x << ": ";
        //cout << y << " " << z << endl;   
             
        os << "Case #" << x << ": ";
        os << y << " " << z << endl;

    }

    is.close();
    os.close();

    return 0;
}
