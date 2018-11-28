#include <iostream>;
#include <fstream>;
#include <set>;
#include <vector>;
using namespace std;
    ifstream in("B-Small.in");
    ofstream out("B-Large.out");

class Fraction{
      public: double up,down;
      public: Fraction::Fraction(){

      }
      public: void setFraction(double _up, double _down){
             up= _up;
             down= _down;              
      }
      
      public: pair<bool,double> isLower(Fraction next, Fraction remaining){
          pair<bool , double> p;
          p.second=(next.up/next.down)+(remaining.up/remaining.down);
          p.first=(up/down) <= (p.second);
          //out<<p.first<<p.second<<" ";
          return p;       
      }
      
} frac;

double solve(double cost, double farm, double goal){

       double cookies=2.0;
       double best=(goal)/cookies;
       double current=0.0;
       bool ended=false;
       while(ended!=true){
           double next=cost/cookies;
           
           cookies+=farm;
           
           double remaining= (goal)/cookies;
       
           if(remaining+next+current >= best ){
               ended=true;
           }else{
               best=remaining+next+current;
               
               current+=next;
           }
           
       
       }
     
       return best;       
}



int main(){
    

    int tests;
    in>>tests;
    for(int i=0;i<tests;i++){
            double cost, farm, goal;
            in>>cost>>farm>>goal;        
            char salida[100]; 
            double answer=solve(cost,farm,goal);
            sprintf(salida, "Case #%d: %.7f\n", (i+1), answer);
            out<<salida;
    }
    
    
    
}


