#include <iostream>
#include <fstream>
using namespace std;
int main(){
    ifstream in;
    ofstream out;
    in.open("A-large.in");
    out.open("output-large.out");
    string invited;
    int maxShy, newInvited, stood, j, cases, newStood; 
    in>>cases;
    
    int i=0;
    while(i<cases){
        newInvited = 0;
        in>>maxShy;
        in>>invited;
        j=0;
        stood=0;
        while(j<=maxShy){
            if(j>stood){
                newInvited+=1;;
                stood +=1;
            }
            newStood = invited[j] - '0';
            stood += newStood;
            j++;
        }
        out<<"Case #"<<i+1<<": "<<newInvited<<endl;
        i++;   
    }
 //   system("pause");
    in.close();
    out.close();
    return 0;  
}
