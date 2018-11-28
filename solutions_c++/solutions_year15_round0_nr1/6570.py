#include <QFile>
#include <QTextStream>
#include <QSet>

//Artem Klimov's solution
//soved using Qt Framework


QFile inFile("C:/CodeJam/Qualification/A/A-large.in");
QFile outFile("C:/CodeJam/Qualification/A/output.txt");


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
        QList<int> people;  //array of currently sitting people where int value means their current shyness
        int Sm;
        char k;

        inData >> Sm;
        inData >> k;  //read space
        for(int i=0; i<=Sm; i++)
        {
            inData >> k;
            k -= '0';  //to number
            for(int j=0; j<k; j++)
            {
                people.append(i);  //i-shyness
            }
        }

        int Extra=0;
        while(people.count())
        {
            bool someoneStoodUp = 0;
            for(int i=0; i<people.count(); i++)  //let's find who can stand up right now
            {
                if(people[i]<=0) //he's going to stand up, remove him and decrease shyness for everyone else
                {
                    people.removeAt(i);
                    someoneStoodUp = 1;
                    for(int j=0; j<people.count(); j++)     people[j]--;
                }
            }

            if(!someoneStoodUp)  //add a person that will stand up on next iteration
            {
                people.append(0);
                Extra++;
            }
        }

        outData << QString("Case #%1: %2\r\n").arg(t+1).arg(Extra);
    }
}
