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
        int ans1 = in.readLine().toInt();

        std::cout<<"ans1="<<ans1<<std::endl;
        for (int i=0; i<ans1-1; ++i) in.readLine();
        QStringList qrow1 = in.readLine().split(" ");
        std::vector<int> row1(qrow1.size());
        for (size_t i=0; i<qrow1.size(); ++i) {
            row1[i] = qrow1.at(i).toInt();
        }
        for (int i=ans1; i<4; ++i) in.readLine();

        int ans2 = in.readLine().toInt();
        std::cout<<"ans2="<<ans2<<std::endl;
        for (int i=0; i<ans2-1; ++i) in.readLine();
        QStringList qrow2 = in.readLine().split(" ");
        std::vector<int> row2(qrow2.size());
        for (size_t i=0; i<qrow2.size(); ++i) {
            row2[i] = qrow2.at(i).toInt();
        }
        for (int i=ans2; i<4; ++i) in.readLine();

        int isthere=0;
        int whois=-1;
        for (size_t i=0; i<row1.size(); ++i){
            for (size_t j=0; j<row2.size(); ++j){
                if (row1[i]==row2[j]) {
                    whois=row1[i];
                    isthere++;
                }
            }
        }

        if (isthere==0){
            std::cout<<"Case #"<<cas+1<<": Volunteer cheated!"<<"\n";
            out<<"Case #"<<QString::number(cas+1)<<": Volunteer cheated!"<<"\n";
        }
        if (isthere==1){
            std::cout<<"Case #"<<cas+1<<": "<<whois<<"\n";
            out<<"Case #"<<QString::number(cas+1)<<": "<<QString::number(whois)<<"\n";
        }
        if (isthere>1){
            std::cout<<"Case #"<<cas+1<<": Bad magician!"<<"\n";
            out<<"Case #"<<QString::number(cas+1)<<": Bad magician!"<<"\n";
        }
    }



    file.close();
    ofile.close();

    return 0;
}
