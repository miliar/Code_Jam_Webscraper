#include <QtCore>

double get(double c, double f, double prev, int count)
{
	return prev + c/(f*count);
}

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);
	QFile inputFile("C:/Users/Igor/Desktop/B-large.in");
	inputFile.open(QFile::ReadOnly | QFile::Text);
	QTextStream inStream(&inputFile);
	QFile outputFile("C:/Users/Igor/Desktop/B-large.out");
	outputFile.open(QFile::WriteOnly | QFile::Text);
	QTextStream outStream(&outputFile);
	int t;
	inStream >> t;
	for(int i = 0; i < t; i++)
	{
		double c,f,x;
		inStream >> c >> f >> x;

		double mintime = x/2;
		int count = 0;
		double gt = 0;
		double prevtime = -1;
		while(true)
		{
			gt += c/(2+f*count);
			double time = gt+x/(2+(count+1)*f);
			if (time < mintime)
				mintime = time;
			if(time > prevtime && prevtime != -1)
				break;
			count++;
			prevtime = time;
		}
		outStream << "Case #" << i+1 << ": " << QString::number(mintime, 'g',16) << endl;
	}
	qDebug() << "fin";

	return a.exec();
}
