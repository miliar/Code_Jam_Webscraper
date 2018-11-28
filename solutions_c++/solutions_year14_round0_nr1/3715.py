#include <iostream>
#include <map>
#include <fstream>
using namespace std;

int main(){
    ofstream cout("archivo.txt");
    int casos;
    cin>>casos;
    int c=1;
    while(casos--){
        int cont=0,num;
        int resp1,resp2;
        cin>>resp1;
        map<int,int> num1;
        for(int i=0;i<4;i++){
            if(resp1==i+1){
                for(int j=0;j<4;j++){
                    int n;
                    cin>>n;
                    num1[n];
                }
            }else{
                for(int j=0;j<4;j++){
                    int a;
                    cin>>a;
                }
            }
        }
        cin>>resp2;
        for(int i=0;i<4;i++){
            if(resp2==i+1){
                cont=0;
                for(int j=0;j<4;j++){
                    int n;
                    cin>>n;
                    map<int,int>::iterator it=num1.find(n);
                    if(it!=num1.end()){
                        cont++;
                        num=it->first;
                    }
                }
            }else{
                for(int j=0;j<4;j++){
                    int a;
                    cin>>a;
                }
            }
        }
        if(cont==0){
            cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
        }
        else{
            if(cont==1){
                cout<<"Case #"<<c<<": "<<num<<endl;
            }else
            cout<<"Case #"<<c<<": Bad magician!"<<endl;
        }
        c++;
    }
    cout.close();
    return 0;
}
