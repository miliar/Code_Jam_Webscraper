#include <QtCore>

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QFile inputFile("input.txt");
	inputFile.open(QFile::ReadOnly | QFile::Text);
	QTextStream inputStream(&inputFile);
	QFile outputFile("output.txt");
	outputFile.open(QFile::WriteOnly | QFile::Text);
	QTextStream outputStream(&outputFile);
	int t;
	inputStream >> t;
	for(int i = 1; i <= t; i++)
	{
		QString str;
		inputStream >> str;
		QStringList list = str.split("/");
		int p, q;
		p = list.first().toInt();
		q = list.last().toInt();
		int res = p;
		int count = 0;
		while(res < q)
		{
			res = res*2;
			count++;
		}
		int temp = 2;
		bool ok = false;
		while(temp <= q)
		{
			if(temp == q)
				ok = true;
			temp = temp*2;
		}
		if(p>q || !ok)
		{
			//qDebug() << str << "imp";
			outputStream << "Case #" << i << ": impossible" << endl;
		}
		else
		{
			//qDebug() << str << count;
			outputStream << "Case #" << i << ": " << count << endl;
		}
	}
	qDebug() << "Finished" << endl;

	return a.exec();
}
