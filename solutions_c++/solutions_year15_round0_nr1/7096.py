//Requires Qt 5.4.1 built with qtcreator

#include <QCoreApplication>
#include <QCommandLineParser>
#include <QFile>
#include <QTextStream>
#include <QDebug>

quint64 countNumRequired(const QList<int> & shynessList);

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QString inputFilename;
    QString outputFilename;

    QCommandLineParser parser;
    parser.setApplicationDescription("RopeIntranet");
    parser.addHelpOption();
    parser.addVersionOption();
    parser.addPositionalArgument("input", QCoreApplication::translate("main", "Input File."));
    parser.addPositionalArgument("output", QCoreApplication::translate("main", "Output File."));

    parser.process(a);
    const QStringList args = parser.positionalArguments();
    inputFilename = args.at(0);
    outputFilename = args.at(1);

    QFile input(inputFilename);
    input.open(QFile::ReadOnly);
    QTextStream in(&input);

    QFile output(outputFilename);
    output.open(QFile::WriteOnly | QFile::Truncate);
    QTextStream out(&output);

    int numTestCases;
    in >> numTestCases;
    in.readLine();

    QString testCase;
    for ( int testIdx = 0; testIdx < numTestCases; ++testIdx )
    {
        testCase = in.readLine();
        QStringList split = testCase.split(' ');
        int maxShyness = split.at(0).toInt();
        QString shynessString = split.at(1);

        qDebug() << "Parsing list for test" << testCase;
        QList<int> shynessList;
        foreach ( const QChar & shyness, shynessString )
        {
            shynessList.append(shyness.digitValue());
        }

        qDebug() << "Counting num required audience for" << shynessList.size() << "actors.";
        quint64 count = countNumRequired(shynessList);
        qDebug() << "Case #" << testIdx + 1 << ": " << count;
        out << "Case #" << testIdx + 1 << ": " << count << '\n';
        out.flush();
    }

    input.close();
    output.close();

    return 0;
}

quint64 countNumRequired(const QList<int> & shynessList)
{
    quint64 numStanding = 0;
    quint64 numRequired = 0;

    for ( int index = 0; index < shynessList.size(); ++index )
    {
        const int & currShyActors = shynessList.at(index);
        if ( numStanding >= index )
        {
            numStanding += currShyActors;
        }
        else
        {
            int newActors = index - numStanding;
            numRequired += newActors;
            numStanding += newActors + currShyActors;
        }
    }

    return numRequired;
}
