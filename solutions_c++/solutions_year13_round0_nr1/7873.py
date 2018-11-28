#include <QtCore/QCoreApplication>
#include <QFile>
#include <QTextStream>

char field[4][4];

enum
{
    _X_=1,
    _O_=10,
    _P_=0,
    _T_=100
};

enum
{
    WIN_X_1=_X_*4,
    WIN_X_2=_X_*3+_T_,
    WIN_O_1=_O_*4,
    WIN_O_2=_O_*3+_T_
};

enum
{
    REZ_TO_X=1,
    REZ_TO_O,
    REZ_NO,  //продолжаем
    REZ_ON   //ничья
};

int test(int in,QFile* f)
{
    QTextStream out(f);
    if ((WIN_O_2==in)||(WIN_O_1==in)) { out << "O won\n"; return REZ_TO_O; }
    if ((WIN_X_2==in)||(WIN_X_1==in)) { out << "X won\n"; return REZ_TO_X;  }
    return 0;
}


int readFile(QFile *f,QFile *f1)
{
    QTextStream in(f);
    int colm[4]={0,0,0,0};
    int str=0;
    int diag[2]={0,0};
    int rz=0;
    char pr=0; //признак наличая пустых мест
    QTextStream out(f1);
    QString line = in.readLine();
    int n = line.toInt();
    line = in.readLine();
    for (int k=0; k<n; k++)
    {
        f1->write("Case #");
        f1->write(QString("%1").arg(k+1).toAscii()+": ");
        for(int i=0;i<4;i++)
        {
            str=0;
            for(int j=0;j<4;j++)
            {
                if (line[j]=='O') {field[i][j]=_O_;}
                if (line[j]=='X') {field[i][j]=_X_;}
                if (line[j]=='.') {field[i][j]=_P_; pr++;}
                if (line[j]=='T') {field[i][j]=_T_;}
                str += field[i][j];
                colm[j] += field[i][j];
                if (i==j) diag[0]+=field[i][j];
                if (3==i+j) diag[1]+=field[i][j];
            }
            rz = test(str,f1);
            if (rz) { for (int ii=0; ii<4-i;ii++) line = in.readLine(); break;}
            else
            line = in.readLine();
        }
        if (!rz) rz+= test(diag[0],f1);
        if (!rz) rz+= test(diag[1],f1);
        for (int ii=0;ii<4;ii++)
            if (!rz) rz+= test(colm[ii],f1);
        if ((!rz)&&(!pr)) f1->write( "Draw\n");
        else if (!rz) f1->write("Game has not completed\n");

        //printf("str = %d diag = %d  diag = %d\n",str,diag[0],diag[1]);
        pr=0;
        str = 0;
        diag[0]=0;
        diag[1]=0;
        colm[0]=0;
        colm[1]=0;
        colm[2]=0;
        colm[3]=0;
        rz=0;
        line = in.readLine();

    }

    /*    while (!line.isNull()) {
        process_line(line);
        line = in.readLine();
    }*/

}


int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);
    QFile fin("/home/kda/gj1/in.txt");
    QFile fout("/home/kda/gj1/out.txt");
    int i,j,k;
    fout.open(QIODevice::WriteOnly | QIODevice::Text);
    fin.open(QIODevice::ReadOnly | QIODevice::Text);
    //fout.write("aaaa");
    readFile(&fin,&fout);
    //out << "bbb" ;
    fout.close();
    exit(0);
    return a.exec();
}


