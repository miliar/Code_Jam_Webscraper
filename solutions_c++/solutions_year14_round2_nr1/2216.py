#include <QTextStream>
#include <QFile>
#include <QStringList>
#include <QGenericMatrix>
#include <QVector>
#include <QString>

#include <QDebug>

#include <cmath>

bool fastTest(QVector<QString> strings);
int slowTest(QVector<QString> strings);
QVector<QString> trimStrings(QVector<QString> strings, int pos, int* changes);
QVector<QString> extendStrings(QVector<QString> strings, int pos, int* changes);
int maxLength(QVector<QString> strings);

int main(int argc, char** argv)
{
  QFile inFile("../input/input.txt");
  if(!inFile.open(QIODevice::ReadOnly)) {
    qDebug() <<  "ReadError:" << inFile.errorString();
    return -1;
  }
  QTextStream in(&inFile);
  QFile outFile("../input/output.txt");
  if(!outFile.open(QIODevice::WriteOnly)) {
    qDebug() <<  "WriteError:" << outFile.errorString();
    return -1;
  }
  QTextStream out(&outFile);
  out.setRealNumberNotation(QTextStream::FixedNotation);
  out.setRealNumberPrecision(7);
  int numberOfCases = in.readLine().toInt();
  qDebug() << "Cases:" << numberOfCases;
  for (int c = 1; c <= numberOfCases; ++c)
  {
    int N = in.readLine().toInt();
    qDebug() << "N = " << N;
    QVector<QString> strings;
    for (int i = 0; i < N; ++i)
    {
      strings.append(in.readLine());
    }
    qDebug() << strings;
    if (!fastTest(strings))
    {
      out << "Case #" << c << ": Fegla Won" << endl;
    }
    else
    {
      out << "Case #" << c << ": " << slowTest(strings) << endl;
    }
  }
  inFile.close();
  outFile.close();
  return 0;
}

int slowTest(QVector<QString> strings)
{
  int pos = 0;
  int changes = 0;
  while (pos < maxLength(strings))
  {
    int diff = 0;
    foreach (QString string, strings)
    {
      
      if (string[pos] != string[pos +1])
      {
	diff++;
      }
    }
    if ((diff > strings.size()/2) && (diff != strings.size()))
    {
      int tmp = 0;
      strings = trimStrings(strings, pos, &tmp);
      changes = changes + tmp;
    }
    else if ((diff != strings.size()) && (diff != 0))
    {
      int tmp = 0;
      strings = extendStrings(strings, pos, &tmp);
      changes = changes + tmp;
    }
    pos++;
  }
  return changes;
}

QVector< QString > trimStrings(QVector< QString > strings, int pos, int* changes)
{
  QVector< QString > res;
  foreach(QString string, strings)
  {
    if (string[pos] == string[pos+1])
    {
      string.remove(pos, 1);
      *changes = *changes + 1;
    }
    res.append(string);
  }
  return res;
}

QVector< QString > extendStrings(QVector< QString > strings, int pos, int* changes)
{
  QVector< QString > res;
  foreach(QString string, strings)
  {
    if (string[pos] != string[pos+1])
    {
      string.insert(pos, string[pos]);
      *changes = *changes + 1;
    }
    res.append(string);
  }
  return res;
}

int maxLength(QVector< QString > strings)
{
  int max = 0;
  foreach(QString string, strings)
  {
    if (string.size() > max)
    {
      max = string.size();
    }
  }
  return max;
}

bool fastTest(QVector< QString > strings)
{
  QVector<QString> res;
  foreach(QString string, strings)
  {
    for (int i = 0; i < string.size() - 1; ++i)
    {
      if (string[i] == string[i+1])
      {
	string.remove(i, 1);
	i = i - 1;
      }
    }
    res.append(string);
  }
  for (int i = 0; i < res.size()-1; ++i)
  {
    if (res[i] != res[i+1])
    {
      return false;
    }
  }
  return true;
}