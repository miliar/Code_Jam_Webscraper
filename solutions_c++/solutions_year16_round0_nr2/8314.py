#include <iostream>
#include <fstream>
#include <string>
#include <map>
using namespace std;

bool mask_bit(char*,int);

int main(int argc,char *argv[]){

    fstream fs(argv[1],fstream::in);

    int N;
    fs >> N;


    map<string,int> shortest_map[101];
    for(int in_index=0; in_index<N; in_index++){
        string ref_str;
        fs >> ref_str;


        cout<<"Case #"<<in_index+1<<": ";

        int str_length = ref_str.length();
        if( shortest_map[str_length].size() == 0){
            string orig = "+";
            for(int len=1;len<str_length; len++){
                orig += "+";
            }
            shortest_map[str_length][orig] = 0;

            for(int loop=0; loop<2*str_length; loop++){
                map<string,int>::iterator it=shortest_map[str_length].begin();
                for(; it != shortest_map[str_length].end(); ++it){
                    string fliping_str_i = it->first;
                    for(int idxPos=0; idxPos < fliping_str_i.length(); idxPos++){
                        string flopped_str_o = fliping_str_i;
                        for(int idxSwap=0; idxSwap<=idxPos; idxSwap++){
                            char c = fliping_str_i[idxPos-idxSwap];
                            if(c == '+'){
                                c = '-';
                            }
                            else{
                                c = '+';
                            }
                            flopped_str_o[idxSwap] = c;
                        }


                        int cost_gen = 1 + it->second;

                        if( shortest_map[str_length].find( flopped_str_o ) == shortest_map[str_length].end()){
                            shortest_map[str_length][flopped_str_o] = cost_gen;
                        }
                        else{
                            int previous_cost = shortest_map[str_length].find( flopped_str_o ) -> second;
                            if( cost_gen < previous_cost){
                                shortest_map[str_length].find( flopped_str_o )->second = cost_gen;
                            }   
                        }
                    }
                }

            }
        }
        cout<<shortest_map[str_length][ref_str]<<endl;

    }


    fs.close();
    return 0;
}

bool mask_bit(char* array,int N){
   bool pass = false; 

   while(N != 0){
      int mod_num = N%10;
      array[mod_num] = 1;
      N /= 10;
   }
    int cnt=0;
    for(cnt=0;cnt<10;cnt++){
        if(array[cnt] == 0){
            break;
        }
    }
    if(cnt == 10){
        pass = true;
    }
    return pass;
}
