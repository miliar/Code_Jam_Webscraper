#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

void problemA(const std::string ifname, const std::string ofname)
{
    std::ifstream ifs(ifname);
    std::ofstream ofs(ofname);
    if(!ifs.is_open() || !ofs.is_open()) {
        throw std::runtime_error("cannot open the io stream");
    }

    int ncases = 0;
    ifs >> ncases;
    if(ncases > 100) {
        throw std::runtime_error("exeed max case number 100");
    }

    for(int t = 0;t < ncases; t++) {
        int nlevels = 0;
        ifs >> nlevels;
        std::cout << nlevels << " ";
        std::vector<int> naudienceperlevel(nlevels+1, 0);
        std::string inputstr;
        ifs >> inputstr;
        for(int i=0;i<nlevels+1;i++) {
            naudienceperlevel[i] = inputstr[i] - '0';
            std::cout << inputstr[i];

        }
        std::cout << std::endl;

        // accumulate the audience;
        std::cout << naudienceperlevel[0];
        for(int i=1;i<naudienceperlevel.size();i++){
            naudienceperlevel[i] += naudienceperlevel[i-1];
            std::cout << naudienceperlevel[i];
        }
        std::cout << std::endl;

        // check the first smaller value
        int nshort=0;
        int i=-1;
        for(i=naudienceperlevel.size()-2;i>=0;i--){
            if(naudienceperlevel[i] < i+1) {
                nshort = std::max(nshort, i+1-naudienceperlevel[i]);
            }
        }
        ofs << "Case #"<<t+1<<": " << nshort << std::endl;
    }
    ofs << std::endl;
    ifs.close();
    ofs.close();
}

int main(int nargc, char* argv[])
{
    problemA(argv[1], argv[2]);
    return 0;
}

