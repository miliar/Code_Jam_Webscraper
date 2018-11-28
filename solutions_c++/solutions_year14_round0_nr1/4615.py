#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout;
    fout.open("out.txt");
    ifstream fin;
    fin.open("A-small-attempt0.in");
    int T;
    int caseNum = 0;
    fin>>T;
    int first[4],second[4],maze[4][4];
    while(caseNum < T){
        caseNum++;
        fout<<"Case #"<<caseNum<<": ";
        int n;
        fin>>n;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++)
                fin>>maze[i][j];
        }
        for(int i = 0; i < 4; i++)
            first[i] = maze[n-1][i];
        fin>>n;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++)
                fin>>maze[i][j];
        }
        for(int i = 0; i < 4; i++)
            second[i] = maze[n-1][i];
        int result = -1;
        for(int i = 0; i < 4; i++){
            for(int j = 0; j < 4; j++){
                if(first[i] == second[j]){
                    if(result == -1)
                        result = first[i];
                    else{
                        result = -2;
                        break;
                    }
                }
            }
            if(result == -2)
                break;
        }
        switch(result){
            case -1 : fout<<"Volunteer cheated!"<<endl;break;
            case -2 : fout<<"Bad magician!"<<endl;break;
            default : fout<<result<<endl;break;
        }
    }
    return 0;
}
