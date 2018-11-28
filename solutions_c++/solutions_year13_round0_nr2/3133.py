#include <QFile>
#include <QTextStream>
#include <QStringList>
#include <QVector>

//Artem Klimov's solution
//soved using Qt Framework 4.7.1
//the idea is to make inverse action and see if we could cut a line from shortest hight to the highest


QFile inFile("C:/CodeJam0b/test.in");
QFile outFile("C:/CodeJam0b/output.txt");

int N, M;
int hMatrix[100][100];
bool cMatrix[100][100];

bool FindMinUnchecked(int *iOut, int *jOut)
{
	bool res = 0;
	int tMin = 1000;
	for(int i=0; i<N; i++)
	{
		for(int j=0; j<M; j++)
		{
			if( (cMatrix[i][j]==0) && (hMatrix[i][j]<tMin) )
			{
				res = 1;
				tMin = hMatrix[i][j];
				*iOut = i;
				*jOut = j;
			}
		}
	}

	return res;
}

bool CouldCutToTheCell(int I, int J)
{
	int i;
	for(i=0; i<N; i++)
	{
		if( hMatrix[i][J] > hMatrix[I][J] ) break;  //couldn't cut like that
	}
	if(i==N)
	{
		for(i=0; i<N; i++)  cMatrix[i][J] = 1;
		return 1;
	}

	int j;
	for(j=0; j<M; j++)
	{
		if( hMatrix[I][j] > hMatrix[I][J] ) break;  //couldn't cut like that
	}
	if(j==M)
	{
		for(j=0; j<M; j++)  cMatrix[I][j] = 1;
		return 1;
	}

	return 0;
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
		inData >> N;
		inData >> M;
		
		int i,j;
		for(i=0; i<N; i++)
		{
			for(j=0; j<M; j++) 
			{
				inData >> hMatrix[i][j];
				cMatrix[i][j] = 0;
			}
		}

		bool res = 1;
		while( FindMinUnchecked(&i,&j) )
		{
			if( !CouldCutToTheCell(i,j) )
			{
				res = 0;
				break;
			}
		}
		
		outData << QString("Case #%1: ").arg(t+1);
		if( res )	outData << "YES\r\n";
		else		outData << "NO\r\n";
	}
}
