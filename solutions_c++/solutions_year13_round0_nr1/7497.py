#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;
int checkwin(map<char,int>,int);
int main()
{
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;t++)
    {
        vector<string> board;
        for(int i=0;i<4;i++)
        {
            string input;
            cin>>input;
            board.push_back(input);
        }
        int end=0,dot=0;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(board[i][j]=='.')
                {
                    dot=1;
                    continue;
                }

                map<char,int> moves;
                moves[board[i][j]]=1;

                //check row
                for(int k=j-1;k>=0;k--)
                    moves[board[i][k]]+=1;

                for(int k=j+1;k<=3;k++)
                    moves[board[i][k]]+=1;

                if(checkwin(moves,t)!=0)
                {
                    end=1;
                    break;
                }


                //check column
                moves.clear();
                moves[board[i][j]]=1;
                for(int k=i-1;k>=0;k--)
                    moves[board[k][j]]+=1;

                for(int k=i+1;k<=3;k++)
                    moves[board[k][j]]+=1;

                if(checkwin(moves,t)!=0)
                {
                    end=1;
                    break;
                }
                //check diagonal
                moves.clear();
                moves[board[i][j]]=1;
                if((i==0 && j==0) || (i==0 && j==3) || (i==3 && j==0) || (i==3 && j==3))
                {
                    for(int k=j-1,r=i+1;k>=0 && r<=3;k--,r++)
                        moves[board[r][k]]+=1;

                    for(int k=j+1,r=i-1;k<=3 && r>=0;k++,r--)
                        moves[board[r][k]]+=1;

                    if(checkwin(moves,t)!=0)
                    {
                        end=1;
                        break;
                    }

                    moves.clear();
                    moves[board[i][j]]=1;
                    for(int k=j+1,r=i+1;k<=3 && r<=3;k++,r++)
                        moves[board[r][k]]+=1;

                    for(int k=j-1,r=i-1;k>=0 && r>=0;k--,r--)
                        moves[board[r][k]]+=1;

                    if(checkwin(moves,t)!=0)
                    {
                        end=1;
                        break;
                    }

                }

            }
            if(end==1)
                break;
        }
        if(end==0 && dot==1)
            cout<<"Case #"<<t<<": "<<"Game has not completed\n";
        else if(end==0)
            cout<<"Case #"<<t<<": "<<"Draw\n";

    }
    return 0;
}
int checkwin(map<char,int> moves,int tc)
{
    if(moves['O']==4 || (moves['O']==3 && moves['T']==1))
    {
        cout<<"Case #"<<tc<<": "<<"O won\n";
        return 2;
    }
    else if(moves['X']==4 || (moves['X']==3 && moves['T']==1))
    {
        cout<<"Case #"<<tc<<": "<<"X won\n";
        return 1;
    }
    else
        return 0;
}
