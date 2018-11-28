#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    int i,j,k,t;
    double a,c,f,x,s;
    double ans;
    int cc = 0;
    ifstream fin("cookie.in");
    ofstream fout("cookie.out");

    fin>>t;
    while (cc<t){
        cc++;

        fin>>c>>f>>x;
        a = 2;
        ans = 0; s = 0;
        while (ans == 0){
            if ((x/a) < (c/a + x/(a + f))){
                s = s + x/a;
                ans = s;
            }
            else{
                s = s + c/a;
                a = a + f;
            }
        }

        fout<<setiosflags(ios::fixed)<<setprecision(7)<<"Case #"<<cc<<": "<<double(ans)<<endl;
    }
    return 0;
}
