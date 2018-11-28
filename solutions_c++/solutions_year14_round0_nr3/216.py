#include <iostream>
#include <fstream>
using namespace std;
void PrintResult(int R, int C,int M){
    int r=R,c=C,n=R*C-M;
    if(c>1&&r>1&&(n==(2*r+1)|n<2*r)){
        PrintResult(R-1,C,M-C);
        for(int i=0;i<C;i++)cout<<'*';
        cout<<endl;
        return;
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(j<(n/r)){
                //map[i*c+j]='.';
                if(i==0&j==0){
                    cout<<"c";
                }
                else if(n%r==1){
                    if(i==(r-1)&&j==((n/r)-1))cout<<"*";
                     else cout<<".";
                }
                else cout<<".";
            }else if(j==(n/r)){
                if(i==0&j==0){
                    cout<<"c";
                }
                else if(n%r==1&&j!=0){
                    if(i>1)cout<<"*";
                    else cout<<".";
                }
                else{
                    if (i>(n%r-1))cout<<"*";
                    else cout<<".";
                }
            }else{
                if(i==0&j==0)cout<<"c";
                else cout<<"*";
            }
        }
        cout<<endl;
    }
}
int calculate(int R, int C,int M){
    if(R>C)swap(R,C);
    int N=R*C-M;
    if(R>2){
        if(N==2|N==3|N==5|N==7)return 0;
    }else if(R==2){
        if(N==1)return 1;
        if((N==2)|(N%2))return 0;
    }else if(R==1){
        return 1;
    }else if(R<1)return 0;
    return 1;
}
int main(int argc, const char * argv[])
{
    ifstream fin("data3.txt");
    int NumberOfTricks;
    int R,C,M;
    fin>>NumberOfTricks;
    for(int i;i<NumberOfTricks;i++){
        fin>>R>>C>>M;
        if(calculate(R,C,M)){
            cout<<"Case #"<<i+1<<": "<<endl;
            PrintResult(R,C,M);
        }else{
            cout<<"Case #"<<i+1<<": "<<endl<<"Impossible"<<endl;
        }
    }
    return 0;
}

