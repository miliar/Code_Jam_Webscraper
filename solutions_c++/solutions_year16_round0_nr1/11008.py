#include <QDebug>
#include <QFile>
using namespace std;


int T; //number of cases
int N = 0; //number of sheeps
int Ni = 1; //N times
int N_original = 0;
int Ln = 0; //number of lines in input file
int gotCasesNumbers = 0;
int a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0; //a represents 1 and j is 10.. is seen then value goes to 1

QString Ns;

void separaecompara();

int main()
{
    //qDebug()<<a<<b<<c<<d<<e<<f<<g<<h<<i<<j;
    QFile inputFile("A-large.in");
    if (inputFile.open(QIODevice::ReadOnly))
    {
       QTextStream in(&inputFile);
       while (!in.atEnd())
       {
          Ln++;
          QString line = in.readLine();



          if(gotCasesNumbers==0){
              T = line.toInt();
              gotCasesNumbers=1;
              //qDebug()<<"Total number of cases: "<<T;
          } else {



              N_original = N = line.toInt();

              if(N==0){

                  int novo = Ln-1;
                 // QString nana = QString::number(novo)

                  qDebug().nospace()<<"Case #"<<novo<<": INSOMNIA";

              } else {
                   N = 0;
                   Ni = 1;
                  a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0; //a represents 1 and j is 10.. is seen then value goes to 1

                  separaecompara();

int novo = Ln-1;
                  qDebug().nospace()<<"Case #"<<novo<<": "<<Ns.toInt();

              }






          }

       }
       inputFile.close();
    }


   // qDebug()<<a<<b<<c<<d<<e<<f<<g<<h<<i<<j;
/*
    if(a==1&&b==1&&c==1&&d==1&&e==1&&f==1&&g==1&&h==1&&i==1&&j==1)
        qDebug()<<"Falling asleep...";

*/

   // qDebug()<<"Netpack - Online Solutions! www.netpack.pt";
//return a.exec();

}


void multiplica()
{
    //qDebug()<<"multiplicando "<<N<<" ovelhas por "<<Ni;

    N = N_original*Ni;
    Ni++;
}


void separaecompara()
{

    multiplica();

    //split into each char

    Ns = QString::number(N);

    for(int n=0;n<Ns.length();n++){

       // qDebug()<<"line["<<n<<"]: "<<line[n];

        if(Ns[n]=='0')
            a=1;

        if(Ns[n]=='1')
            b=1;

        if(Ns[n]=='2')
            c=1;

        if(Ns[n]=='3')
            d=1;

        if(Ns[n]=='4')
            e=1;

        if(Ns[n]=='5')
            f=1;

        if(Ns[n]=='6')
            g=1;

        if(Ns[n]=='7')
            h=1;

        if(Ns[n]=='8')
            i=1;

        if(Ns[n]=='9')
            j=1;


    }

      if(a==0||b==0||c==0||d==0||e==0||f==0||g==0||h==0||i==0||j==0)
      {
          separaecompara();
      }
}
