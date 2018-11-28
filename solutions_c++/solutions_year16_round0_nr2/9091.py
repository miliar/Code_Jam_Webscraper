#include <iostream>
#include <fstream>
#include <string>

using namespace std;
string hold;

void flip(int i,int j){
    string hold2=hold;
    int r=j;
    for(int u=i;j>=i;u++){
        if(hold[u]=='-')
            hold2[j]='+';
        else
            hold2[j]='-';
        j--;
    }
    for(int u=i;u<=r;u++) hold[u]=hold2[u];
}

int main()
{
    ofstream fout ("input.out");
    ifstream fin ("input.in");
    int n;
    fin>>n;
    for(int i=1;i<=n;i++){
        fin>>hold;
        fout<< "Case #" << i<< ": ";
        int len=hold.size();
        if(len==1){
            if(hold[0]=='-')
                fout<<1<<endl;
            else
                fout<<0<<endl;
            continue;
        }
        bool tadhg=false;
        int count=0;
        for(int j=0;j<len;j++)
            if(hold[j]=='-'){
                tadhg=true;
                break;
            }
        while(tadhg){
            tadhg=false;
            count++;
            for(int k=len-1;k>=0;k--){//might be len
                if(hold[k]=='-'){
                    if(hold[0]=='-')
                        flip(0,k);
                    else{
                        int y=1;
                        while(hold[y]=='+')
                            y++;
                        flip(0,y-1);
                        flip(0,k);
                        count++;
                    }
                    break;
                }
            }
            for(int j=0;j<len;j++){
                if(hold[j]=='-'){
                    tadhg=true;
                    break;
                }
            }
        }
        fout<<count<<endl;
    }
    return 0;
}
