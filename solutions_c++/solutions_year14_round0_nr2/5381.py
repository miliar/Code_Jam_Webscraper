#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

int main() {
    int T,c;
    int ans = -1;
    fin>>T;

    for (c=1; c<=T; ++c) {
        double farm_cost, farm_extra, goal;
        fin>>farm_cost>>farm_extra>>goal;

        int n = 0;
        double delta, ans = goal/2;
        while (ans > 0) {
            ++n;
            delta = (goal - farm_cost)/(2 + (n-1)*farm_extra) - goal/(2 + n*farm_extra);
            if (delta <= 1e-9) break;
            ans -= delta;
        }

        // output
        fout<<"Case #"<<c<<": ";
        
        fout<< fixed << setprecision(7) <<ans;
        
        fout<<endl;
    }
    return 0;
}
