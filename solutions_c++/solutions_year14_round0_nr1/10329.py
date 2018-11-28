#include <iostream>
#include <fstream>
using namespace std;
ifstream f("A-small-attempt1.in");
ofstream g("date.out");
int T;
int first_grid[5][5], second_grid[5][5];
int answer_one = 0;
int answer_two = 0;
bool found;

int first_arr[10];
int second_arr[10];

//FIRST GRID
void read_first_grid()
{
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            f>>first_grid[i][j];
}

//SECOND GRID
void read_second_grid()
{
    for(int i=1;i<=4;i++)
        for(int j=1;j<=4;j++)
            f>>second_grid[i][j];
}

//////////////////////////////////////////
int main()
{
    int result=0;

    f>>T;
    int q=0;

    for(int t=1;t<=T;t++){

        q=0;

        f>>answer_one;
        read_first_grid();

        f>>answer_two;
        read_second_grid();

        //NO CHEAT METHOD

        for(int i=1;i<=4;i++)
            first_arr[i]=first_grid[answer_one][i];

        for(int i=1;i<=4;i++)
            second_arr[i]=second_grid[answer_two][i];

        for(int i=1;i<=4;i++){
            for(int j=1;j<=4;j++){
                if(first_arr[i]==second_arr[j]){
                    result=first_arr[i];
                    found=true;
                    q++;
                    break;
                }
            }
        }

        if(found==true){
            if(result!=0&&q==1){
                g<<"Case #"<<t<<": "<<result<<"\n";
            }
            else if(q>=1&&result!=0){
                g<<"Case #"<<t<<": Bad magician!"<<"\n";
            }
            if(result==0)
                g<<"Case #"<<t<<": Volunteer cheated!"<<"\n";
            result=0;
        }

    }
}
