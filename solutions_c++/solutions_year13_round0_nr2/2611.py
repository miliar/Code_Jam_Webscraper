#include<iostream>
#include<string>
#include<vector>
#include<fstream>
#include<sstream>
#include<map>
#include<set>

using namespace std;

int field[256][256];
int N,M;

int check(){
    for(int n=0;n<N;n++) for(int m=0;m<M;m++){
        bool row = true;
        for(int i=0;i<M;i++){
            if(field[n][i]>field[n][m]){
                row=false; break;
            }
        }

        bool column = true;
        for(int i=0;i<M;i++){
            if(field[i][m]>field[n][m]){
                column=false; break;
            }
        }

        if(!row && !column) return false;
    }
    return true;
}


int main(int argc, char* argv[])
{
    if(argc != 2){
        cout<<argv[0]<<" input_file"<<endl;
        return 0;
    }

    fstream file(argv[1]);

    char line[1024];
    file.getline(line, 1024);

    int T = atoi(line);

    for(int t=0;t<T;t++){
        file.getline(line, 1024);
        stringstream ss(line);
        ss>>N>>M;

        memset(field, 0x0, sizeof(field));

        for(int i=0;i<N;i++){
            file.getline(line, 1024);
            stringstream ss(line);
            for(int j=0;j<M;j++){
                int V;
                ss>>V;
                field[i][j]=V;
            }
        }

        bool res = check();

        cout<<"Case #"<<t+1<<": "<<(res?"YES":"NO")<<endl;
    }
    return 0;
}
