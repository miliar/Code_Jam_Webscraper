#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int Test_case;
    input>>Test_case;
    cout<<"Test_case:" <<Test_case;
    for(int t=1;t<=Test_case;t++)
    {
        output<<"Case #"<<t<<": ";
        int M,N;
        input>>N>>M;
        int tab[N][M];
        for(int i=0;i<N;i++)
        {
            for(int j=0;j<M;j++)
            {
                input>>tab[i][j];
            }
        }
        bool finish=1;
        for(int i=0;i<N &&finish;i++)
        {
            for(int j=0;j<M && finish;j++)
            {
                bool blocked_largeur=0;
                bool blocked_hauteur=0;
                int tester=tab[i][j];
                    for(int h=0;h<N;h++)
                    {
                        if(tab[h][j]>tester)
                        {
                            //cout<<"BLOCKED EN HAUTEUR:"<<endl;
                            blocked_hauteur=1;
                            break;
                        }
                    }
                    for(int h=0;h<M;h++)
                    {
                        if(tab[i][h]>tester)
                        {
                            //cout<<"BLOCKED EN HAUTEUR:"<<endl;
                            blocked_largeur=1;
                            break;
                        }
                    }

                    if(blocked_hauteur && blocked_largeur)
                    {
                        output<<"NO"<<endl;
                        finish=0;
                    }
            }
        }
        if(finish)
            output<<"YES"<<endl;
    }
}
