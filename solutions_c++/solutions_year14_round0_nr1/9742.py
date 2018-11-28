#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
using namespace std;

int main(){
    ifstream input("input.in");
    int TCases,ans1,ans2;
    if(input.is_open()){
        cout<<"Opened successfully"<<endl;
        int arr1[4][4]; int arr2[4][4]; input>>TCases; cout<<TCases<<endl;
        for(int i=0; i<TCases; i++){
            input>>ans1;//cout<<ans1<<endl;
            for(int a=0; a<4; a++){
                for(int b=0; b<4; b++){
                    input>>arr1[a][b];
                }
            }
            input>>ans2;//cout<<ans2<<endl;
            for(int a=0; a<4; a++){
                for(int b=0; b<4; b++){
                    input>>arr2[a][b];
                }
            }
            int counter=0; int datNum;
            for(int i=0; i<4; i++){
                    for(int j=0; j<4; j++){
                        cout<<arr1[ans1-1][i]<<" vs "<<arr2[ans2-1][j]<<endl;
                        if(arr1[ans1-1][i]==arr2[ans2-1][j]){
                            counter++;
                            datNum=arr1[ans1-1][i]; cout<<datNum<<endl;
                        }
                    }
            }
            ofstream output("output.in",ios::ate | ios::app);
            if(output.is_open()){
            if(counter==0){
                cout<<"Volunteer cheated"<<endl;
                output<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
            }else if(counter>1){
                cout<<"Bad magician"<<endl;
                output<<"Case #"<<i+1<<": Bad magician!"<<endl;
            }else{
                cout<<"The number is "<<datNum<<endl;
                output<<"Case #"<<i+1<<": "<<datNum<<endl;
            }}else{
                cerr<<"Could not create output file"<<endl;
            }

        }
    }else{
        cerr<<"Could not open the file"<<endl;
    }

    return 0;
}
