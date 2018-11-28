#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

string input_file = "A-large.in";
string output_file = "output.txt";

// For directing files to standard input-output
void file_io_init(){
    freopen(input_file.c_str(), "r", stdin);
    freopen(output_file.c_str(), "w", stdout);
}

char arr[100][100];

int row[100], col[100];

int R, C;

bool inline possible(){
    bool value = true;
    for(int r = 0; r < R; r++){
        for(int c = 0; c < C; c++){
            if(r == 2 && c == 2){
            }
            if((row[r] <= 1) && (col[c] <= 1)){
                if(arr[r][c] == '.'){

                }else{
                    value = false;
                }
            }
        }
    }
    return value;
}

int change(){
    int count = 0;
    bool present;
    for(int r = 0; r < R; r++){
        for(int c = 0; c < C; c++){
                present = false;
                switch(arr[r][c]){
                    case '^' :
                        for(int a = (r-1); a >= 0; a--){
                            if(arr[a][c] != '.'){
                                present = true;
                                break;
                            }
                        }
                        break;
                    case 'v' :
                        for(int a = (r+1); a < R; a++){
                            if(arr[a][c] != '.'){
                                present = true;
                                break;
                            }
                        }
                        break;
                    case '>' :
                        for(int a = (c+1); a < C; a++){
                            if(arr[r][a] != '.'){
                                present = true;
                                break;
                            }
                        }
                        break;
                    case '<' :
                        for(int a = (c-1); a >= 0; a--){
                            if(arr[r][a] != '.'){
                                present = true;
                                break;
                            }
                        }
                        break;
                    default: present = true;
                    break;
                    }
               if(present == false){
                    count++;
               }
        }
    }
    return count;
}

int main()
{
    file_io_init();
    int Test;
    cin >> Test;
    for(int t = 1; t <= Test; t++){
        cin >> R >> C;
        for(int r = 0; r < R; r++){
            row[r] = 0;
            for(int c = 0; c < C; c++){
                cin >> arr[r][c];
                if(arr[r][c] != '.'){
                    row[r]++;
                }
            }
        }
        for(int c = 0; c < C; c++){
            col[c] = 0;
            for(int r = 0; r < R; r++){
                if(arr[r][c] != '.'){
                    col[c]++;
                }
            }
        }
        bool value = possible();
        if(value == false){
            cout << "Case #" << t << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << t << ": " << change() << endl;

    }
    return 0;
}
