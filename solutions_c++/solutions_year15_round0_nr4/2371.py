#include <iostream>
#include <vector>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main(){
    string line;
    ifstream myin ("in");
    ofstream myout ("out");
    getline(myin,line);
    int test=stoi(line);
    int D;
    for(int i = 1;i<=test;i++){
        getline(myin,line);
        D=stoi(line);
        getline(myin,line);
        cout<<line<<endl;
        stringstream stream(line);
        vector<int> plates;
        int n;
        while(1){
            stream>>n;
            if(!stream)
                break;
            plates.push_back(n);
        }
        int biggest=0;
        int sec=-1;
        int round=0;
        while(plates[biggest]!=0){
            biggest=0;
            sec=-1;
            cout<<"cur round "<<round<<endl;
            for(int j=0;j<D;j++)
                cout<<plates[j]<<" ";
            for(int j=1;j<D;j++){
                if(plates[j]>plates[biggest]){
                    sec=biggest;
                    biggest=j;
                }
                else if (sec==-1||plates[j]>=plates[sec]){
                    sec=j;
                }
            }
            cout<<endl;
            cout<<"the biggest "<<plates[biggest]<<" and the sec "<<plates[sec]<<endl;
            if(plates[biggest]<=3){
                for(int j=0;j<D;j++){
                    if(plates[j]>0)
                        plates[j]--;
                }
            }
            else{
                int least=plates[biggest];
                int cut=1;
                for(int j=1;j<=plates[biggest];j++){
                    int cur=(plates[biggest]-1)/j+j-1;
                    if(cur<least){
                        least=cur;
                        cut=j;
                    }

                }
                //cut is the smallest;
                cout<<"the cut is"<<cut<<endl;
                plates[biggest]=plates[biggest]-plates[biggest]/cut;

            }
            round++;
        }
        myout<<"Case #"<<i<<": "<<round<<endl;
        cout<<"case # "<<i<<": "<<round<<endl;
       
    }
    return 0;
}
