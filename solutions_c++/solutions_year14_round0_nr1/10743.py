#include "mainwindow.h"
#include "ui_mainwindow.h"


MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    QFile fileIn("A-small-attempt0.in");
    if( !fileIn.open(QFile::ReadOnly | QFile::Text) )
    {
        ui->textEdit->setText("File open error!");
    }
    else
    {
        QFile fileOut("output.txt");
        if( !fileOut.open(QFile::WriteOnly | QFile::Text) )
        {
            ui->textEdit_2->setText("File save error!");
        }
        QTextStream streamIn(&fileIn);
        QTextStream streamOut(&fileOut);
        int numOfTest, first, second, card;
        streamIn >> numOfTest;

        for(int t = 0; t < numOfTest; t++)
        {
            int matrixFirst[4][4];
            int matrixSecond[4][4];
            QList<int>* line = new QList<int>();
            streamIn >> first;
            ui->textEdit->insertPlainText(QString::number(first) + "\n");
            for(int i = 0; i < 4; i++){;
                for(int j = 0; j < 4; j++){
                    streamIn >> card;
                    ui->textEdit->insertPlainText(QString::number(card) + " ");
                    matrixFirst[i][j] = card;
                    if(i == first - 1)
                    {
                        line->append(card);
                    }
                }
                ui->textEdit->insertPlainText("\n");
            }
            streamIn >> second;
            ui->textEdit->insertPlainText(QString::number(second) + "\n");
            for(int i = 0; i < 4; i++){;
                for(int j = 0; j < 4; j++){
                    streamIn >> card;
                    ui->textEdit->insertPlainText(QString::number(card) + " ");
                    matrixSecond[i][j] = card;
                }
                ui->textEdit->insertPlainText("\n");
            }

            int contains = 0;
            int index;
            for(int i = 0; i < 4; i++)
            {
                if(line->contains(matrixSecond[second - 1][i]))
                {
                    contains++;
                    index = i;
                }
            }

            if(contains == 0)
            {
                ui->textEdit_2->insertPlainText("Case #" + QString::number(t + 1) + ": Volunteer cheated!\n");
                streamOut << "Case #" + QString::number(t + 1) + ": Volunteer cheated!\n";
            }
            if(contains == 1)
            {
                ui->textEdit_2->insertPlainText("Case #" + QString::number(t + 1) + ": " + QString::number(matrixSecond[second - 1][index]) + "\n");
                streamOut << "Case #" + QString::number(t + 1) + ": " + QString::number(matrixSecond[second - 1][index]) + "\n";
            }
            if(contains > 1)
            {
                ui->textEdit_2->insertPlainText("Case #" + QString::number(t + 1) + ": Bad magician!\n");
                streamOut << "Case #" + QString::number(t + 1) + ": Bad magician!\n";
            }
        }
        fileIn.close();
        fileOut.close();
    }
}

MainWindow::~MainWindow()
{
    delete ui;
}
