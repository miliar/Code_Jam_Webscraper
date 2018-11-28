#include<iostream>

int main(){
    int tests;
    std::cin >> tests;
    for(int i = 0; i!=tests;++i){
        int R, X, C;
        std::cin >> X >> R >> C;
        bool fillable = false;
        if(X == 1){
            fillable = true;
        }
        else if(X== 2){
            if(R> 1 || C > 1){
                if((R*C)%2==0){fillable = true;}
            }
        }
        else if(X==3){
            if((R>2 || C > 2) && (R!= 1 && C != 1)){
                    if((R*C)%3==0){fillable=true;}
            }
        }
        else if(X==4){
            if((R>3 || C > 3) && (R>=3 && C>=3)){
                    if((R*C)%4==0){fillable=true;}
            }
        }

        if(fillable){
            std::cout << "Case #" << i+1 << ": GABRIEL" << std::endl;
        }
        else{
            std::cout << "Case #" << i+1 << ": RICHARD" << std::endl;
        }
/**
        std::cout << X << " " << R << " " << C << " " << std::endl;
        for(int i = 0; i!=R;++i){
            for(int j = 0; j!=C; ++j){
                std::cout << fillable;
                }
            std::cout << std::endl;
        }
**/
    }
}

