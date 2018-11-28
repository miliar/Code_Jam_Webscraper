#include <QVector>
#include <QTextStream>

typedef long long lint;

QString solve(int K, int C, int S)
{
    if (S < K)
    {
        return "IMPOSSIBLE";
    }

    QString ret;
    for (int i = 0; i < K; ++i)
    {
        lint base = i;
        for (int j = 0; j < C - 1; ++j)
        {
            base = base * K + i;
        }
        ret.append(QString("%1 ").arg(QString::number(base + 1)));
    }
    return ret.trimmed();
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        int K, C, S;
        ins >> K >> C >> S;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(K, C, S) << endl;
    }

    return 0;
}
