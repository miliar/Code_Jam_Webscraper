#include<iostream>
#include<fstream>
#include<vector>


using namespace std;
main(){
    ifstream in("A-large.in");
    ofstream out("output.txt");

    int a;
    in>>a;
    for(int l=1;l<=a;l++){

     int t;
        int x;
        in>>x;
        x++;
        int a=0,m=0;
            string  e;
            in>>e;
        for(int i=0;i<e.size();i++){
           t=e[i]-'0';
            if(t!=0){
                if(i<=a){
                    a+=t;
                }else{
                    m+=i-a;
                    a+=(i-a)+t;
                }
            }
        }
        out<<"Case #"<<l<<": "<<m<<endl;

    }



}
