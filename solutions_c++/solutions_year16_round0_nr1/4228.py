#include <fstream>

using namespace std;

int main()
{
    int t, i, j, n, ans=0;
    bool cf[10];
    ifstream f1("in.in");
    ofstream f2("out.out");
    f1>>t;
    for(int c=1;c<=t;c++)
    {
        f2 << "Case #" << c << ": ";

        for(i=0;i<10;i++)
            cf[i]=false;

        f1 >> n;
        bool stop=false;
        ans=0;
        for(i=1;i<1000000 && !stop; i++)
        {
            int xn = i * n;
            int cxn = xn;
            while(xn)
            {
                cf[xn%10] = true;
                xn/=10;
            }
            bool adevarat=true;
            for(j=0;j<10;j++)
                if(!cf[j])
                    adevarat=false;
            stop = adevarat;
            if(stop)
                ans = cxn;
        }
        if(ans == 0)
            f2 << "INSOMNIA";
        else
            f2 << ans;

        f2 << "\n";
    }

    f1.close();
    f2.close();
    return 0;
}
