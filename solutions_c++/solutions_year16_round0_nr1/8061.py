#include<iostream>
#include<fstream>
using namespace std;
class answer{
long N,changed_N;
bool _1,_2,_3,_4,_5,_6,_7,_8,_9,_0;
public:
    answer(){
    _1=false;
    _2=false;
    _3=false;
    _4=false;
    _5=false;
    _6=false;
    _7=false;
    _8=false;
    _9=false;
    _0=false;
    }
    void enter_number(){
        cin >> N;
    }
    int get_f_number(){
    return changed_N;}
    int get_number(){return N;}
    void splitter(){
    int tmp_n;
    int i=1;
    while(!(_1&&_2&&_3&&_4&&_5&&_6&&_7&&_8&&_9&&_0)){
     tmp_n = i*N;
     changed_N = i*N;
        while(tmp_n!=0){
            if(tmp_n%10==1){_1=true;}
            else if(tmp_n%10==2){_2=true;}
            else if(tmp_n%10==3){_3=true;}
            else if(tmp_n%10==4){_4=true;}
            else if(tmp_n%10==5){_5=true;}
            else if(tmp_n%10==6){_6=true;}
            else if(tmp_n%10==7){_7=true;}
            else if(tmp_n%10==8){_8=true;}
            else if(tmp_n%10==9){_9=true;}
            else if(tmp_n%10==0){_0=true;}
            tmp_n = tmp_n/10;
        }
    //if(!(_1&&_2&&_3&&_4&&_5&&_6&&_7&&_8&&_9&&_0))N*=2;
    ++i;
    }

    }
} ;

int main(){
freopen("A-large.in","r",stdin);
ofstream fout("OUT_GOOGLE.txt",ios::out);
int test_cases;
do{
    cin >> test_cases;
}while(test_cases<1 || test_cases>100);
answer *p = new answer[test_cases];
for(int run = 0; run < test_cases;++run){
    p[run].enter_number();
    if(p[run].get_number()!=0)p[run].splitter();
}
for(int i =0; i<test_cases;++i){
    fout << "Case #" << (i+1) << ": ";
    if(p[i].get_number()==0) fout << "INSOMNIA";
    else fout << p[i].get_f_number();
    fout << endl;
}

freopen("OUTPUT_GOOGLE.out","w",stdout);
return 0;
}
