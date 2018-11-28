#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int T;
    char first;
    int status=0,finished=1;
    //status:  1:decided 0:undecided
    char table[4][4];
    ifstream tin("in");
    ofstream tout("out");
    tin>>T;
    for(int count=1;count<=T;++count){
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j){
                tin>>table[i][j];
                if(table[i][j]=='.')
                    finished=0;
            }

        for(int i=0;i<4;++i){
            first=table[i][0];
            if(first=='.')
                continue;
            if(first=='T')
                first=table[i][1];
            status=1;
            for(int j=1;j<4;++j)
                if(first!=table[i][j] && table[i][j]!='T'){
                    status=0;
                    break;
                }
            if(status==1)
                goto end;
        }

        for(int i=0;i<4;++i){
            first=table[0][i];
            if(first=='.')
                continue;
            if(first=='T')
                first=table[1][i];
            status=1;
            for(int j=1;j<4;++j)
                if(first!=table[j][i] && table[j][i]!='T'){
                    status=0;
                    break;
                }
            if(status==1)
                goto end;
        }

        if(table[0][0]!='.'){
            first=table[0][0];
            if(first=='T')
                first=table[1][1];
            status=1;
            for(int i=1;i<4;++i)
                if(first!=table[i][i] && table[i][i]!='T'){
                    status=0;
                    break;
                }
            if(status==1)
                goto end;
        }
        
        if(table[0][3]!='.'){
            first=table[0][3];
            if(first=='T')
                first=table[1][2];
            status=1;
            for(int i=1;i<4;++i)
                if(first!=table[i][3-i] && table[i][3-i]!='T'){
                    status=0;
                    break;
                }
            if(status==1)
                goto end;
        }

        end:
        tout<<"Case #"<<count<<": ";
        if(status)
            tout<<first<<" won"<<endl;
        else
            if(finished)
                tout<<"Draw"<<endl;
            else
                tout<<"Game has not completed"<<endl;
        status=0;
        finished=1;
    }
    tin.close();
    tout.close();
}
