#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream FILE("i.in",ios::in);
    ofstream OUT("out.txt",ios::out);

    int n;
    FILE>>n;

    for (int d=0;d<n;d++)
    {
        int r,c;
        FILE>>r;
        r-=1;

        int **mas1 = new int* [4];
        for (int i=0;i<4;i++) {
            mas1[i]=new int [4];
            for (int j=0;j<4;j++) {FILE>>mas1[i][j];mas1[i][j]-=1;}
        }

        FILE>>c;
        c-=1;

        int **mas2 = new int* [4];
        for (int i=0;i<4;i++) {
            mas2[i]=new int [4];
            for (int j=0;j<4;j++) {FILE>>mas2[i][j];mas2[i][j]-=1;}
        }

        int *mas=new int [16];
        for (int i=0;i<16;i++) mas[i]=0;

        for (int i=0;i<4;i++) mas[mas1[r][i]]++;
        for (int i=0;i<4;i++) mas[mas2[c][i]]++;


        bool t=0;
        int save;
        for (int i=0;i<16;i++) if (mas[i]>=2) {t=1;save=i;break;}
        bool m=1;
        for (int i=save+1;i<16;i++) {if(mas[i]>=2) {m=0;break;}}

        OUT<<"Case #"<<d+1<<": ";
        if (t && m) OUT<<save+1<<endl;
        else{
            if (!m) OUT<<"Bad magician!"<<endl;
            else OUT<<"Volunteer cheated!"<<endl;
        }
    }




    OUT.close();
    FILE.close();


    return 0;
}
