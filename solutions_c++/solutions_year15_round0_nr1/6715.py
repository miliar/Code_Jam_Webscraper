#include <iostream>

#include <fstream>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <string>


using namespace std;


void solve_problem_A(){

    std::ifstream in_file("A.in",std::ifstream::in);
    std::ofstream out_file("A.out",std::ofstream::out);


    if(in_file.is_open() && out_file.is_open()){

        int cases,current_case=1;

        in_file>>cases;

        while(cases--){

            int shyness;
            in_file>>shyness;
            std::string audience;

            in_file>>audience;


            long int queue=0;

            long int invites=0;


            int len=audience.length();



            for(int i=0;i<len && shyness;i++){

                if(audience[i]=='0'){

                    if(queue==0){
                        invites++;
                    }else{
                        queue--;
                    }

                }else{
                    queue+=((int)audience[i]-'0')-1;

                }


                shyness--;
            }

            out_file<<"Case #"<<current_case<<": "<<invites<<std::endl;
            current_case++;
        }


        in_file.close();
        out_file.close();

    }else{
        std::cout<<"Files are not open"<<std::endl;
    }

}

int main() {

    solve_problem_A();

    return 0;
}


