#include <iostream>
#include <string>
#include <sstream>
using namespace std;

void outputarray(int to_out[][4])
{
    for(int i = 0; i < 4; i++)
    {
        for (int j=0; j < 4; j++)
        {
            cout << to_out[i][j] << " ";
        }
        cout << endl;
    }
}

int CardProblem()
{

    int row1, row2;         //input

    int cards1[4][4];        //row by column
    int cards2[4][4];

    int equalities = 0;         //number of equalities at the end

    cin>>row1;
    row1-=1;

    for(int i=0;i<4;i++)
    {
        //cout << "Cardinput \n";
        for(int j=0;j<4;j++)
        {
            cin >> cards1[i][j];
            //cout << cards2[i][j];
        }
        //cout << endl;
    }

    cin>>row2;
    row2-=1;


    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            cin >> cards2[i][j];
        }
    }

    int equalcase=0;

    // cout << "input1"<< endl;
    // outputarray(cards1);

    // cout << "input2"<< endl;
    // outputarray(cards2);

    //cout << "row being selected: "<< endl;
    for (int i=0; i<4; i++)
    {
        //cout<<cards1[row1][i]<< endl;
        for (int j=0; j<4;j++)
        {
            if(cards1[row1][i]==cards2[row2][j])
            {
                equalcase=cards2[row2][j];
                equalities++;
            }
        }
    }
    
    string functionout="";

    if (equalities>1)
    {
       return -1; 
    }

    else if (equalities == 1)
    {
        return equalcase;
    }

    else
    {
        return 200;
    }

}


string output="";
stringstream ss;

int main(){
    int inputs = 0;
    
    cin>>inputs;

    
    for (int i=0; i<inputs; i++)
    {
        int successval = CardProblem();

        if( successval == 200 ){
            ss<<"Case #"<<(i+1)<<": "<<"Volunteer cheated!"<<"\n";
        }

        else if ( successval == -1 ){
            ss<<"Case #"<<(i+1)<<": "<<"Bad magician!"<<"\n";
        }
        else
        {
            ss<<"Case #"<<(i+1)<<": "<<successval<<"\n";
        }
        
    }

    cout << ss.str();

    return 0;

}
