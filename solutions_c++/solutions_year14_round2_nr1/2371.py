#include <QtCore>

QString getr(QString str)
{
	QString nodup;
	QString regex;
	QChar prev;
	for(int i = 0; i < str.count(); i++)
	{
		if(str.at(i) != prev)
			nodup.append(str.at(i));
		prev = str.at(i);
	}
	for(int i = 0; i < nodup.count(); i++)
	{
		regex = regex + "(" + nodup.at(i) + "+)";
	}
	//qDebug() << regex;
	return regex;
}

int main(int argc, char *argv[])
{
	QCoreApplication a(argc, argv);

	QFile infile("input.txt");
	infile.open(QFile::ReadOnly | QFile::Text);
	QTextStream ins(&infile);
	QFile outfile("output.txt");
	outfile.open(QFile::WriteOnly | QFile::Text);
	QTextStream outs(&outfile);
	int t;
	ins >> t;
	for(int i = 1; i <=t; i++)
	{
		int c;
		QString a, b;
		ins >> c >> a >> b;
		//if(i ==75)
			//qDebug() << a << b;
		int count = 0;
		QString r = getr(a);
		QRegularExpression re(r);
		QRegularExpressionMatch x = re.match(a);
		QRegularExpressionMatch y = re.match(b);
		if(!(x.hasMatch() && y.hasMatch() && x.captured() == a && y.captured() == b))
		{
			outs << "Case #" << i << ": " << "Fegla Won" << endl;
			continue;
		}
		for(int j = 1; j <= r.count()/4; j++)
		{
			QString xx = x.captured(j);
			QString yy = y.captured(j);
			count+=qAbs(xx.count()-yy.count());
		}
		outs << "Case #" << i << ": " << count << endl;
	}
	qDebug() << "Finished" << endl;
	return a.exec();
}
