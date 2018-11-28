#include<iostream>
#include<fstream>
using namespace std;

int main(){

ofstream output;
output.open("outS.txt");
ifstream input;
input.open("D-small-attempt0.in");
 int x;
	input>>x;
	for(int t=0;t<x;t++){
int g=0;
int ri=0;
int X,R,C;
input>>X>>R>>C;
    if(X==1){
                    g=1;
    }else if(X==2){
                    if( (R==1 && C==1) || (R==1 && C==3) || (R==3 && C==1) ||( R==3 && C==3)){
                        ri=1;
                    }else{
                        g=1;}}
     else if (X==3){
                    if( (R==2 && C==3) || (R==3 && C==2) || (R==3 && C==4) ||( R==4 && C==3)||(R==3&&C==3)){
                        g=1;
                    }else{
                        ri=1;}}
     else{
        if((R==4 && C==4 )||( R==4 && C==3)||( R==3&&C==4)){g=1;
                    }else{
                        ri=1;}}


        if(ri){
            output<<"Case #"<<t+1<<": RICHARD"<<"\n";
        }
        else{
            output<<"Case #"<<t+1<<": GABRIEL"<<"\n";
        }


}
}
