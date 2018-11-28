#include<iostream>
#include<fstream>
using namespace std;

class answer{
string a;
int Size;
bool allpositive;
int turns;
public:
    int strlen(string hehe){
        int i=0;
        for(;hehe[i]!='\0';++i);
        return i;
    }

    void get_S(){
        do{
            cin >> a;
            Size = strlen(a);
        }while(Size<1 || Size>100);
    turns =0;
    }
    void all_positive_check(){

        for(int i=0;i<Size;++i){if(a[i]!='+'){allpositive=false;break;}else{allpositive=true;}}
    }

    int get_last_index(){
    int maxi =0;
        for(int i=0;i<Size;++i){
            if(a[i]=='-'){
                if(i>maxi){
                    maxi = i;
                }
            }
        }
        return maxi;
    }

    void changes(){
    all_positive_check();
    int tmp;
    while(!allpositive){
        tmp = get_last_index();
        for(int i=0;i<=tmp;++i){
            if(a[i]=='-')a[i]='+';
            else a[i]='-';
        }
    turns++;
    all_positive_check();
    }
    }
    int get_turns(){
    return turns;
    }
};

int main(){
freopen("B-large.in","r",stdin);
ofstream fout("google_output_9v2.txt",ios::out);
int tests;
do{
    cin >> tests;
}while(tests<0 || tests>100);
answer *p = new answer[tests];
for(int i =0;i<tests;++i){
    p[i].get_S();
    p[i].changes();
}
for(int i =0;i<tests;++i){
    fout << "Case #"<<(i+1)<<": " << p[i].get_turns();
    fout << endl;
}

fout.close();

return 0;
}
