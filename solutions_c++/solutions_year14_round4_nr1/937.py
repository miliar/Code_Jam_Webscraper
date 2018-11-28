#include <QFile>
#include <QtGlobal>
#include <QTextStream>

#include <iostream>

/* Switch between console and file output modes. */
// #define STDOUT

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
    int N, X;
    input >> N >> X;
    IntVector fileSize(N);
    for(int n = 0; n < N; ++n) input >> fileSize[n];
    std::sort(fileSize.begin(), fileSize.end());
    int answer = 0;
    while(!fileSize.empty()) {
        ++answer;
        int s = fileSize.back();
        fileSize.pop_back();
        if(!fileSize.empty()) {
            IntVector::iterator i = fileSize.end() - 1, e = fileSize.begin();
            do {
                if(*i + s <= X) {
                    fileSize.erase(i);
                    break;
                }
                else --i;
            } while(i >= e);
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
