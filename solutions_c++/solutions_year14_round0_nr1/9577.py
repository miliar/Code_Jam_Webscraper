#include <iostream>
#include <fstream>
#include <vector>
#include<strstream>

using namespace std ;

ifstream in ("A-small-attempt0.in");
ofstream out ("output.txt");

void fillCards(int c[],int row)
{
    int aux;

    for(int i = 0 ; i < 4 ; i++)
    {
        for(int j = 0 ; j < 4 ; j++)
        {
            if( (i+1) == row )
            {
                in>>c[j];
            }
            else
            {
                in>>aux;
            }

        }
    }
}

int getNonZero(vector<int>a)
{
    for(int i = 0; i < a.size() ; i++)
    {
        if(a[i]!=0){return a[i];}
    }
    return -1;
}


string solveNextCase(int thiscase)
{
    int Answer;
    vector<int> possibleAnswers;
    int cards[4];

    in>>Answer;

    fillCards(cards,Answer);

     for(int i=0; i < 4;i++)
    {

        possibleAnswers.push_back(cards[i]);

    }

    in>>Answer;

    fillCards(cards,Answer);

    for(int i = 0 ; i < possibleAnswers.size() ; i++)
    {

       bool found = false;
       for(int j = 0 ; j < 4 ; j++)
       {
           if(possibleAnswers[i]==cards[j])
           {
               found=true;
           }
       }

       if(!found)
       {
           possibleAnswers[i]=0;
       }

    }

    int answers= 0;
    string result;

    for(int o = 0; o < 4 ; o++)
    {
        if(possibleAnswers[o]!=0)
        {
            answers++;
        }

    }

    if(answers == 0)
    {
        out<<"Case #"<<thiscase<<": Volunteer cheated!"<<endl;
    }
    else if(answers> 1)
    {
        out<<"Case #"<<thiscase<<": Bad Magician!"<<endl;
    }
    else
    {
        out<<"Case #"<<thiscase<<": "<<getNonZero(possibleAnswers)<<endl;
    }


    return result;
}




int main ()
{

    int cases ;

    in>>cases;

    for(int k = 0; k < cases ; k++)
    {
        solveNextCase(k+1);
    }


    return 0 ;
}
