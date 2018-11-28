#include<iostream>
#include<string>
#include<cstring>
#include<map>

using namespace std; 


int sum(char c1 , char c2 , char c3 , char c4, bool & full)
{
    map<char , int> m ; 
    m.insert(pair<char,int>('X',1));
    m.insert(pair<char,int>('O',2));

    int sum = 0 ; 
    char cs[] = {c1 , c2 , c3 , c4} ; 
    for (int i = 0 ; i < 4; i ++)
    {
        if(cs[i] == 'T')
        {
            if(i == 0 ) 
                sum += m[cs[1]] ; 
            else 
                sum += m[cs[i-1]];
             
        }
        else if(cs[i] == 'X' || cs[i] == 'O')
        {
            sum += m[cs[i]] ; 
        }
        else 
        {
            sum = -1 ; 
            full = false; 
            break;  
        }
    }
    
    return sum ; 
}


void work()
{
    int T ; 
    cin >> T ; 
    for(int t = 1 ; t <= T ; t++)
    {
        char board[4][4] ; 
        for(int i = 0 ; i < 4; i ++)
            for (int j = 0 ; j < 4; j ++)
                cin >> board[i][j] ;   

        bool full = true; 
        bool over = false; 
        //row 
        for(int r = 0 ; r < 4 ; r++)
        {
            int s = sum(
            board[r][0] ,          
            board[r][1] ,          
            board[r][2] ,          
            board[r][3] ,          
            full);
            
            if(s == 4) 
            {
                cout << "Case #" << t <<": X won" << endl;
                over = true; 
                break; 
            }else if(s == 8 ) 
            {
                cout << "Case #" << t <<": O won" << endl;
                over = true; 
                break; 
            }
        }

        if(over) 
            continue ;
        //column 
        for(int c = 0 ; c < 4; c++) 
        {
            int s = sum(
            board[0][c], 
            board[1][c], 
            board[2][c], 
            board[3][c], 
            full); 

            if(s == 4) 
            {
                cout << "Case #" << t <<": X won" << endl;
                over = true; 
                break; 
            }else if(s == 8 ) 
            {
                cout << "Case #" << t <<": O won" << endl;
                over = true; 
                break; 
            }
        }

        if (over)
            continue ; 

        //dig
        int s = sum(
            board[0][0], 
            board[1][1], 
            board[2][2], 
            board[3][3], 
            full);
       
            if(s == 4) 
            {
                cout << "Case #" << t <<": X won" << endl;
                over = true; 
                continue ; 
            }else if(s == 8 ) 
            {
                cout << "Case #" << t <<": O won" << endl;
                over = true; 
                continue ; 
            }

        s = sum(
            board[0][3], 
            board[1][2], 
            board[2][1], 
            board[3][0], 
            full);
       
            if(s == 4) 
            {
                cout << "Case #" << t <<": X won" << endl;
                over = true; 
                continue ; 
            }else if(s == 8 ) 
            {
                cout << "Case #" << t <<": O won" << endl;
                over = true; 
                continue ;
            }


        if( full ) 
            cout << "Case #" << t <<": Draw" << endl;  
        else 
            cout << "Case #" << t <<": Game has not completed" << endl;  
            
    }//T 

}

int main()
{
    work();
    return 0 ; 
}
