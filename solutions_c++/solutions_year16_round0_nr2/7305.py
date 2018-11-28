#include<iostream>
#include<fstream>
#include<string>
#include<deque>
#include<stack>
#include<map>
#include<set>

using namespace std;

class Pancakes_Data{
    public:
        string pancakes;
        int level;

        Pancakes_Data(string pancakes, int level){
            this->pancakes = pancakes;
            this->level = level;
        }
};

int main(){

    ofstream myfile;
    myfile.open ("output.in");

    int T;
    cin>>T;

    for(int case_i = 1 ; case_i<=T ; case_i++){

        string input;
        cin>>input;

        int flips = 0;
        int last = input[0];
        for(int i=0;i<input.length();i++){
            if( input[i] != last ){
                last = input[i];
                flips++;
            }
        }

        if(input[0] == '+'){
            if(flips %2 != 0){
                flips++;
            }
        }
        else{
            if(flips %2 == 0){
                flips++;
            }
        }

        cout<<"Case #"<<case_i<<": "<<flips<<endl;
        myfile<<"Case #"<<case_i<<": "<<flips<<endl;
    }

    return 0;
}
