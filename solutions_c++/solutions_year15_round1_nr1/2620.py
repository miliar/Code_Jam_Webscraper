#include <fstream>
#include <iostream>
#include <algorithm>
using namespace std;

int main(){
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    int mushroom[2001];
    int t;
    int tt=1;
    fin>>t;
        while(t--){
            int N;
            int i=1;
            int temp;
            int rate2=0;

            fin>>N;
            temp=N;
            mushroom[0]=-9999999;
            while(temp--){
                fin>>mushroom[i];
                if((mushroom[i-1]-mushroom[i])>rate2){
                    rate2=mushroom[i-1]-mushroom[i];
                }
                i++;
            }
            long long int firstmethod=0;
            i=1;
            while(i<N){
                if(mushroom[i]>mushroom[i+1]){
                    firstmethod+=(mushroom[i]-mushroom[i+1]);

                }
                i++;
            }
            long long int secondmethod=0;
            int total=0;
            int eaten;
            int remain;
            i=1;
            while(i<N){
                total=mushroom[i];
                if(total<rate2){
                    eaten=total;
                }
                else{
                    eaten=rate2;
                }
                secondmethod+=eaten;
                i++;
            }
            fout<<"Case #"<<tt<<": "<<firstmethod<<" "<<secondmethod<<"\n";
            tt++;
    }
    fin.close();
    fout.close();
    return 0;
}
