#include<iostream>
#include<fstream>

using namespace std;

int main()
{
    ifstream fin("Dsmall1.in.txt");
    ofstream fout("Dsmall0000000.out");
    int t;
    fin>>t;
    for(int h=0;h<t;h++){
        int x,r,c;
        fin>>x>>r>>c;
        if((x==1)){
            fout<<"Case #"<<h+1<<": GABRIEL"<<endl;
            continue;
        }
        if((x>=3)&&((r<2)||(c<2))){
            fout<<"Case #"<<h+1<<": RICHARD"<<endl;
            continue;
        }
        if((x==4)){
            if((r<=2)||(c<=2)){
                fout<<"Case #"<<h+1<<": RICHARD"<<endl;
            continue;
            }
        }
        if((r*c)%x!=0){
            fout<<"Case #"<<h+1<<": RICHARD"<<endl;
            continue;
        }
        else{
            fout<<"Case #"<<h+1<<": GABRIEL"<<endl;
            continue;
        }
    }
}
