//
//  main.cpp
//  T4
//
//  Created by Tanifuji Keita on 13/04/13.
//  Copyright (c) 2013年 Tanifuji Keita. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

namespace GameState
{
    enum EnumType
    {
        WonX,
        WonO,
        Draw,
        Playing,
        TERM
    };
}

class Board {
public:
    Board(const char * argv[])
    {
        GameState = GameState::Playing;
        for (int y = 0; y < Height; ++y )
        {
            for (int x = 0; x < Width; ++x)
            {
                cin >> Table[y][x];
            }
        }
    }
    
    //====================================================================
    void check()
    {
        // 横
        for( int y = 0; y < Height; ++y )
        {
            checkCore(0, y, 1, 0);
            if( GameState != GameState::Playing )
            {
                return;
            }
        }
        
        // 縦
        for( int x = 0; x < Width; ++x )
        {
            checkCore(x, 0, 0, 1);
            if( GameState != GameState::Playing )
            {
                return;
            }
        }
        
        // 斜め
        checkCore(0,0,1,1);
        if( GameState != GameState::Playing )
        {
            return;
        }
        checkCore(3,0,-1,1);
        if( GameState != GameState::Playing )
        {
            return;
        }
        
        if( isExistEmpty() )
        {
            return;
        }
        
        GameState = GameState::Draw;
    }
    
    void checkCore(const int sx, const int sy, const int dx, const int dy)
    {
        int panelX = 0, panelO = 0, panelT = 0;
        int x = sx, y = sy;
        for(int i = 0; i < 4; ++i)
        {
            switch ( Table[y][x] )
            {
                case 'X': panelX++; break;
                case 'O': panelO++; break;
                case 'T': panelT++; break;
                default:  break;
            }
            x += dx;
            y += dy;
        }
        
        if( panelX == 4 || (panelX ==3 && panelT == 1) )
        {
            GameState = GameState::WonX;
            return;
        }
        
        if( panelO == 4 || (panelO ==3 && panelT == 1) )
        {
            GameState = GameState::WonO;
            return;
        }
    }
    
    bool isExistEmpty()
    {
        for (int y = 0; y < Height; ++y )
        {
            for (int x = 0; x < Width; ++x)
            {
                if( Table[y][x] == '.' )
                {
                    return true;
                }
            }
        }
        return false;
    }
    
    //====================================================================
    
    void dump()
    {
        for (int y = 0; y < Height; ++y )
        {
            for (int x = 0; x < Width; ++x)
            {
                cout << Table[y][x];
            }
            cout << endl;
        }
        cout << endl;
    }
    
    
public:
    static const int Width = 4;
    static const int Height = 4;
    static const int PanelCount = Width * Height;
    char Table[Height][Width];
    GameState::EnumType GameState;
};

namespace Util {
    void WriteResult( const int TestNumber, const GameState::EnumType State )
    {
        stringstream ss;
        ss << TestNumber;
        cout << "Case #" << ss.str() << ": ";
        switch ( State )
        {
            case GameState::WonX:
                cout << "X won" << endl;
                break;
            case GameState::WonO:
                cout << "O won" << endl;
                break;
            case GameState::Draw:
                cout << "Draw" << endl;
                break;
            case GameState::Playing:
                cout << "Game has not completed" << endl;
                break;
            default:
                break;
        }
    }
}

int main(int argc, const char * argv[])
{
    int TestCount = 0;
    cin >> TestCount;
    
    for (int i = 0; i < TestCount; ++i)
    {
        Board board(argv);
        board.check();
        Util::WriteResult(i+1,board.GameState);
        //board.dump();
    }
    
    return 0;
}

