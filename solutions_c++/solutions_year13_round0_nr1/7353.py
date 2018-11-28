#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int sumAnswer(int sum){
    if(sum==4||sum==103) return 0;
    else if(sum==40||sum==130) return 1;
    else if(sum<1000) return 2;
    return 3;
}


int calculateTable(int table[4][4]){
    bool incomplete=false;
    // calculate rows
    for(int row = 0 ;row<4;row++){
        int sum = 0;
        for(int col = 0;col<4;col++){
            sum+=table[row][col];
        }
        int answer=sumAnswer(sum);
        if(answer<2) return answer;
        if(answer==3) incomplete=true;
    }
    // calculate cols
    for(int col = 0 ;col<4;col++){
        int sum = 0;
        for(int row = 0;row<4;row++){
            sum+=table[row][col];
        }
        int answer=sumAnswer(sum);
        if(answer<2) return answer;
        if(answer==3) incomplete=true;
    }
    // calculate diagonal
    int sum=0;
    for( int i = 0;i<4;i++){
        sum+=table[i][i];
    }
    int answer=sumAnswer(sum);
    if(answer<2) return answer;
    sum=0;
    for(int i = 0;i<4;i++){
        sum+=table[i][3-i];
    }
    answer = sumAnswer(sum);
    if(answer<2) return answer;
    if(incomplete) return 3;
    return 2;
}

string answerToString(int case_number){
    switch(case_number){
    case 0: return "O won";break;
    case 1: return "X won";break;
    case 2: return "Draw";break;
    case 3: return "Game has not completed";break;
    }
    return "Error";
}

//#define TEST

int main()
{
    streambuf * buf;
#ifdef TEST
    buf = cout.rdbuf();
#else
    ofstream of;
    //of.open("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/ans1-1.txt");
    of.open("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/A-large.out");
    buf = of.rdbuf();
#endif
    ostream out(buf);


    string line;
    //ifstream infile("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/A-small-attempt0.in");
    ifstream infile("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/A-large.in");
    if(!infile.is_open()){
        cout << "file error" <<endl;
    }
    // read to stringstream
    stringstream ss;
    ss << infile.rdbuf();
    infile.close();

    int num_case=0;
    ss>>num_case;
    cout << num_case <<endl;

    for(int i=1;i<=num_case;i++){
        int table[4][4];
        // change to number
        for(int col = 0;col<4;col++){
            for(int row = 0 ;row<4;row++){
                char c;
                ss>>c;
                if(c=='.') table[row][col]=1000;
                else if(c=='T') table[row][col]=100;
                else if(c=='X') table[row][col]=10;
                else table[row][col]=1;
            }
        }
        int answer = calculateTable(table);
        stringstream ss_answer;
        ss_answer<<"Case #"<<i<<": "<<answerToString(answer)<<endl;
        out<<ss_answer.str();
    }

    cout << "THE END!" << endl;
#ifndef TEST
    of.close();
#endif
    return 0;
}

