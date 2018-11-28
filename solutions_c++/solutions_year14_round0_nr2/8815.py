#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
    int k;
    ifstream a ("q2.txt");
    ofstream b ("a2.txt");
    a>>k;
    for (int i=0; i<k; i++)
    {
        double c;
        double f;
        double x;
        a>>c;
        a>>f;
        a>>x;
        char z[1];
        a.getline(z,1);
        double past=0;
        double rate=2.0;
        double future=c/rate;
        int count=0;
        past=x/rate;
        future=future+x/(rate+f);
        rate=rate+f;
        while(past>future)
        {
            past=future;
            future=future-(x/rate)+(c/rate);
            future=future+x/(rate+f);
            rate=rate+f;
        }
        b<<std::fixed;
        b<<setprecision(7)<<"Case #"<<i+1<<": "<<past<<endl;
    }
}
