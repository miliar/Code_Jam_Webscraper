//
//  main.cpp
//  Minesweeper Master
//
//  Created by Tengqi Ye on 12/04/2014.
//  Copyright (c) 2014 Tengqi Ye. All rights reserved.
//

#include <iostream>
#include <fstream>

bool arrange(char* locations,int R, int C, int M);
void arrangeByRow(char* locations,int R, int C, int M);
void arrangeByColumn(char* locations,int R, int C, int M);

void arrangeByDoubleRow(char* locations, int R, int C, int M);
void arrangeByDoubleColumn(char* locations, int R, int C, int M);

void mineMatrixInit(char* locations, int R, int C);


int main(int argc, const char * argv[])
{

    //open files
    std::ifstream in;
    std::ofstream out;
    
    in.open("C-small-attempt5.in");
    out.open("C-small-attempt5.out");
    
    //global variables
    int T, R, C, M;
    char* arrangement;
    
    //in & out
    in >> T;
    for(int i = 0; i < T; i ++ )
    {
        in >> R >> C >> M;
        
        arrangement = new char[R * C];
        out << "Case #" << i + 1 << ":" << std::endl;
        
        //init the mine map
        mineMatrixInit(arrangement, R, C);
        
        //print the game
        if(arrange(arrangement, R, C, M))
        {
            for( int row = 0; row < R; row ++ )
            {
                for( int column = 0; column < C; column ++ )
                {
                    out << arrangement[row * C + column];
                }
                out << std::endl;
            }
        }else
        {
            out << "Impossible" << std::endl;
        }
        
        //release
        delete [] arrangement;
    }
    
    //close files
    in.close();
    out.close();
    
    
    return 0;
}


bool arrange(char* locations,int R, int C, int M)
{
    //special cases
    if( R == 1 || C == 1 || M == R * C - 1 || M == 0 )
    {
        arrangeByRow(locations, R, C, M);
        return true;
    }
    
    if( R == 2 )
    {
        if( M % 2 == 0 && R * C - M >=4 )
        {
            arrangeByDoubleRow(locations, R, C, M);
            locations[0] = 'c';
            return true;
        }else
        {
//            std::cout << "0: R=" << R << ",C=" << C << ",M=" << M << std::endl;
            return false;
        }
    }
    
    
    if( C == 2 )
    {
        if( M % 2 == 0 && R * C - M >=4 )
        {
            arrangeByDoubleColumn(locations, R, C, M);
            locations[0] = 'c';
            return true;
        }else
        {
//            std::cout << "0: R=" << R << ",C=" << C << ",M=" << M << std::endl;
            return false;
        }
    }
    
    
    if( M <= C * (R-2) )
    {//special cases
        arrangeByRow(locations, R, C, M);
        
        if( (M + 1) % C == 0 )
        {
            if( (M + 1)/C + 2 < R )
            {
                locations[R*C-M] = '.';
                locations[R*C-M-2] = '*';
                return true;
            }
            
            if( (M + 1)/C + 2 == R && C > 3 )
            {
                locations[ R*C-M ] = '.';
                locations[ R*C-M-2 ] = '*';
                
                locations[ R*C-M + 1 ] = '.';
                locations[ R*C-M-2 - C ] = '*';
                
                return true;
            }else
            {
//                std::cout << "1: R=" << R << ",C=" << C << ",M=" << M << std::endl;
                return false;
            }
            
        }else
        {
            return true;
        }
        
    }
    if( M <= R * (C-2) )
    {

        arrangeByColumn(locations, R, C, M);
        
        if( (M + 1) % R == 0 )
        {
            if( (M + 1)/R + 2 < C )
            {
                locations[2 * C - (M+1)/R] = '.';
                locations[C * R + (M+1)/R - 1] = '*';
                return true;
            }

            if( (M + 1)/R + 2 == C && R > 3 )
            {
                locations[ C + 2 ] = '.';
                locations[ C * (R-1) + 1 ] = '*';
                
                locations[ 2 * C + 2 ] = '.';
                locations[ C * (R-1) ] = '*';
                return true;
            }else
            {
//                std::cout << "2: R=" << R << ",C=" << C << ",M=" << M << std::endl;
                return false;
            }
        }else
        {
            return true;
        }

    }
    
    if( (R * C - M) >= 4 )
    {
        if( (R * C - M) % 2 == 0 )
        {
            arrangeByRow(locations, R, C, C*(R-2));
            arrangeByDoubleRow(locations, R, C, M - C*(R-2));
            
            locations[0] = 'c';
            return true;
        }
        
        if( R * C - M == 9 )
        {
            for( int row = 0; row < R; row ++ )
            {
                for( int column = 0; column < C; column ++ )
                {
                    if(! (row < 3 && column < 3) )
                    {
                        locations[row * C + column] = '*';
                    }
                }
            }
            locations[0] = 'c';
            return true;
        }
        
    }
    
    std::cout << "3: R=" << R << ",C=" << C << ",M=" << M << ",R*C-M=" << R*C-M << std::endl;
    return false;
}



void arrangeByRow(char* locations,int R, int C, int M)
{
    locations[0] = 'c';
    
    for( int i = R * C - M; i < R * C; i ++ )
    {
        locations[i] = '*';
    }
    
}


void arrangeByColumn(char* locations,int R, int C, int M)
{
    
    int index = 0;
    
    for( int column = 0; column < C; column ++ )
    {
        for( int row = 0; row < R; row ++ )
        {
            if(index + M < R * C)
            {
                index ++;
            }else
            {
                locations[row * C + column] = '*';
            }
        }
    }
    
    locations[0] = 'c';
}


void arrangeByDoubleRow(char* locations, int R, int C, int M)
{
    for( int i = 0; i < M/2; i ++ )
    {
        locations[ C - i - 1 ] = '*';
        locations[ 2 * C - i - 1 ] = '*';
    }
}



void arrangeByDoubleColumn(char* locations, int R, int C, int M)
{
    for( int i = 0; i < M/2; i ++ )
    {
        locations[ (R - i - 1) * C ] = '*';
        locations[ (R - i - 1) * C + 1 ] = '*';
    }
}

void mineMatrixInit(char* locations, int R, int C)
{
    for( int i = 0; i < R; i ++ )
    {
        for( int j = 0; j < C; j ++ )
        {
            locations[ i * C + j ] = '.';
        }
    }
}