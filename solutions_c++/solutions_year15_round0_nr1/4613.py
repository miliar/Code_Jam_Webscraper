#include<iostream>
#include<fstream>
#include<vector>


using namespace std;
main(){
    ifstream in("A-large.in");
    ofstream out("output.txt");

    int T;
    in>>T;
    for(int l=1;l<=T;l++){

     int t;
        int x;
        in>>x;
        x++;
        int a=0,m=0;
            string  s;
            in>>s;
        for(int i=0;i<s.size();i++){
           t=s[i]-'0';
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
