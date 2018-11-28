#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework

QFile inFile("C:/CodeJam2016/Qualification/B/B-large.in");
QFile outFile("C:/CodeJam2016/Qualification/B/output.txt");

void FlipAndInvert(bool *S, int i1, int i2)
{
    bool temp;
    while(i1<=i2)
    {
        temp = S[i1];
        S[i1] = !S[i2];
        S[i2] = !temp;
        i1++;
        i2--;
    }
}

int main(int argc, char *argv[])
{
    inFile.open(QFile::ReadOnly);
    outFile.open(QFile::WriteOnly);
    QTextStream inData(&inFile);
    QTextStream outData(&outFile);

    int T;
    inData >> T;
    bool S[100];
    char c;
    inData >> c;  //\r
    //inData >> c;  //\n

    for(int t=0; t<T; t++)
    {
        int N=0;
        for(;;)
        {
            inData >> c;
            if(c=='-')       S[N] = 0;
            else if(c=='+')  S[N] = 1;
            else  //\r
            {
                //inData >> c;  //\n
                break;
            }
            N++;
        }

        int flips = 0;
        int firstMinus, lastMinus = N-1;
        for( ; (lastMinus>=0) && (S[lastMinus]==1); lastMinus--) ;

        while(lastMinus>=0)
        {
            for(firstMinus=0; S[firstMinus]==1; firstMinus++) ;  //count all '+' at the top that we want to make '-'

            if(firstMinus>0)  //there are some pluses at the top, let's make them minuses
            {
                FlipAndInvert(S, 0, firstMinus-1);
                flips++;
            }

            FlipAndInvert(S, 0, lastMinus);
            flips++;

            for( ; (lastMinus>=0) && (S[lastMinus]==1); lastMinus--) ;
        }

        outData << QString("Case #%1: %2\r\n").arg(t+1).arg(flips);
    }
}
