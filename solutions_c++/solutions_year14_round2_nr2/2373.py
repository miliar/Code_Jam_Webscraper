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
    std::ostream &output = std::cout;
#endif

void SolveCase()
{
   int A, B, K; int res = 0;
   input >> A >> B >> K;
   for(int a = 0; a < A; ++a) {
       for(int b = 0; b < B; ++b) {
           if((a & b) < K) ++res;
       }
   }
   output << res << '\n';
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
