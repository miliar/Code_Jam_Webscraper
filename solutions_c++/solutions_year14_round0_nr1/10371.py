#include<iostream>
#include<fstream>
#include<vector>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;

    fin.open("A-small-attempt0.in");
    fout.open("output1.txt");

    int count=0;
    fin>>count;
    vector<int> myV;
    vector<int> myV2;

    int array1[4][4];
    int array2[4][4];

    for(int i=0;i<count;i++){
        int number1=0;
        int number2=0;
        fin>>number1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++){
                fin>>array1[j][k];
            }
        }

        fin>>number2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++){
                fin>>array2[j][k];
            }
        }


        for(int j=0;j<4;j++)
        {
            myV.push_back(array1[number1-1][j]);
        }

        for(int j=0;j<4;j++)
        {
            myV2.push_back(array2[number2-1][j]);
        }

        vector<int> m;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++){
                if(myV[j]==myV2[k])
                {
                    m.push_back(myV[j]);
                }
            }
        }
        if(m.size()>1){
            fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
        else if(m.size()==1){
            fout<<"Case #"<<i+1<<": "<<m[0]<<endl;
        }
        else if(m.size()==0){
            fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }




        myV.clear();
        myV2.clear();
        m.clear();






    }
    return 0;
}
