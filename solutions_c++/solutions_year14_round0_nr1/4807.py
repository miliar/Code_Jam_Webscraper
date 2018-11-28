#include <iostream>
#include <fstream>
using namespace std;

int main()
{

    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    int T;
    int x1[4],x2[4];
    fin>>T;
    for(int t=1;t<=T;t++){
        int card;
        int countCards=0;
        int row;
        int dummy;
        fin>>row;
        for(int i=1;i<=4;i++){
            if(row==i){
                for(int j=0;j<4;j++)
                    fin>>x1[j];
            }
            else{
                for(int j=0;j<4;j++)
                    fin>>dummy;
            }
        }
        fin>>row;
        for(int i=1;i<=4;i++){
            if(row==i){
                for(int j=0;j<4;j++)
                    fin>>x2[j];
            }
            else{
                for(int j=0;j<4;j++)
                    fin>>dummy;
            }
        }
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(x1[i]==x2[j]){
                    countCards++;
                    card=x1[i];
                }

        if(countCards>=2)
            fout<<"Case #"<<t<<": "<<"Bad magician!"<<endl;
        else if(countCards==1)
            fout<<"Case #"<<t<<": "<<card<<endl;
        else
            fout<<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
