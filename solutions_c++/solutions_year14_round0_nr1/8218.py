#include <QtCore>

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QFile inputFile("C:/Users/Igor/Desktop/A-small-attempt0.in");
	inputFile.open(QFile::ReadOnly | QFile::Text);
	QTextStream inStream(&inputFile);
	QFile outputFile("C:/Users/Igor/Desktop/A-small-attempt0.out");
	outputFile.open(QFile::WriteOnly | QFile::Text);
	QTextStream outStream(&outputFile);	
	int t;
	inStream >> t;
	for(int i = 0; i < t; i++)
	{
		int cards[4][4];
		int row1;
		inStream >> row1;
		for(int z = 0; z < 4; z++)
		{
			for(int x = 0; x < 4; x++)
			{
				int temp;
				inStream >> temp;
				cards[z][x] = temp;
			}
		}
		int newcards[4][4];
		int row2;
		inStream >> row2;
		row1--;
		row2--;
		for(int z = 0; z < 4; z++)
		{
			for(int x = 0; x < 4; x++)
			{
				int temp;
				inStream >> temp;
				newcards[z][x] = temp;
			}
		}
		int count = -1;
		for(int z = 0; z < 4; z++)
		{
			for(int x = 0; x < 4; x++)
			{
				if(newcards[row2][x] == cards[row1][z])
					if(count == -1)
						count = cards[row1][z];
					else
						if(count >= 0)
							count = -2;
			}
		}
		if(count == -1)
			outStream << "Case #" << i+1 <<": " << "Volunteer cheated!" << endl;
		if(count == -2)
			outStream << "Case #" << i+1 <<": " << "Bad magician!" << endl;
		if(count >= 0)
			outStream << "Case #" << i+1 <<": " << count << endl;
		qDebug()  << "Case #" << i <<": " << count;
	}

	return a.exec();
}
