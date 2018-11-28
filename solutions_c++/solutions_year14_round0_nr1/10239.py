#include <QCoreApplication>

#include <QDebug>
#include <QFile>
#include <QTextStream>
#include <QVector>


struct TestCaseInput
{
    unsigned int firstColumn;
    unsigned int firstArrangement[4][4];

    unsigned int secondColumn;
    unsigned int secondArrangement[4][4];
} ;

static unsigned int nCases = 0;
static QVector<TestCaseInput> testCases;


void ConsumeInput(const QString& fileName)
{
    QFile* file = new QFile(fileName);

    if (!file->open(QFile::ReadOnly)) {
        qDebug("This file cannot be opened! Maybe there is a spelling error in the name?");
        return;
    }

    QTextStream input(file);
    nCases = input.readLine().toUInt();

    for(unsigned int ii = 0; ii < nCases; ++ii)
    {
          TestCaseInput testCase;

          input >> testCase.firstColumn;
          for (unsigned int xx = 0; xx < 4; ++xx)
          {
              for (unsigned int yy = 0; yy < 4; ++yy)
              {
                  input >> testCase.firstArrangement[xx][yy];
              }
          }

          input >> testCase.secondColumn;
          for (unsigned int xx = 0; xx < 4; ++xx)
          {
              for (unsigned int yy = 0; yy < 4; ++yy)
              {
                  input >> testCase.secondArrangement[xx][yy];
              }
          }

          testCases.append(testCase);
    }

    file->close();
}

int SolveProblem(const TestCaseInput& testCase)
{
    unsigned int possibleAnswers1 [4];
    unsigned int possibleAnswers2 [4];

    for (unsigned int ii = 0; ii < 4; ++ii)
        possibleAnswers1[ii] = testCase.firstArrangement[testCase.firstColumn - 1][ii];

    for (unsigned int ii = 0; ii < 4; ++ii)
        possibleAnswers2[ii] = testCase.secondArrangement[testCase.secondColumn - 1][ii];

    // Find corresponding number
    bool hasAnswer = false;
    unsigned int answer;

    for (int ii = 0; ii < 4; ++ii)
    {
        for (unsigned int jj = 0; jj < 4; ++jj)
        {
            if (possibleAnswers1[ii] == possibleAnswers2[jj])
            {
                if (hasAnswer == true) // Found a second answer; Bad magician
                    return -1;

                hasAnswer = true;
                answer = possibleAnswers1[ii];
            }
        }
    }

    if (!hasAnswer)
        return 0; // Cheat!
    else
        return answer;
}



int main(int argc, char *argv[])
{
    ConsumeInput("/Users/jellevanmourik/Dropbox/MScMusicTechnology/Qt/GoogleCodeJam/build-GoogleCodeJame-Desktop_Qt_5_2_0_clang_64bit-Debug/TestInput.txt");

    QFile outFile("output.txt");
    if (!outFile.open(QFile::WriteOnly | QFile::Truncate))
        return 1;
    QTextStream output(&outFile);

    for (unsigned int ii = 0; ii < nCases; ++ii)
    {
        int answer = SolveProblem(testCases[ii]);
        output << "Case #" << ii + 1 << ": ";
        switch (answer)
        {
            case 0:
                output << "Volunteer cheated!\n";
                break;
            case -1:
                output << "Bad magician!\n";
                break;
            default:
                output << answer << "\n";
                break;
        }
    }
    outFile.close();
}
