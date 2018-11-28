#include <iostream>
#include <fstream>
//#include <math>
#include<vector>

using namespace std;

unsigned int base[4][4]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768};
  
//#define CHECK (s[i]=="XXXX"||s[i]=="OOOO"||s[i]=="TXXX"||s[i]=="XTXX"||s[i]=="XXTX"||s[i]=="XXXT"||s[i]=="TOOO"||s[i]=="OTOO"||s[i]=="OOTO"||s[i]=="OOOT")

bool wingame(unsigned int z){//cout<<z<<endl;
    if(z==15 || z==240 || z==3840 || z==61440) return true;
    if(z==4369 || z==8738 || z==17476 || z==34952) return true;
    if(z==33825 || z==4680) return true;
    return false;
}

int main(){
    ifstream fin;
    ofstream fout;
  //  fstream fi=("",in);
    fin.open("/Users/xianpan/Desktop/code/codejam13/A-large.txt");
    fout.open("/Users/xianpan/Desktop/code/codejam13/A-largeres.txt");
    if(!fin.is_open())
        cout<<"in open error"<<endl;
    if(!fout.is_open())
        cout<<"out open error"<<endl;
    
    int cases=0;
    fin>>cases; cout<<cases<<endl;
    char ch;
//    fin.get(ch);
    
    int cc=0;
    for(cc=1; cc<=cases; cc++){
        fout<<"Case #"<<cc<<": ";
    
        string s[4];
        fin.get(ch);
        for(int i=0;i<4;i++){
            getline(fin,s[i]);
        }
        for(int i=0;i<4;i++){
            cout<<s[i]<<endl;
        }
    
        unsigned int x=0; unsigned int y=0;
        bool hasempty = false;
        bool win=false;
        bool dot=false;
        for(int i=0; i<4;i++){
            for(int j=0;j<4;j++){
                if(s[i][j]=='.') {hasempty=true;dot=true;break;}
                else if(s[i][j]=='X') x+=base[i][j];
                else if(s[i][j]=='O') y+=base[i][j];
                else{
                    x+=base[i][j]; y+=base[i][j];
                }
            }
            if(dot==false){
                if(wingame(x)) {fout<<"X won"<<endl;win=true;break;}
                if(wingame(y)) {fout<<"O won"<<endl;win=true;break;}
            }
            dot=false; x=0; y=0;
        }
        if(win==true){win=false;continue;}
    
        for(int i=0; i<4;i++){
            for(int j=0;j<4;j++){
                if(s[j][i]=='.') {hasempty=true;dot=true;break;}
                else if(s[j][i]=='X') x+=base[j][i];
                else if(s[j][i]=='O') y+=base[j][i];
                else{
                    x+=base[j][i]; y+=base[j][i];
                }
            }
            if(dot==false){
                if(wingame(x)) {fout<<"X won"<<endl;win=true;break;}
                if(wingame(y)) {fout<<"O won"<<endl;win=true;break;}
            }
            dot=false; x=0; y=0;
        }
        if(win==true){win=false;continue;}

        for(int j=0;j<4;j++){
            if(s[j][j]=='.') {hasempty=true;dot=true;break;}
            else if(s[j][j]=='X') x+=base[j][j];
            else if(s[j][j]=='O') y+=base[j][j];
            else{
                x+=base[j][j]; y+=base[j][j];
            }
        }
        if(dot==false){
            if(wingame(x)) {fout<<"X won"<<endl;win=true;}
            if(wingame(y)) {fout<<"O won"<<endl;win=true;}
        }
        dot=false; x=0; y=0;
        if(win==true){win=false;continue;}
        
        int i=3;
        for(int j=0;j<4;j++,i--){
            if(s[j][i]=='.') {hasempty=true;dot=true;break;}
            else if(s[j][i]=='X') x+=base[j][i];
            else if(s[j][i]=='O') y+=base[j][i];
            else{
                x+=base[j][i]; y+=base[j][i];
            }
        }
        if(dot==false){
            if(wingame(x)) {fout<<"X won"<<endl;win=true;}
            if(wingame(y)) {fout<<"O won"<<endl;win=true;}
        }
        dot=false; x=0; y=0;
        if(win==true){win=false;continue;}
        
        if(hasempty==false) fout<<"Draw"<<endl;
        else fout<<"Game has not completed"<<endl;
        
    //    fin.get(ch); cout<<cc<<"M;"<<cases<<endl;
    }
cout<<cc<<";"<<cases<<endl;
    fin.close();
    fout.close();
}
