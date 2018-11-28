#include <iostream>
#include <vector>
#include <fstream>


using namespace std;

int solute(vector<int> &vec1,vector<int> &vec2);

int main()
{
    int num1[4][4],num2[4][4];
    int ans1,ans2;
    int T;
    int times = 1;
    ifstream myin("A-small-attempt2.in");
    ofstream myout("result.txt");

    myin >> T;
    while(times++ <= T){
        myin >> ans1;
        vector <int> line1;
        vector <int> line2;
        for(int i=0 ;i<4 ; i++){
            for(int j=0 ; j<4 ; j++){
                myin >> num1[i][j];
            }
        }
        for(int i=0 ; i<4 ; i++){
            line1.push_back(num1[ans1-1][i]);
        }
        myin >> ans2;
        for(int i=0 ;i<4 ; i++){
            for(int j=0 ; j<4 ; j++){
                myin >> num2[i][j];
            }
        }
        for(int i=0 ; i<4 ; i++){
            line2.push_back(num2[ans2-1][i]);
        }
        int ret = solute(line1,line2);
        // -1 bad
        // 0 cheated
        myout << "Case #"<<times-1<<": ";
        if(ret == -1){
            myout << "Bad magician!" << endl;
        }
        else if(ret == 0){
            myout << "Volunteer cheated!" << endl;
        }
        else {
            myout << ret << endl;
        }

    }

    return 0;
}

int solute(vector<int> &vec1,vector<int> &vec2)
{
    int num,sum=0;

    for(int i=0 ; i<4 ; i++){
        for(int j=0 ; j<4 ; j++){
            if(vec1[i] == vec2[j]){
                num = vec1[i];
                sum ++;
            }
        }
    }
    if(sum == 0){
        return 0;
    }
    else if(sum > 1){
        return -1;
    }
    else return num;
}
