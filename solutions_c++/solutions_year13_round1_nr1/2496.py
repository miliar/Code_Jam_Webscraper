//#include <QVector>
#include <QTextStream>
#include <math.h>

typedef long double ldouble;
typedef long long llong;

ldouble mpi = acosl(-1.0L);
ldouble mult = 2.0L / mpi;

llong solve(ldouble r, ldouble t)
{
    /*
    ldouble r2 = floorl(sqrtl(r * r + t * 2));
    qDebug("%d", (int)r2);
//    return QString::number(qlonglong(r2 - r) / 2);
    return qlonglong(r2 - r) / 2;
*/

    llong cnt = 0;
    while(true)
    {
        ldouble S = (r+1)*(r+1) - r*r;
        if (S>t)
            break;
        t -= S;
        ++cnt;
        r += 2;
    }
    return cnt;

}

int main(int argc, char *argv[])
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();
    for (int i = 0; i < T; ++i)
    {
        //long
        double r, t;
        ins >> r >> t;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(r, t) << endl;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
    }

    return 0;
}
