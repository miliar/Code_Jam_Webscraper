#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
using namespace std;

class count_sheep
{
public:
    count_sheep(int n)
    {
        _n = n;
        digits.resize(10,0);
    }
    void get_digits(int n)
    {

        while(1)
        {
            if(digits[n%10]==false)
                total_digits++;
            digits[n%10]=true;
            if(n/10==0)
                break;
            else
            n/=10;
        }
    }
    int get_result()
    {
        int g=1;
        for(g=1;g<100;g++)
        {

            get_digits(g*_n);
            if(total_digits==10)
                break;
        }
        if(g==100)
            return -1;
        else
        return g*_n;
    }

private:
    vector<bool> digits;
    int total_digits=0;
    int _n;
};

int main()
{
    ifstream in ("qq");
    ofstream out("myout.txt");
    int times;
    in>>times;
    for(int g=0;g<times;g++)
    {
        int n;
        in>>n;
        int res;
        count_sheep cs(n);
        res=cs.get_result();
        if(res==-1)
        {
            out<<"Case #"<<g+1<<": INSOMNIA\n";
        }
        else
        {
            out<<"Case #"<<g+1<<": "<<res<<"\n";
        }
    }
    return true;
}
