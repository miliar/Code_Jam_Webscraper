#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
#include <string>

using namespace std;

int main()
{
    ifstream in ("A-large.in");
    ofstream out ("output.out");
    string number;
    int T, N, m_i, m_ii, max, eaten1, eaten2;

    if(in.is_open()){
        in >> T;
        for (int i = 1; i <= T; i++){
            eaten1 = 0;
            eaten2 = 0;
            in >> N;
            int line[N];
            in >> number;
            max = 0;
            stringstream convert(number);
            convert >> line[0];
            m_ii = line[0];
            for (int j = 1; j < N; j++){
                m_i = m_ii;
                in >> number;
                stringstream convertt(number);
                convertt >> line[j];
                m_ii = line[j];
                if (m_i > m_ii) {
                    eaten1 += (m_i - m_ii);
                    if (m_i - m_ii > max)
                        max = (m_i - m_ii);
                }
            }

            for (int j = 0; j < N-1; j++){
                m_i = line[j];
                if (m_i > max)
                    eaten2 += max;
                else
                    eaten2 += m_i;
            }
            out << "Case #" << i << ": " << eaten1 << " " << eaten2 << endl;
        }
        in.close();
    }
    out.close();
    return 0;
}

