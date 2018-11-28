#include<iostream>
#include<fstream>
#include<vector>


using namespace std;
main(){
    ifstream in("A-large.in");
    ofstream out("output.txt");

    int r;
    in>>r;
    int l=1;
    while(l<=r){

     int t;
        int x;
        in>>x;
        x++;
        int a=0,m=0;
            string  s;
            in>>s;
            int i=0;
        while(i<s.size()){
           t=s[i]-'0';
            if(t!=0){
                if(i<=a){
                    a+=t;
                }else{
                    m+=i-a;
                    a+=(i-a)+t;
                }
            }
            i++;
        }
        out<<"Case #"<<l<<": "<<m<<endl;
        l++;

    }



}
