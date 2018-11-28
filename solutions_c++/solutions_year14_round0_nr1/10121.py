#include<iostream>
#include<fstream>
using namespace std;
int main(){

    ifstream fin("magic.in");
    ofstream fout("magic.out");

    int n;
    fin>>n;

    int row;
    int row2;
    for(int i=0;i<n;i++){
        fin>>row;
        int set1[4][4];
        for(int a=0;a<4;a++){
            for(int b=0;b<4;b++){
                fin>>set1[a][b];
            }
        }

        fin>>row2;
        int set2[4][4];
        for(int a=0;a<4;a++){
            for(int b=0;b<4;b++){
                fin>>set2[a][b];
            }
        }

        int count = 0;
        int val = 0;
        for(int a=0;a<4;a++){
            int temp = set1[row-1][a];
            for(int b=0;b<4;b++){
                int temp2= set2[row2-1][b];
                if(temp == temp2){
                    count++;
                    val = temp;
                }
            }
        }

        if(count==1){
            fout<<"Case #"<<i+1<<": "<<val<<endl;
        }else if(count==0){
            fout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }else if(count>1){
            fout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }
    }

    return 0;
}
