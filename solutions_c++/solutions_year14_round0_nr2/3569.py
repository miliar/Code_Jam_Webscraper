#include <fstream>
#include <iomanip>
using namespace std;

ifstream in("data.in");
ofstream out("data.out");

int main()
{
    double C,F,X,cookieRate;
    double elapsedTime, timeToStop, timeWithAnotherFerm;
    bool finished;
    int T;
    in >> T;

    out << setprecision(7) << fixed;

    for(int t = 1; t <= T; t++){

        in >> C >> F >> X;

        cookieRate = 2;
        elapsedTime = 0;
        finished = false;

        while(!finished){
            timeToStop = X / cookieRate;

            //vad daca e buna achizitia unei ferme imi imbunatateste timpul
            timeWithAnotherFerm = X /(cookieRate + F) + C/cookieRate;

            if(timeWithAnotherFerm < timeToStop) {
                elapsedTime += C/cookieRate;
                cookieRate += F;
            }
            else {
                finished = true;
            }
        }
        out <<"Case #" <<t<<": " << elapsedTime + X/cookieRate << '\n';
    }
    return 0;
}
