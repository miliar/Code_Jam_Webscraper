#include <iostream>
#include <fstream>
#include <algorithm>

using namespace std;

int main(){
    ifstream inputFile("A-large.in");
    ofstream outputFile("A-large.out");

    int cases;
    long long y, a;
    int mote_count;
    inputFile >> cases;
    for(int testcase = 1; testcase<=cases;testcase++){
        y=0;
        inputFile >> a >> mote_count;
        long long motes[mote_count];
        int operations[mote_count];
        for(int i=0;i<mote_count;i++){
            inputFile>>motes[i];
        }
        if(a==1){
            y = mote_count;
        }
        else{
            long total_adds=0;
            sort(motes,motes+mote_count);
            long long temp_a = a;
            for(int i=0;i<mote_count;i++){
                operations[i]=0;
                while(temp_a<=motes[i]){
                    temp_a = temp_a*2 - 1;
                    operations[i]++;
                    total_adds++;
                };
                temp_a = temp_a+motes[i];
            }

            // analyse operations array
            int op = 0;
            for(int i=0;i<mote_count;i++){
                if(operations[i]!=0){
                    if(operations[i]==1){
                        op++;
                    }else{
                        if(total_adds-op<=(mote_count-i)){
                            op = op +operations[i];
                        }
                        else{
                            op = op +mote_count-i;
                            break;
                        }
                    }
                }

            }
            y =op;

        }
        outputFile<<"Case #"<<testcase<<": "<<y<<endl;
    }
    inputFile.close();
    outputFile.close();

    return 0;
}
