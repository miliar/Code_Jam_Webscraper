#include <QFile>
#include <QtGlobal>
#include <QTextStream>

#include <iostream>

/* Switch between console and file output modes. */
//#define STDOUT

QTextStream input;

#ifndef STDOUT
    QTextStream output;
#else
#   define endl '\n'
    std::ostream &output = std::cout;
#endif

typedef std::vector<int> IntVector;

void SolveCase()
{
    int N; input >> N;
    IntVector A; A.resize(N);
    for(int n = 0; n < N; ++n) input >> A[n];
    IntVector ASorted(A);
    std::sort(ASorted.begin(), ASorted.end());
    int b = 0, e = N - 1;
    qint64 answer = 0;
    for(int n = 0; n < N; ++n) {
        int pos = std::find(A.begin(), A.end(), ASorted[n]) - A.begin();
        int swapsToBegin = pos - b, swapsToEnd = e - pos;
        if(swapsToBegin < swapsToEnd) {
            answer += swapsToBegin;
            while(pos > b) {
                std::swap(A[pos], A[pos - 1]);
                --pos;
            }
            ++b;
        }
        else {
            answer += swapsToEnd;
            while(pos < e) {
                std::swap(A[pos], A[pos + 1]);
                ++pos;
            }
            --e;
        }
    }
    output << answer << endl;
}

int main(int argc, char *argv[])
{
    Q_UNUSED(argc);
    Q_UNUSED(argv);

    QFile infile("input.txt");
    infile.open(QIODevice::ReadOnly);
    input.setDevice(&infile);

#   ifndef STDOUT
        QFile outfile("output.txt");
        outfile.open(QIODevice::WriteOnly);
        output.setDevice(&outfile);
#   endif

    uint T; input >> T;
    for(uint t = 1; t <= T; ++t)
    {
        output << "Case #" << t << ": ";
        SolveCase();
    }

    return 0;
}
