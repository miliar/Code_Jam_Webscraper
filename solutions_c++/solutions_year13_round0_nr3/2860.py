#include <QFile>
#include <QTextStream>
#include <math.h>


//Artem Klimov's solution
//soved using Qt Framework 4.7.1


QFile inFile("C:/CodeJam0c/test.in");
QFile outFile("C:/CodeJam0c/output.txt");

quint64 A,B;

bool IsPalindrome(quint64 N)
{
	QString tStr = QString("%1").arg(N);
	int count = tStr.length();
	for(int i=0; i<count; i++)
	{
		if( tStr[i] != tStr[count-i-1] )  return 0;
	}

	return 1;
}

quint64 CountPalindrNumb()
{
	quint64 N=0;

	//let's walk thru squares interval, since it's much smaller
	quint64 sqA = sqrt((long double)A); 
	quint64 sqB = sqrt((long double)B);

	//just to be sure that we got first correct number
	sqA--;
	while( sqA*sqA < A ) sqA++;
	sqB++;
	while( sqB*sqB > B ) sqB--;

	for(quint64 i=sqA; i<=sqB; i++)
	{
		if( IsPalindrome(i) )
			if( IsPalindrome(i*i) )  N++;
	}

	return N;
}

int main(int argc, char *argv[])
{
	inFile.open(QFile::ReadOnly);
	outFile.open(QFile::WriteOnly);
	QTextStream inData(&inFile);
	QTextStream outData(&outFile);

	int T;
	inData >> T;

	for(int t=0; t<T; t++)
	{
		inData >> A;
		inData >> B;
		
		outData << QString("Case #%1: %2\r\n").arg(t+1).arg(CountPalindrNumb());
	}
}
