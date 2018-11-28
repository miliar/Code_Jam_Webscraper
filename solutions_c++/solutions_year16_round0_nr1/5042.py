#include <QVector>
#include <QTextStream>

typedef long long lint;

QString solve(int nN)
{
    if (nN == 0)
    {
        return "INSOMNIA";
    }

    QVector<int> N;
    while (nN > 0)
    {
        N.push_back(nN % 10);
        nN /= 10;
    }

    int missingMask = 0x3ff;
    lint curI = 1;
    for (; missingMask; ++curI)
    {
        lint accum = 0;
        for (int j = 0; j < N.size() || accum; ++j)
        {
            if (j < N.size())
            {
                accum = N[j] * curI + accum;
            }
            missingMask &= ~(1 << (accum % 10));
            accum /= 10;
        }
    }
    --curI;

    QString ret;
    lint accum = 0;
    for (int j = 0; j < N.size() || accum; ++j)
    {
        if (j < N.size())
        {
            accum = N[j] * curI + accum;
        }
        ret += ('0' + (accum % 10));
        accum /= 10;
    }

    for (int j = 0; j < ret.size() / 2; ++j)
    {
        QChar ch = ret[j];
        ret[j] = ret[ret.size() - 1 - j];
        ret[ret.size() - 1 - j] = ch;
    }

    return ret;
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        int N;
        ins >> N;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(N) << endl;
    }

    return 0;
}
