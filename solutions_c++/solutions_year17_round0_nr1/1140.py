#include <QFile>
#include <QTextStream>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam2017/Qualification/A/A-large.in");
QFile outFile("C:/CodeJam2017/Qualification/A/output.txt");


int main(int argc, char *argv[])
{
  inFile.open(QFile::ReadOnly);
  outFile.open(QFile::WriteOnly);
  QTextStream inData(&inFile);
  QTextStream outData(&outFile);

  int T;
  inData >> T;

  for(int t=0; t<T; t++) {
    QString str;
    int K;
    inData >> str;
    inData >> K;

    int flips = 0;
    int i = 0;
    for (; i<str.count() && (str.count()-i)>=K; i++) {
      if (str[i] == '-') { //flip
        flips++;
        for (int j=0; j<K; j++) {
          if (str[i+j] == '-') str[i+j] = '+';
          else str[i+j] = '-';
        }
      }
    }

    //check the rest
    bool possible = true;
    for (; i<str.count(); i++) {
      if (str[i] == '-') {
        possible = false;
        break;
      }
    }

    if (possible) outData << QString("Case #%1: %2\r\n").arg(t+1).arg(flips);
    else outData << QString("Case #%1: %2\r\n").arg(t+1).arg("IMPOSSIBLE");
  }
}
