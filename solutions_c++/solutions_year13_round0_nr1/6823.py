

#include <iostream>

using namespace std;

/*
 * 
 */

char check(char a , char b , char c , char d){
    if(a == 'T')
        if (b==c && c==d)
            return b;
    if (b == 'T')
        if (c==a && c==d)
            return c;
    if (c == 'T')
        if(a==b && d==b)
            return a;
    if (d == 'T')
        if (a==b && b==c)
            return a;
    if(a==b && b==c && c==d)
        return c;
    return 'n';
}
struct str{
    char input[4][4];
};
int main(int argc, char** argv) {
    int t;
    str inp[11];
    cin >> t;
    for(int l=0;l<t;l++){
        for (int i=0;i<4;i++)
                cin>>inp[l].input[i];
    }
    for(int k = 0;k<t;k++){
        cout <<"\nCase #"<<k+1<<": ";
    int flag = 0;
    for (int i=0;i<4;i++){
        char ans = check(inp[k].input[i][0],inp[k].input[i][1],inp[k].input[i][2],inp[k].input[i][3]);
        if (ans != 'n'){
            if (ans == 'X' || ans == 'O'){
                cout<<ans<<" won";
                flag =1;
                break;
            }
        }
        ans = check(inp[k].input[0][i],inp[k].input[1][i],inp[k].input[2][i],inp[k].input[3][i]);
        if (ans != 'n'){
            if (ans == 'X' || ans == 'O'){
                cout<<ans<<" won";
                flag =1;
                break;
            }
        }
        ans = check(inp[k].input[0][0],inp[k].input[1][1],inp[k].input[2][2],inp[k].input[3][3]);
        if (ans != 'n'){
            if (ans == 'X' || ans == 'O'){
                cout<<ans<<" won";
                flag = 1;
                break;
            }
        }
        ans = check(inp[k].input[0][3],inp[k].input[1][2],inp[k].input[2][1],inp[k].input[3][0]);
        if (ans != 'n'){
            if (ans == 'X' || ans == 'O'){
                cout<<ans<<" won";
                flag = 1;
                break;
            }
        }
        
    }
    int fl = 0; 
    if (flag !=1){
        for (int i=0;i<4;i++){
            for(int j=0 ; j<4 ; j++)
                if(inp[k].input[i][j] == '.'){
                    fl = 1;
                    break;
                }
        }
        if (fl==0)
                cout <<"Draw";
        else 
            cout <<"Game has not completed";
    }
    }
    cout <<"\n";
    
    return 0;
}

