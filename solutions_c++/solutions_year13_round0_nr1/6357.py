#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <string.h>
#include <cmath>
#include <limits.h>
#include <set>
#include <stdlib.h>
int board[4][4]= {0};
int cases=0;
using namespace std;
ofstream fp1("p.txt");
int processboard(int a,int count){
//check for row;

 int product=1;

for (int i=0;i<4;i++){
    product=1;
    //check for that row
    for (int j=0;j<4;j++){
     //  cout<<board[i][j]<<"compare "<<a;
    if ((a!=board[i][j] && board[i][j]!=3)||(board[i][j]==0)){
    product=0;
    break;
    }
}
if (product==1){
if (a==1)
fp1<<"Case #"<<count+1<<": X won"<<endl;
else
fp1<<"Case #"<<count+1<<": O won"<<endl;

//cout<<"Case #"<<count<<": "<<a <<" Won 2"<<endl;
return a;
}
}

//check for row;


for (int i=0;i<4;i++){
    product=1;
    //check for that column
    for (int j=0;j<4;j++){
    if ((a!=board[j][i] && board[j][i]!=3)||(board[j][i]==0)){
    product=0;
    break;
    }
}
if (product==1){
  if (a==1)
fp1<<"Case #"<<count+1<<": X won"<<endl;
else
fp1<<"Case #"<<count+1<<": O won"<<endl;//cout<<"Case #"<<count<<": "<<a <<" Won 3"<<endl;
return a;

}
}

//check for diagonal left to right
product=1;
for (int i=0;i<4;i++)
{
if ((a!=board[i][i] && board[i][i]!=3) ||( board[i][i]==0)){

product=0;
break;
}
}
if (product==1){
  if (a==1)
fp1<<"Case #"<<count+1<<": X won"<<endl;
else
fp1<<"Case #"<<count+1<<": O won"<<endl;
//cout<<"Case #"<<count<<": "<<a <<" Won 4"<<endl;
return a;

}
//check for diagonal  right to left
product=1;
//cout<<"val a "<<a;
//cout<<board[3][3]<<"val check";
for (int i=3;i>=0;i--)
{
  //  cout<<board[i][i]<<"at "<<i<<i<<endl;
if ((a!=board[i][3-i] && board[i][3-i]!=3)||(board[i][3-i]==0)){
product=0;
break;
}
}
if (product==1){
  if (a==1)
fp1<<"Case #"<<count+1<<": X won"<<endl;
else
fp1<<"Case #"<<count+1<<": O won"<<endl;
//cout<<"Case #"<<count<<": "<<a <<" Won 5"<<endl;
return a;

}

if (product==0)
return 0;
}

void ReadFromFile(char * path)
{
    ifstream fp (path);
    if (!fp.is_open()) //
        cout<< "Error in the file path";
    else
    {

        fp>>cases;


      //  cout<<"No of test cases"<<cases<<endl;
        int count=0;
        while (cases>0)
        {
            for (int i=0; i<4; i++)
            {
                for (int j=0; j<4; j++)
                {
                    char c;
                    fp>>c;
                    switch (c)
                    {
                    case 'X':
                        board[i][j]=1;
                       // cout<<c;
                        break;
                    case 'O':
                        board[i][j]=2;
                       // cout<<c;
                        break;
                    case 'T':
                        board[i][j]=3;
                       // cout<<c;
                        break;

                    case '.':
                        board[i][j]=0;
                    }

                }
             //   cout<<endl;
            }
//            for(int i=0;i<4;i++){
//            for(int j=0;j<4;j++)
//            cout<<board[i][j];
//            cout<<endl;
//            }
            int result=0;
            for (int i=1;i<3;i++){

                result=processboard(i,count);
                if (result!=0)
                break;
            }
            bool is_zero=0,is_draw=1;
            if (result==0){
            for (int i =0;i<4;i++){
                if (!is_zero)
            for(int j=0;j<4;j++){
                if (!is_zero)
            if (board[i][j]==0)
            {
             is_zero=1;
            }
            }
            if (is_zero){
            fp1<<"Case #"<<count+1<<": "<<"Game has not completed"<<endl;
            is_draw=0;
            break;
            }
            }

            if (is_draw)
            fp1<<"Case #"<<count+1<<": "<<"Draw"<<endl;

            }


            cases--;
            count++;

        }


    }

};



int main(int argc, char* argv[])
{
    ReadFromFile(argv[1]);

    return 0;
}
