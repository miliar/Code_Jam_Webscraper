/*
if i have n farms,
the cookie rate is (n F + 2) / second
so the time to additional farm is C / (nF+2)

Now, think.
if you really need n farms,
you should buy as early as possible
so we can divide the whole time period as two.
first, buy farms as possible
second, do nothing until success (X cookies)

first period takes sum_n C/(nF+2)
second period takes X/(nF+2)
*/

struct game{
    long double C,F,X;
};


#include <fstream>
#include <vector>

using std::vector;

vector<game> games;
vector<long double> result;

int main(){
    size_t cases;
    std::ifstream ifp("input.txt");
    ifp >> cases;
    games.resize(cases);
    for (size_t i = 0; i < cases; ++i)
        ifp >> games[i].C >> games[i].F >> games[i].X;
    ifp.close();
    
    for (size_t i = 0; i < cases; ++i){
        vector<long double> timecase(1,0);
        while (timecase.size() < 3 || *(timecase.end()-3) > *(timecase.end()-2) ){
            timecase.push_back(timecase.back()+games[i].C/((timecase.size()-1)*games[i].F+2));
            (*(timecase.end()-2))+=games[i].X/((timecase.size()-2)*games[i].F+2);
        }
        result.push_back(*(timecase.end()-3));
    }
    
    std::ofstream ofp("output.txt");
    ofp << std::fixed;
    ofp.precision(7);
    for (size_t i = 0; i < cases; ++i)
        ofp << "Case #"<<i+1<<": "<<result[i] << std::endl;
    ofp.close();
}