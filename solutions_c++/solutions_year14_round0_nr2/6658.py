#include <QCoreApplication>
#include <QFile>
#include <QString>
#include <QStringList>
#include <QTextStream>
#include <iostream>

int main(int argc, char *argv[]) {
    QCoreApplication a(argc, argv);
    QStringList arglist = a.arguments();
    QString infile;

    if (arglist.size()>1) {
        infile = arglist.at(1);
    }else{
        std::cerr<<"Filename not provided"<<std::endl;
        exit(-1);
    }

    QFile file(infile);
    if(!file.open(QIODevice::ReadOnly)) {
        std::cerr<<"Filename not valid"<<std::endl;
        exit(-2);
    }else{
        std::cout<<"File \"" << infile.toStdString() << "\" valid"<<std::endl;
    }

    QFile ofile("out.in");
    ofile.open(QIODevice::WriteOnly | QIODevice::Text);
    QTextStream out(&ofile);

    QTextStream in(&file);
    int numCases = in.readLine().toInt();


    for (int cas=0; cas<numCases; ++cas) {
        QStringList qrow1 = in.readLine().split(" ");
        std::vector<double> row1(qrow1.size());
        for (size_t i=0; i<qrow1.size(); ++i) {
            row1[i] = qrow1.at(i).toDouble();
        }

        double C=row1[0], F=row1[1], X=row1[2];
            std::cout<<"C="<<C<<", F="<<F<<", X="<<X<<std::endl;
        double currspeed=2.0;
        double tcc=0, tesp=X/currspeed, tccp=C/(currspeed), tespp=X/(currspeed+F);
        double time=0.0;

        while(tesp>tcc+tespp){
            time+=tcc;
            tcc = C/(currspeed);
            tesp = X/(currspeed);
            currspeed+=F;
            tccp = C/(currspeed);
            tespp = X/(currspeed);
        }
        time+=tesp;

        std::cout<<"Case #"<<cas+1<<": "<<time<<"\n";
        out<<"Case #"<<QString::number(cas+1)<<": "<<QString::number(time, 'f', 7)<<"\n";
    }



    file.close();
    ofile.close();

    return 0;
}
