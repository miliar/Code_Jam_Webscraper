#include <cstdio>
#include <cstdlib>>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char ** argv){

    int T;
    cin>>T;
    string name[2];
    name[0] = "GABRIEL";
    name[1] = "RICHARD";

    for(int i = 0 ; i < T; ++i){

        int ans = 0;
        int X, R, C;
        cin>>X>>R>>C;

        do{
            if(R*C % X != 0){
                ans = 1;
                break;
            }
            if(X == 3){
                if(R == 1 || C == 1){
                    ans = 1;
                    break;
                }
            }
            if(X == 4){
                if(R < 3 || C < 3){
                    ans = 1;
                    break;
                }
            }
        }while(false);
        cout<<"Case #"<<i + 1<<": "<<name[ans]<<endl;
    }

    return 0;
}
