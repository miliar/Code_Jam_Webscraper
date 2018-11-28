#include <iostream>
#include <fstream>
#include <algorithm>
//#define F(x) cout<< #x " = "<<x<<endl;

using namespace std;

struct par
{
      short br;
      bool T;
      char znak;
      void sredi()
      {
            if(br==-4 || (br==-3 && T == true)) znak = 'O';
            else
            if(br==4 || (br == 3 && T == true)) znak ='X';
            else znak = '0';
      }
      friend bool operator <(const par &a,const par &b)
      {
            short A = a.br<0?-a.br:a.br,B = b.br<0?-b.br:b.br;
            return A>B;
      }
};

inline string testiramo(string table[4])
{
      string rez = "";
      bool flagTacke = false;

      //tacke
      for(int i=0;i<4 && !flagTacke;i++)
            for(int j=0;j<4 && !flagTacke;j++)
                  if(table[i][j]=='.')
                        flagTacke = true;
      par tete[10];
      for(int i=0;i<10;i++)
      {
            tete[i].br = 0;
            tete[i].T = false;
      }

      for(int i=0;i<4;i++)
      {
            if(table[i][i]=='T') tete[8].T = true;
            if(table[i][i]=='O') tete[8].br--;
            if(table[i][i]=='X') tete[8].br++;

            //F(table[i][3-i]);

            if(table[i][3-i]=='T') tete[9].T = true;
            if(table[i][3-i]=='O') tete[9].br--;
            if(table[i][3-i]=='X') tete[9].br++;

            for(int j=0;j<4;j++)
            {
                  if(table[i][j]=='T') tete[j].T = true;
                  if(table[i][j]=='O') tete[j].br--;
                  if(table[i][j]=='X') tete[j].br++;

                  if(table[j][i]=='T') tete[j+4].T = true;
                  if(table[j][i]=='O') tete[j+4].br--;
                  if(table[j][i]=='X') tete[j+4].br++;
            }
      }

      sort(tete,tete+10);

      tete[0].sredi();
      if(tete[0].znak!='0')
      {
            rez = tete[0].znak ;
            rez+= " won";
            return rez;
      }
      if(flagTacke)
            return "Game has not completed";
      else return "Draw";
}

int main()
{
    ifstream in("A-small-attempt0.in");
    ofstream out("test.out");

    int testBR = 0;
    in>>testBR;
    for(int i=1;i<=testBR;i++)
    {
          string tabela[4];
          in>>tabela[0]>>tabela[1]>>tabela[2]>>tabela[3];
          //cout<<tabela[0]<<endl<<tabela[1]<<endl<<tabela[2]<<endl<<tabela[3]<<endl;
          out<<"Case #"<<i<<": "<<testiramo(tabela)<<endl;
    }

    in.close();
    out.close();
    return 0;
}
