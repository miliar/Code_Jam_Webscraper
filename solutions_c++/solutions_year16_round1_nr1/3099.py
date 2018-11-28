#include <fstream>
#include <string>
#include <deque>

std::ifstream in("in.txt");
std::ofstream out("out.txt");

int main()
{
    int T;
    in >> T;
    for (int t = 0; t < T; ++t) {
        std::string w;
        in >> w;
        std::deque<char> deq;
        deq.push_back(w[0]);
        for (size_t i = 1; i < w.size(); ++i)
            if (deq.front() > w[i])
                deq.push_back(w[i]);
            else
                deq.push_front(w[i]);
        std::string res(deq.begin(), deq.end());
        out << "Case #" << t + 1 << ": ";
        out << res << std::endl;
    }
    return 0;
}
