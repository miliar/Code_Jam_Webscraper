#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>

using namespace std;
int board[4][4];
void readBoard()
{
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            cin>>board[i][j];
}

int main()
{
    int T, r1, r2;
    cin>>T;
    for(int tt = 1; tt <= T; ++tt)
    {
        cin>>r1;
        readBoard();
        set<int> s1;
        for(int i = 0; i < 4; ++i)
            s1.insert(board[r1 - 1][i]);
        
        cin>>r2;
        readBoard();
        set<int> s2;
        for(int i = 0; i < 4; ++i)
            s2.insert(board[r2 - 1][i]);
        int common = 0;
        set<int>::iterator itr = s1.begin();
        while(itr != s1.end()){
            if(s2.find(*itr) != s2.end())
                common = common * 20 + *itr;
            ++itr;
        }
        cout<<"Case #"<<tt<<": ";
        if(common == 0)
            cout<<"Volunteer cheated!"<<endl;
        else if(common < 20)
            cout<<common<<endl;
        else 
            cout<<"Bad magician!"<<endl;
    }

    return 0;
}
