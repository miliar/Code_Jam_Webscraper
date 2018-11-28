#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <fstream>
#include <cmath>  

using namespace std;
string process_ln(string line);

int main(){
    ifstream infile("A-large.in");
    ofstream outfile("A-large-practice-result.in");

    int i=0,n=1;
    int N;
    string line;

	int num_people_level_ant=0 ;  
	int num_people_level_actual ; 
	int position=0;
    int friends_need=0;
    int friends_already_have=0;
	int lvl_shiness=0;


    infile>>N;  //number of test cases
    getline(infile,line); // Discard the rest of the line.
    int stop=0;
    stringstream ss;
    string result_position;

    while(i < N) {
        getline(infile,line);
        int stop=line.find(" ");
        string first_number = line.substr(0,stop+1);
        int num_first_number=0;
        stringstream(first_number) >> num_first_number;
        string new_string = line.substr(stop+1, line.length());
        string result=new_string;

        int j=0;
        //bool flag=true;
        //&& flag
		while (j<=num_first_number){	
				result_position+=result[position];
                stringstream(result_position) >> num_people_level_actual;
				lvl_shiness= position;
                if (num_people_level_actual!=0) {

                            if (j==0 && num_first_number==0){
                                //friends_needed=0;
                                friends_already_have=0;
                                }
                                
                            if (num_people_level_ant < lvl_shiness){
                                    friends_need=  lvl_shiness-num_people_level_ant -friends_already_have;
                                    if (friends_need>0) {
                                        friends_already_have= friends_already_have + friends_need;
                                        result_position=""; 
                                    }
                                    result_position="";   
                                }                          
                }                
                num_people_level_ant = num_people_level_ant + num_people_level_actual;
                position ++;
                result_position=""; 
                j++;
            }   
        outfile << "Case #" << n << ": " <<  friends_already_have << endl;
        n++,i++;
        //flag=true;

        num_people_level_ant =0;  
		num_people_level_actual =0;  
		position=0;
		//friends_needed=0;
        friends_need=0;
        friends_already_have=0;
		lvl_shiness=0;
}
return 0;
}





