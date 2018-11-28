//Problem A. Magic Trick
//Confused? Read the quick-start guide.
//Small input
//6 points
//Solve A-small
//You may try multiple times, with penalties for wrong submissions.
//Note: To advance to the next rounds, you will need to score 25 points. Solving just this problem will not give you enough points.

//Problem

//Recently you went to a magic show. You were very impressed by one of the tricks, so you decided to try to figure out the secret behind it!

//The magician starts by arranging 16 cards in a square grid: 4 rows of cards, with 4 cards in each row. Each card has a different number from 1 to 16 written on the side that is showing. Next, the magician asks a volunteer to choose a card, and to tell him which row that card is in.

//Finally, the magician arranges the 16 cards in a square grid again, possibly in a different order. Once again, he asks the volunteer which row her card is in. With only the answers to these two questions, the magician then correctly determines which card the volunteer chose. Amazing, right?

//You decide to write a program to help you understand the magician's technique. The program will be given the two arrangements of the cards, and the volunteer's answers to the two questions: the row number of the selected card in the first arrangement, and the row number of the selected card in the second arrangement. The rows are numbered 1 to 4 from top to bottom.

//Your program should determine which card the volunteer chose; or if there is more than one card the volunteer might have chosen (the magician did a bad job); or if there's no card consistent with the volunteer's answers (the volunteer cheated).

//Solving this problem

//Usually, Google Code Jam problems have 1 Small input and 1 Large input. This problem has only 1 Small input. Once you have solved the Small input, you have finished solving this problem.

//Input

//The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a line containing an integer: the answer to the first question. The next 4 lines represent the first arrangement of the cards: each contains 4 integers, separated by a single space. The next line contains the answer to the second question, and the following four lines contain the second arrangement in the same format.

//Output

//For each test case, output one line containing "Case #x: y", where x is the test case number (starting from 1).

//If there is a single card the volunteer could have chosen, y should be the number on the card. If there are multiple cards the volunteer could have chosen, y should be "Bad magician!", without the quotes. If there are no cards consistent with the volunteer's answers, y should be "Volunteer cheated!", without the quotes. The text needs to be exactly right, so consider copying/pasting it from here.

//Limits

//1 ≤ T ≤ 100.
//1 ≤ both answers ≤ 4.
//Each number from 1 to 16 will appear exactly once in each arrangement.

//Sample


//Input

//Output

//3
//2
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16
//3
//1 2 5 4
//3 11 6 15
//9 10 7 12
//13 14 8 16
//2
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16
//2
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16
//2
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16
//3
//1 2 3 4
//5 6 7 8
//9 10 11 12
//13 14 15 16

//Case #1: 7
//Case #2: Bad magician!
//Case #3: Volunteer cheated!


#include <QtCore/QCoreApplication>
#include <QtDebug>
#include <QString>
#include <QList>
#include <QFile>
#include <QStringList>

QList<int> readRow(QFile& caseFile)
{
    QString rowOfText = QString(caseFile.readLine());
    QStringList cardText = rowOfText.split(" ");

    QList<int> retVal;
    foreach(QString singleCard, cardText)
    {
        retVal.append(singleCard.toInt());
    }

    return retVal;
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    
    if (argc != 3)
    {
        qDebug() << "Usage:  ./magic in.txt out.txt";
        return 0;
    }

    QFile inputFile(a.arguments().at(1));
    QFile outputFile(a.arguments().at(2));

    inputFile.open(QIODevice::ReadOnly);
    outputFile.open(QIODevice::WriteOnly);

    int totalCases = QString(inputFile.readLine()).toInt();

    for(int caseNum = 1; caseNum <= totalCases; caseNum++)
    {
        int firstChoice = QString(inputFile.readLine()).toInt();

        QList<int> firstCardsSelected;
        for(int firstPassRowIndex = 1; firstPassRowIndex <= 4; firstPassRowIndex++)
        {
            if (firstPassRowIndex == firstChoice)
            {
                firstCardsSelected = readRow(inputFile);
                qDebug() << "Volunteer 1st selected one of the following:" << firstCardsSelected;
            }
            else
            {
                qDebug() << "Did not select (1st pass):  " << readRow(inputFile);
            }
        }

        int secondChoice = QString(inputFile.readLine()).toInt();

        QList<int> secondCardsSelected;
        for(int secondPassRowIndex = 1; secondPassRowIndex <= 4; secondPassRowIndex++)
        {
            if (secondPassRowIndex == secondChoice)
            {
                secondCardsSelected = readRow(inputFile);
                qDebug() << "Volunteer 2nd selected one of the following:" << secondCardsSelected;
            }
            else
            {
                qDebug() << "Did not select (2nd pass):  " << readRow(inputFile);
            }
        }

        int numMatchingCards = 0;
        int whatWasTheCard = 0;
        for(int fcIndex = 0; fcIndex < firstCardsSelected.count(); fcIndex++)
        {
            for(int scIndex = 0; scIndex < secondCardsSelected.count(); scIndex++)
            {
                if (firstCardsSelected[fcIndex] == secondCardsSelected[scIndex])
                {
                    whatWasTheCard = firstCardsSelected[fcIndex];
                    qDebug() << "Volunteer selected" << whatWasTheCard;

                    numMatchingCards++;
                }
            }
        }

        QString outputText;
        switch(numMatchingCards)
        {
        case 0:
            qDebug() << "No card selected cheater";
            outputText = QString("Case #%1: Volunteer cheated!\n").arg(caseNum);
            outputFile.write(outputText.toAscii().data());
            break;

        case 1:
            qDebug() << "Selected Card" << whatWasTheCard;
            outputText = QString("Case #%1: %2\n").arg(caseNum).arg(whatWasTheCard);
            outputFile.write(outputText.toAscii().data());
            break;

        default:
            qDebug() << "Magician is an idiot";
            outputText = QString("Case #%1: Bad magician!\n").arg(caseNum);
            outputFile.write(outputText.toAscii().data());
        }



    }







    inputFile.close();
    outputFile.close();
}
