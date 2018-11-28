#include <iostream>
#include<fstream>
using namespace std;

void fill_grid(int**ex){
    for(int i=0;i<4;i++){
        ex[i]=new int[4];
        }
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++)
            cin>>ex[i][j];
        }
    }
int main(){
    ofstream fs("nombre.txt");
    int T,answer1,answer2,temp=0,iter=0,stop=1;
    int**a;
    a=new int*[4];
    int**b;
    b=new int*[4];
    cin>>T;
    do{
        cin>>answer1;
        fill_grid(a);
        cin>>answer2;
        fill_grid(b);

        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(a[answer1-1][i]==b[answer2-1][j]){
                    iter++;
                    temp=a[answer1-1][i];
                    }
                }
            }
        cout<<endl;
        if(iter==1)
            fs<<"Case #"<<stop<<": "<<temp<<endl;
        else if(iter>1)
            fs<<"Case #"<<stop<<": "<<"Bad magician!"<<endl;
        else if(iter==0)
            fs<<"Case #"<<stop<<":  "<<"Volunteer cheated!"<<endl;
        iter=0;
        temp=0;
        stop++;
        }
    while(stop<=T);
    return 0;
    }
