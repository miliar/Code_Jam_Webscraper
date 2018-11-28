#include <stdio.h>
#include <iostream>
#include <queue>

#define LOWEST 1
#define HIGHEST 2

using namespace std;

typedef struct{
int row,col;
} pixel;

queue<pixel> Elements;

int N,M;
int input[101][101];
int check_input[101][101];

bool check_validity(){

    for(int i = 0 ; i < N ; i++){
        for(int j = 0 ; j < M ; j++){
            check_input[i][j] = 0;
        }
    }

    if(N == 1 || M == 1) return true;

    bool valid = true;
    bool own_validity = true;

    while(!Elements.empty()){
        pixel tmp = Elements.front();
        Elements.pop();

        //cout << "(i,j) : " << tmp.row << "," << tmp.col << endl;
        int r = tmp.row, c = tmp.col;

        if(check_input[r][c])
            continue;

        bool rowValid = true, colValid = true;
        // Check Row Elements
        for(int j = 0 ; j < M ; j++){
            if(input[r][c] != input[r][j]){
                rowValid = false;
                break;
            }
        }
        if(rowValid){
            for(int j = 0 ; j < M ; j++)
                check_input[r][j] = 1;
            continue;
        }

        // Check Column Elements
        for(int i = 0 ; i < N ; i++){
            if(input[r][c] != input[i][c]){
                colValid = false;
                break;
            }
        }
        if(colValid){
            for(int i = 0 ; i < N ; i++)
                check_input[i][c] = 1;
        }

        if(! (rowValid || colValid) )
            return false;
    }

    return true;

//    // For two parameters 1 and 2
//    for(int i = 0 ; i < N ; i++){
//        // rowwise
//        int first_element = input[i][0];
//        //cout << "First Element: " << first_element << endl;

//        for(int j = 1 ; j < M; j++){

//            if(check_input[i][j])
//                continue;

//            // If there is rowwise mismatch, the column should be matched
//            if( input[i][j] != first_element ){

//                // If all of the elements in the row does not match, first_element can itself be invalid
//                if(first_element == 1)
//                own_validity = false;

//                int int_element = input[i][j];
//                //printf("Valid check: (%d,%d):%d\n",i,j,int_element);
//                // Search the full column
//                for(int k = 0; k < N ; k++){
//                    if(input[k][j] != int_element){
//                        valid = false;
//                        //cout << "Found invalid" << endl;
//                        break;
//                    }
//                }
//                if(!valid) break;
//                else {
//                    for(int k = 0; k < N ; k++){
//                        check_input[k][j] = 1;
//                    }
//                }
//            }
//            if(!valid) break;
//        }
//        if(!valid) break;

//        if(!own_validity){

//            for(int k = 0; k < N ; k++){
//                if(input[k][0] != first_element){
//                    valid = false;
//                    break;
//                }
//            }
//            if(!valid) break;

//            for(int k = 0 ; k < N; k++){
//                check_input[k][0] = 1;
//            }
//        }

//        for(int j = 0 ; j < M; j++){
//            check_input[i][j] = 1;
//        }
//    }

//    return valid;

}

int main(){

    int cases, index;
    bool result;

    scanf("%d",&cases);

    for(index = 1 ; index <= cases; index++){

        result = false;
        scanf("%d %d",&N,&M);

        while(!Elements.empty())
            Elements.pop();

        for(int i = 0 ; i < N ; i++){
            for(int j = 0 ; j < M; j++){
                scanf("%d",&input[i][j]);
                if(input[i][j] == 1){
                    pixel tmp;
                    tmp.row = i, tmp.col = j;
                    Elements.push(tmp);
                }
            }
        }

        result = check_validity();

        if(result)
            printf("Case #%d: YES\n",index);
        else printf("Case #%d: NO\n",index);
    }


    return 0;
}
