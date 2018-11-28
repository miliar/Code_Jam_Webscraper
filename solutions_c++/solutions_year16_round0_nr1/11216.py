#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int ndigits( int x )
{
	return x > 0 ? (int) log10 ((double) x ) + 1 : 1;
}
#define bitget(n,i) (n>>i)&1
int main()
{
	int n,T, nd;
	bool asleep = false;
	ifstream infile;
	ofstream outfile;
	int j,d;
	int x = 0;
    n = 3;int n2,l;
	
	infile.open("A-large.in");
	outfile.open("problemA.out");

	infile >> T;
	
    for(int i = 1; i <= T; i++){
        asleep = false;
        x = 0;
        infile >> n;
        l=1;
        cout << "Case: " << i << "  test number: " << n << endl;
        while(!asleep){
            nd = ndigits(n*l);
        //    cout << "n: " << l*n << "   ndigits: " << nd << endl;
            n2 = (l++)*n;
            for(j = 0; j < nd; j++)
            {
                d = n2%10;
                n2/=10;
          //      cout << "current digit: " << d << endl;
                x |= 1 << d;
                if(x == 1023) asleep = true;
             //   for(int k = 0; k < 10; k++){
             //       cout << (bitget(x,k));
             //   }
           //     cout << " <= x => " << x << "   asleep status: " << asleep;
            }
            //cout << endl << endl;
            //cin.get();
            if(n == (l*n)) {
                outfile << "Case #" << i << ": INSOMNIA" << endl;
                break;
            }
            if(asleep){
                outfile << "Case #" << i << ": " << (l-1)*n << endl;
            }
        }
    }
	
}
