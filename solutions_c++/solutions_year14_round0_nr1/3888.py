#include<iostream>

#include<fstream>
#include<sstream>

using namespace std;

int main(int argc, char* argv[]){
    char* filename = argv[1];
    //cout << filename << endl;
    fstream fp;
    int T;

    fp.open(filename, ios::in);
    if(!fp){
        cout <<"fail to open" << filename <<endl;
    }
    fp >> T ;
    int guess =0;
    int row1=0;
    int row2=0;
    int arr1[4][4];
    int arr2[4][4];
    for(int t=0; t<T; t++){
        fp >> row1;
        for(int i=0;i<4;i++)
            for(int j=0; j<4;j++)
                fp >> arr1[i][j];
        fp >> row2;
        for(int i=0;i<4;i++)
            for(int j=0; j<4;j++)
                fp >> arr2[i][j];
        row1 --;
        row2 --;
        int cnt =0;
        int idx;
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++){
            if(arr1[row1][i] == arr2[row2][j]){
                cnt++;
                idx = arr1[row1][i];
            }
        }
        //cout << "test" << endl;
        if(cnt ==0){
            cout << "Case #" << (t+1) << ": Volunteer cheated!" << endl;
        }else if(cnt ==1){
            cout << "Case #" << (t+1) << ": " << idx << endl;
        }else{
            cout << "Case #" << (t+1) << ": Bad magician!" << endl;
        }


    }


    return 0;
}
