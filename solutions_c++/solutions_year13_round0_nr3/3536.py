#include <QVector>
#include <QTextStream>

#include <math.h>

typedef long long llong;
typedef long double ldouble;

bool isPD(llong value)
{
    QString str = QString("%1").arg(value);
    int len = str.length();
    for (int i = 0; i < len / 2; ++i)
    {
        if (str[i] != str[len - 1 - i])
        {
            return false;
        }
    }
    return true;
}

llong getSqrt(llong value)
{
    llong sq = sqrtl(value);
    return sq * sq == value ? sq : -1;
}

bool isSPD(llong value)
{
    llong sq = getSqrt(value);
    return sq > 0 && isPD(sq);
}

llong solve(llong N, llong M)
{
    llong ret = 0;
    for (llong i = N; i <= M; ++i)
    {
        if (isSPD(i) && isPD(i))
        {
            ++ret;
        }
    }
    return ret;
}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        llong N, M;
        ins >> N >> M;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(N, M) << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
    }

    return 0;
}
