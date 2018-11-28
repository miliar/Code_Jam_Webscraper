#include <iostream>
#include <fstream>
#include <string>
using namespace std;

bool mask_bit(char*,int);

int main(int argc,char *argv[]){

    fstream fs(argv[1],fstream::in);

    int N;
    fs >> N;

    for(int in_index=0; in_index<N; in_index++){
        long multiplier = 1;
        char mask[10]={0};
        long next_value = 0;
        long cur_value;
        fs >> cur_value;
        //cout <<"case input: "<< cur_value<<endl;
        // mask bit of 
        mask_bit(mask,cur_value);
        multiplier = 2;
        while(1){

            next_value = cur_value * multiplier;
            if(cur_value == next_value){
                cout<<"Case #"<<in_index+1<<": INSOMNIA\n";
                break;
            }
            // mask bit
            // check mask
            bool pass;
            pass = mask_bit(mask,next_value);

            if( pass ){
                cout<<"Case #"<<in_index+1<<": "<<next_value<<"\n";
                break;
            }
            multiplier += 1;
            //cout <<"case input: "<<in_index<<"  "<< next_value<<endl;
        }



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
