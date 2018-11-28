#include <iostream>
#include <string>
#include <fstream>

using namespace std;

std::ifstream infile("A-large.in");
std::ofstream outfile ("out.txt",std::ios::out);

int main()
{
	unsigned long test_n;
    infile>>test_n;
    cout<<test_n<<endl;
    unsigned long long nums;
    for(unsigned long i=1; i<=test_n; ++i) {
    	infile>>nums;


        if(nums==0){
        	outfile<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        unsigned long hash=0;
        unsigned long long n=1;
        unsigned long long prev = 0;
        while(hash!=0x3ff){
            unsigned long long tmp = nums*n;
            prev=tmp;
            ++n;
            while(tmp) {
                hash=hash |  (0x0001<<(tmp%10));
                tmp/=10;
            }
        }
        outfile<<"Case #"<<i<<": "<<prev<<endl;
    }

    outfile.close();
}
