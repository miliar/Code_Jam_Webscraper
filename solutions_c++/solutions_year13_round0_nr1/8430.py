/* 
 * Email : 12MCA17@nirmauni.ac.in       
 * Defination: Tic-Tac-Toe-Tomec
 */

#include <cstdlib>
#include <iostream>

using namespace std;
class matrix{
public :
    char mat[4][4];
    void get_inputs(){
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>mat[i][j];
            }
        }
    }
    char check_diag2(char meta){
        char res='N';
        if(mat[3][0]==meta || mat[3][0]=='T') 
            if(mat[2][1]==meta || mat[2][1]=='T')
                if(mat[1][2]==meta || mat[1][2]=='T')
                    if(mat[0][3]==meta || mat[0][3]=='T')
                        res='Y';
        return res; 
    }
    char check_row(char meta){
        char res='N';
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(mat[i][j]==meta || mat[i][j]=='T'){
                    res='Y';
                }
                else
                {
                    res='N';
                    break;
                }
            }
            if(res=='Y')
                break;
        }
        return res;
    }
    char check_col(char meta){
          char res='N';
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                   if(mat[j][i]==meta || mat[j][i]=='T'){
                    res='Y';
                }
                else
                {
                    res='N';
                    break;
                }
            }
            if(res=='Y')
                break;
        }
          return res;
    }
    char check_diag1(char meta){
        char res='N';
            for(int j=0;j<4;j++){                                                                             
                if(mat[j][j]==meta || mat[j][j]=='T'){
                    res='Y';
                }
                    
                else{    
                    res='N';
                    break;
                }
            }
             
        return res;
    }
        
    char check_dot(){
        char res='N';
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(mat[i][j]=='.'){
                    res='Y';
                    break;
                }
            }
        }
        return res;
    }
};
int main(int argc, char** argv) {
    for(int i=0;i<10;i++)
    {
        int ans=0;
    matrix m;
    m.get_inputs();
    if(m.check_col('X')=='Y' || m.check_row('X')=='Y'|| m.check_diag1('X')=='Y' || m.check_diag2('X')=='Y'){
        cout<<"\n Case #"<<i+1<<": X won";
        ans=1;
    }
     if(m.check_col('O')=='Y' || m.check_row('O')=='Y'|| m.check_diag1('O')=='Y' || m.check_diag2('O')=='Y'){
        cout<<"\n Case #"<<i+1<<": O won";
        ans=1;
    }
     if(m.check_dot()=='Y'){
         if(ans==0){
                cout<<"\n Case #"<<i+1<<": Game has not completed";
                ans=1;
         }
    }
    else {
         if(ans==0)
                cout<<"\n Case #"<<i+1<<": Draw";
    }
    cout<<"\n";
    }
    
    return 0;
}

