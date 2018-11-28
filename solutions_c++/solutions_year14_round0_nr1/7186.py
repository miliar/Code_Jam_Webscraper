#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    int T;
    ifstream fin;
    ofstream fout;
    fin.open("A-small-attempt4.in");
    fout.open("Output.txt");
    //cin >> T;
    fin >> T;
    int i,j,k,fansw,sansw;
    int farr[4][4],sarr[4][4];


    for(i=1;i<=T;i++){
                // reading arrangements
        //cin >> fansw;
        fin >> fansw;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                //cin >> farr[j][k];
                fin >> farr[j][k];
        //cin >> sansw;
        fin >> sansw;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                //cin >> sarr[j][k];
                fin >> sarr[j][k];

                //comparing rows
        int counter=0;
        int rightpos=0;
        for(j=0;j<4;j++)
            for(k=0;k<4;k++)
                if((farr[fansw-1][j])==(sarr[sansw-1][k])) {
                    counter++;
                    rightpos=k;             // rightpos has the right value only in the case of counter==1 , as we want
                }
        if (counter==0)
            //cout <<  "Case #"<<i<<": Volunteer cheated!" << endl;
            fout <<  "Case #"<<i<<": Volunteer cheated!" << endl;
        else if(counter==1)
            //cout << "Case #"<<i<<": "<<sarr[sansw-1][rightpos]<<endl;
            fout << "Case #"<<i<<": "<<sarr[sansw-1][rightpos]<<endl;
        else
            //cout << "Case #"<<i<<": Bad magician!"<< endl;
            fout << "Case #"<<i<<": Bad magician!"<< endl;
        }
    fin.close();
    fout.close();
    return 0;
}
