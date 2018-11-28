#include <QVector>
#include <QTextStream>

typedef QVector<QVector<int> > Lawn;

bool solve(Lawn& lawn, int N, int M)
{
    QVector<int> maxN, maxM;
    maxN.resize(N);
    maxM.resize(M);

    for (int i = 0; i < N; ++i)
    {
        maxN[i] = lawn[i][0];
    }
    for (int j = 0; j < M; ++j)
    {
        maxM[j] = lawn[0][j];
    }
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            maxN[i] = std::max(maxN[i], lawn[i][j]);
            maxM[j] = std::max(maxM[j], lawn[i][j]);
        }
    }
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < M; ++j)
        {
            if (lawn[i][j] < maxN[i] && lawn[i][j] < maxM[j])
            {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        Lawn sample;
        int N, M;
        ins >> N >> M;
        sample.resize(N);
        for (int j = 0; j < N; ++j)
        {
            sample[j].resize(M);
            for (int k = 0; k < M; ++k)
            {
                ins >> sample[j][k];
            }
        }
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << (solve(sample, N, M) ? "YES" : "NO") << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
    }

    return 0;
}
