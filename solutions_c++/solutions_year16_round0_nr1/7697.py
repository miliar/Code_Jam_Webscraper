#include "countingsheep.h"

CountingSheep::CountingSheep()
{

}

void CountingSheep::solve(const char *inputPath, const char *outputPath)
{
    // read input
    std::ifstream in(inputPath);

    in >> T;
    ns.reserve(T);

    for(int j=0; j<T && in.good(); ++j){
        unsigned long n;
        in >> n;
        ns.push_back(n);
    }

    in.close();

    std::ofstream out;
    out.open(outputPath);

    // solve problem
    for (unsigned int i = 0; i <ns.size(); ++i){
        unsigned long n = ns[i];

        if (n == 0) {
            out << "Case #" << i+1 << ": INSOMNIA\n";
            continue;
        }

        int flag = 0;
        unsigned int count = 0;
        unsigned long number;

        do {
            number = (++count)*n;
            while (number>0) {
                flag |= 0x1 << number%10;
                number /= 10;
            }
        } while (flag != 1023 && count <=1000000);

        if (count > 1000000) { // 1 million, that "should" be INSOMNIA; TODO
            out << "Case #" << i+1 << ": INSOMNIA\n";
        }
        else {
            char buffer[1024];
            sprintf(buffer, "Case #%u: %lu\n", i+1, n*count);
            out << buffer;
        }
    }

    out.close();
}
