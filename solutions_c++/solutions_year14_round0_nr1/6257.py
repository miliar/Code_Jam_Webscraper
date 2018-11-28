#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");
    int T;
    in>>T;
    for ( int t = 0; t < T; t++)
    {
        int a1;
        in>>a1;
        int card[4];
        for ( int i = 0; i < 4;i++)
        {
            int cardtemp[4];
            for ( int j = 0; j <4;j++)
                in>>cardtemp[j];
            if (i +1 == a1){
                for ( int k = 0; k<4;k++)
                    card[k] = cardtemp[k];
            }
        }
        int a2;
        in>>a2;
         int same = 0;
         int c = 0;
        for ( int i = 0; i < 4; i++)
        {
            int cardtemp[4];
            for ( int j = 0; j <4;j++)
                in>>cardtemp[j];
            if ( i +1==a2){

                for ( int k = 0;k<4;k++)
                {
                    for ( int l =0;l<4;l++)
                    {
                        if (card[k] == cardtemp[l]){
                            same++;c = card[k];
                        }
                    }
                }
            }
        }
        out<<"Case #"<<t+1<<": ";
        if (same ==0)
            out<<"Volunteer cheated!"<<endl;
        else if (same ==1)
            out<<c<<endl;
        else
            out<<"Bad magician!"<<endl;
    }
    in.close();out.close();
}
