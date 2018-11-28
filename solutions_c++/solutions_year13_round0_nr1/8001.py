#include <iostream>
#include <fstream>
using namespace std;
int explode(string str, string delim, string *result);

int main(int argc, char **argv)
{
    char temp[1024];
    int testCases = 0;
    string board[4][4];
    ifstream iFile("A-small-attempt0.in");
    ofstream output("out.txt");
    string message = "";
    
    if(iFile.fail())
    {
        cout<<"Unable to open input file!"<<endl;
        exit(1);
    }
   
    iFile.getline(temp, 1024);
    testCases = atoi(temp);
    //cout<<testCases<<endl;
            
    for(int i=0; testCases > i; ++i)
    {
        for(int j=0; 5 > j; ++j)
        {
            iFile.getline(temp, 1024);
            string input(temp);
            if("" == input) 
                continue;
            for(int k=0; 4 > k; ++k)
                board[j][k] = input.substr(k, 1);
            
            /*for(int k=0; 4 > k; ++k)
                cout<<board[j][k];
            cout<<" ";*/
        }
        bool won = false;
        string player = "";
        /****************************** row wise ******************************/
        for(int j=0; 4 > j; ++j)
        {
            won = false;
            player = "";
            int count = 1;
            for(int k=0; 4 > k; ++k)
            {
                if("." == board[j][k])
                    break;
                if(!k)
                {
                    player = board[j][k];
                }
                else
                {
                    if("T" == player)
                        player = board[j][k];
                    if(player == board[j][k] || "T" == board[j][k])
                        count++;
                    else
                        break;
                }   
            }
            if(4 <= count)
            {
                won = true;
                break;
            }
            /*if(won)
                cout<<player<<" won: "<<i<<endl;*/
        }
        /**********************************************************************/
        
       
        /****************************** col wise ******************************/
        if(!won)
            for(int j=0; 4 > j; ++j)
            {
                won = false;
                player = "";
                int count = 1;
                for(int k=0; 4 > k; ++k)
                {
                    if("." == board[k][j])
                        break;
                    if(!k)
                    {
                        player = board[k][j];
                    }
                    else
                    {
                        if("T" == player)
                            player = board[k][j];
                        if(player == board[k][j] || "T" == board[k][j])
                            count++;
                        else
                            break;
                    }   
                }
                if(4 <= count)
                {
                    won = true;
                    break;
                }
                /*if(won)
                    cout<<player<<" won: "<<i<<endl;*/
            }
        /**********************************************************************/
        if(!won)
        {
            player = "";
            int count = 1;
            for(int j=0; 4 > j; ++j)
            {
                won = false;
                for(int k=0; 4 > k; ++k)
                {
                    if(k!=j)
                        continue;
                    
                    if("." == board[j][k])
                        break;
                    if(!k)
                    {
                        player = board[j][k];
                    }
                    else
                    {
                        if("T" == player)
                            player = board[j][k];
                        if(player == board[j][k] || "T" == board[j][k])
                            count++;
                        else
                            ;//break;
                    }
                    //cout<<player<<"p "<<board[j][k]<<" ";   
                }
                if(4 <= count)
                {
                    won = true;
                    break;
                }
                /*if(won)
                    cout<<player<<" won: "<<i<<endl;*/
            }
        }
        /**********************************************************************/
        if(!won)
        {
            player = "";
            int count = 1;
            for(int j=0; 4 > j; ++j)
            {
                won = false;
                for(int k=3; 0<=k; --k)
                {
                    if(k + j != 3)
                        continue;
                    
                    if("." == board[j][k])
                        break;
                    if(k==3)
                    {
                        player = board[j][k];
                    }
                    else
                    {
                        if("T" == player)
                            player = board[j][k];
                        if(player == board[j][k] || "T" == board[j][k])
                            count++;
                        else
                            ;//break;
                    }
                    //cout<<player<<"p "<<board[j][k]<<" ";   
                }
                if(4 <= count)
                {
                    won = true;
                    break;
                }
                /*if(won)
                    cout<<player<<" won: "<<i<<endl;*/
            }
        }
        if(won)
             message = player + " won";
        else
        {
            bool full = false;
            for(int j=0; 4>j; ++j)
                for(int k=0; 4>k; ++k)
                    if("." == board[j][k])
                    {
                        full = false;
                        break;
                    }
                    else
                        full = true;
            
            if(full)
                message = "Draw";
            else
                message = "Game has not completed";
        }
        //cout<<endl;
        output<<"Case #"<<i+1<<": "<<message<<endl;
    }
    output.close();
    
    
    return 0;
}



int explode(string str, string delim, string *result)
{
    char *token;
    char cStr[1024];
    int i = 0;
    strcpy(cStr, str.c_str());
    
    token = strtok(cStr, delim.c_str());
    while(token!=NULL)
    {
        result[i++] = token;
        token = strtok(NULL, delim.c_str());
    }
    return i;
}
