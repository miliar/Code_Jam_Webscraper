#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;
int main(){
    freopen("D-small-attempt0.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputD.txt", "w", stdout);
    int T,X,R,C;
    string answer;
    cin>>T;
    for(int i=0;i<T;i++){
        cin>>X>>R>>C;
        if(R*C < X)
            answer = "RICHARD";
        else if(X==1)
            answer = "GABRIEL";
        else if(R*C == X){
            if(X==2)
                answer = "GABRIEL";
            else
                answer = "RICHARD";
        }
        else{
            if(X==2){
                if((R*C)%2==0)
                    answer = "GABRIEL";
                else
                    answer = "RICHARD";
            }
            else if((R<X && C<X) || (R==1 || C==1))
                answer = "RICHARD";
            else if(X==3){
                 if((R*C)%X != 0)
                    answer = "RICHARD";
                 else
                    answer = "GABRIEL";
            }
            else if(X==4){
                if(R==2 || C==2)
                   answer = "RICHARD";
                else
                  answer = "GABRIEL";
            }
        }

        cout<<"Case #"<<i+1<<": "<<answer<<endl;
    }


    return 0;
}
