#include <string>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <iostream>
#include <fstream>


using namespace std;


int main() {
    ifstream in("../input.txt");
//    streambuf *cinbuf = std::cin.rdbuf(); //save old buf
    cin.rdbuf(in.rdbuf()); //redirect std::cin to in.txt!
    ofstream out("../output.txt");
//    streambuf *coutbuf = std::cout.rdbuf(); //save old buf
    cout.rdbuf(out.rdbuf());

    int T;
    cin >> T;

    /**
     * S = "-+-++-"   длина строки N = 6. пусть лопатка K = 3. тогда N-K+1=4 способов переворота:
     *      ~~~       1-й способ
     *       ~~~      2-й способ
     *        ~~~     3-й способ
     *         ~~~    4-й способ
     * любой их этих переовротв мы либо сделаем, либо нет - делать его дважды нет смысла -
     * это всё равно что его не делать.
     * рассмотрим самый левый блинчик - его затрагивает только 1 из 4 способов переворота.
     * значит, если первый блинчик "-", то мы делаем первый переворот, иначе - не делаем.
     * в нашем примере - делаем переворот и получаем:
     * S'= +(-+++-) - первый символ нас уже не интересует. рассматриваем подстроку со второго и т.д.
     *       +--+-
     *        ++--  - и получаем последнюю подстроку, содержащую "-" => impossible
     */
    for (int i = 0; i < T; ++i) {
        string S;
        int K;
        cin >> S;
        cin >> K;
        int result = 0;

        do {
            if (S[0] == '-') {
                // flip first 'k' pancakes
                for (int j = 0; j < K; ++j)
                    S[j] = (S[j] == '+') ? '-' : '+';
                result++;
            }
            S = S.substr(1);
        } while (S.size() >= K);
        if (S.find('-') != string::npos)
            result = -1;

        cout << "Case #" << (i + 1) << ": ";
        cout << ((result == -1) ? "IMPOSSIBLE" : to_string(result)) << "\n";
    }


    // cout << fixed << result;

//    cin.rdbuf(cinbuf);   //reset to standard input again
    // getchar();

    return 0;
}
