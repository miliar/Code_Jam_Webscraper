

#include <iostream>
#include <fstream>
#include <string.h>
#include <string>
using namespace std;

char tic[4][5];
bool dot=false;
string check(){
    int count=0;
    for (count=0; count<4; count++) {
        int count1=0;
        bool x=false;
        bool y=false;
        for (count1=0; count1<4; count1++) {
            if (tic[count][count1]=='.'){
                dot=true;
                break;
            }else if(tic[count][count1]=='X'){
                x=true;
            }else if (tic[count][count1]=='O')
                y=true;
        }
        if (count1==4&&x && !y)
            return "X won";
        if (count1==4&&!x && y)
            return "O won";
    }
    for (count=0; count<4; count++) {
        int count1=0;
        bool x=false;
        bool y=false;
        for (count1=0; count1<4; count1++) {
            if (tic[count1][count]=='.'){
                dot=true;
                break;
            }else if(tic[count1][count]=='X'){
                x=true;
            }else if (tic[count1][count]=='O')
                y=true;
        }
        if (count1==4&&x && !y)
            return "X won";
        if (count1==4&&!x && y)
            return "O won";
    }
    bool x=false;
    bool y=false;
    for (count=0; count<4; count++) {
        if (tic[count][count]=='.'){
            dot=true;
            break;
        }else if(tic[count][count]=='X'){
            x=true;
        }else if (tic[count][count]=='O')
            y=true;
    }
    if (count==4&&x && !y)
        return "X won";
    if (count==4&&!x && y)
        return "O won";
    x=false;
    y=false;
    for (count=0; count<4; count++) {
        if (tic[count][3-count]=='.'){
            dot=true;
            break;
        }else if(tic[count][3-count]=='X'){
            x=true;
        }else if (tic[count][3-count]=='O')
            y=true;
    }
    if (count==4&&x && !y)
        return "X won";
    if (count==4&&!x && y)
        return "O won";
    if (dot)
        return "Game has not completed";
    return "Draw";
}
int main() {
    ifstream input("/Users/Sunku/A-large.in.txt");
    ofstream output("/Users/Sunku/output1.txt");
    int testcases;
    input>> testcases;
    int count=0;
    for (count=1;count<=testcases;count++){
        dot=false;
        input>>tic[0];
        input>>tic[1];
        input>>tic[2];
        input>>tic[3];
        output<<"Case #"<<count<<": "<<check()<<endl;
    }
    input.close();
    output.close();
    return 0;
}