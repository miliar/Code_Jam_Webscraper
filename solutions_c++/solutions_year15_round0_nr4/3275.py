//code compiled under g++ / c++11
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <string>

using namespace std;
bool solve_case(int X,int R,int C);

int main(void){
    int case_all;

    cin >> case_all;

    for(int i=1;i <= case_all;i++){
        int X,R,C;
        cin >> X;
        cin >> R;
        cin >> C;

        cout << "Case #" << i << ": ";
        if(solve_case(X,R,C)){//completeable
            cout << "GABRIEL";
        }else{//not
            cout << "RICHARD";
        }
        cout << endl;
    }
}

bool solve_case(int X,int R,int C){
    int s_side = (R<C)?R:C;
    int l_side = (R<C)?C:R;

    //when X>6 (>=7) it's possible to form 
    //a square with an empty hole inside
    //*** (something like this)
    //* *
    //**
    //thus makes completion impossible
    if(X > 6){
        return false;
    }

    //check size
    if( R*C < X ){
        return false;
    }

    //check grid is a multiple of x
    if( (R*C) % X != 0 ){
        return false;
    }

    //check shape, block off 2 area
    if((X+1)/2 >= s_side){
        if( X >3 || ((X+1)/2 >s_side) ){
            return false;
        }
    }

    //** this shape
    // *
    //**
    /*
    if(X >=5 && s_side <= X-5+2){
        return false;
    }
    */

    return true;
}

