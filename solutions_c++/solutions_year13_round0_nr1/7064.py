#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

int try_line(vector<vector<char> > board, vector<int> begin, vector<int> direction);

template<typename T>
void dump(vector<vector<T>> board){
    for(auto& line:board){
        for(T& c:line){
            cout<<c;
        }
        cout<<endl;
    }
}

bool is_finished(vector<vector<char>> board){
    for(auto& line:board){
        for(char& c:line){
            if(c=='.'){
                return false;
            }
        }
    }
    return true;
}

template<typename T>
void dump(vector<T> vec){
    for(auto& e:vec){
        cout<<e;
    }
    cout<<endl;
}

//-1 if no one
//0 if O
//1 if X
int analyze(vector<vector<char> > board){
    for(int i=0;i<4;i++){
        int r1=try_line(board, {i,0}, {0,1});
        int r2=try_line(board, {0,i}, {1,0});
        if(r1 != -1){
            //cout<<"Search row "<<i<<endl;
            //dump(board[i]);
            return r1;
        }
        if(r2 != -1){
            //cout<<"Search col "<<i<<endl;
            return r2;
        }
    }
    int r1=try_line(board, {0,0}, {1,1});
    int r2=try_line(board, {3,0}, {-1,1});
    if(r1 != -1){
        return r1;
    }
    if(r2 != -1){
        return r2;
    }
    return -1;
}

//-1 if no one
//0 if O
//1 if X
int try_line(vector<vector<char> > board, vector<int> begin, vector<int> direction){
    int x=begin[0];
    int y=begin[1];
    if(board[x][y]=='T'){
        x+= direction[0];
        y+= direction[1];
    }
    char side=board[x][y];
    if(side=='.'){
        return -1;
    }
    x+= direction[0];
    y+= direction[1];
    while(x<4 && y<4){
        if(board[x][y]!=side && board[x][y]!='T'){
            //cout<<board[x][y]<<" "<<side<<endl;
            return -1; //found . or not side
        }
        x+= direction[0];
        y+= direction[1];
    }
    if(side=='O')
        return 0;
    return 1;
}

vector<vector<char> > read_board(){
    string l;
    vector<vector<char> > b;
    for(int line=0;line<4;++line){
        getline(cin,l);
        vector<char> lc;
        for(char& c: l){
            lc.push_back(c);
        }
        b.push_back(lc);
    }
    getline(cin,l);
    return b;
}


int main(){
    int num_boards;
    cin>>num_boards;
    string s;
    getline(cin,s);
    for(int bn=1;bn<=num_boards;bn++){
        cout<<"Case #"<<bn<<": ";
        auto b=read_board();
        //dump(b);
        int winner=analyze(b);
        if(winner>=0){
            if(winner==0){
                cout<<"O";
            }
            else{
                cout<<"X";
            }
            cout<<" won"<<endl;
        }
        else{
            if(is_finished(b)){
                cout<<"Draw"<<endl;
            }
            else{
                cout<<"Game has not completed"<<endl;
            }
        }
    }
    return 0;
}
