//gmw.sjtu@gmail.com

#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    ifstream fin("B-large.in");
    ofstream fout("output.out");

    int N;
    int** field;
    int* row;
    int* column;
    /*
    int field[10][10];
    int row[10];
    int column[10];
    */
    fin>>N;
    for(int n=0;n<N;n++)
    {
        bool flag=true;
        int i=0,j=0;
        int R,C;
        fin>>R>>C;
        row=new int[R];
        column=new int[C];
        field=new int*[R];
        for(i=0;i<R;i++)
        {
            field[i]=new int[C];
            row[i]=1;
            for (j=0;j<C;j++)
            {

                fin>>field[i][j];
                row[i]=max(row[i],field[i][j]);
            }
        }

        for(j=0;j<C;j++)
        {
            column[j]=1;
            for(i=0;i<R;i++)
            {
                 column[j]=max(column[j],field[i][j]);
            }
        }

        //check the elements
        for(i=0;i<R;i++)
        {
            for(j=0;j<C;j++)
            {
                if (field[i][j]<min(row[i],column[j])) {flag=false;break;}
            }
            if (!flag) break;
        }

        fout<<"Case #"<<n+1<<": ";
        if (flag) fout<<"YES"<<endl;
        else fout<<"NO"<<endl;
    }
    fin.close();
    fout.close();
    return 0;
    }
