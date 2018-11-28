#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream cin("A-small-attempt2.in");
    //ifstream cin("entrada.txt");
    ofstream cout("A-small-attempt2.txt");

    long long int case_=0,row1=0,row2=0,num,tam,sw,resp;
    cin>>case_;
    for(int k=1;k<=case_;k++){
            cin>>row1;
            set<long long int>  mySet;
            for (int j=0;j<4;j++){
                for (int i=0;i<4;i++){
                    cin>>num;
                    if ((j+1)==row1){
                        mySet.insert(num);
                    }
                }
            }
            cin>>row2;
            tam=mySet.size();
            sw=0;
           for (int j=0;j<4;j++){
               for (int i=0;i<4;i++){
                    cin>>num;
                    if ((j+1)==row2){
                        mySet.insert(num);
                        if(tam==mySet.size()){
                           if (sw==0){
                                sw=1;
                                resp=num;
                           }else{
                                sw=-1;
                           }
                        }
                        tam=mySet.size();
                    }
                }
           }
           cout<<"Case #"<<k<<": ";
           if(sw==1){
            cout<<resp;

           }else if(sw==0){
            cout<<"Volunteer cheated!";
           }else if(sw==-1){
            cout<<"Bad magician!";
            }
            cout<<endl;
    }


    return 0;
}
