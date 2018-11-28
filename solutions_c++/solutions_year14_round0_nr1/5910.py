#include <iostream>
#include <fstream>
#include <map>
using namespace std;

ifstream fin("C:\\Users\\yanta_000\\Downloads\\A-small-attempt1.in");
ofstream fout("A-small-attempt1.out");

int main()
{
    int num_case,row_1,row_2,first[5],second[5],tmp[5],match=0,find_num;
   // map<int,int> map_num;
    map<int,int>::iterator it;
    fin>>num_case;
    for(int i=1;i<=num_case;i++){
        map<int,int> map_num;
        match=0;
        fin>>row_1;
        for(int j=1;j<=4;j++){
            if(j==row_1){
                for(int k=1;k<=4;k++){
                    fin>>first[k];
                    map_num[first[k]]=1;
                }
            }
            else{
                for(int k=1;k<=4;k++){
                    fin>>tmp[k];
                }
            }
        }
        fin>>row_2;
        for(int j=1;j<=4;j++){
            if(j==row_2){
                for(int k=1;k<=4;k++){
                    fin>>second[k];
                    if(map_num.find(second[k])!=map_num.end()){
                        map_num[second[k]]=0;
                    }
                }
            }
            else{
                for(int k=1;k<=4;k++){
                    fin>>tmp[k];
                }
            }
        }
        for(it=map_num.begin();it!=map_num.end();it++){
            if(it->second==0){
                match++;
                find_num=it->first;
            }
        }
        if(match==1){
            fout<<"Case #"<<i<<": "<<find_num<<endl;
        }
        else if(match==0){
            fout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
        }
        else{
            fout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
        }

    }
    return 0;
}
