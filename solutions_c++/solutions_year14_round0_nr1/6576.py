//
//  main.cpp
//  MagicTrick
//
//  Created by Stoica Alexandru on 4/12/14.
//  Copyright (c) 2014 Stoica Alexandru. All rights reserved.
//

#include <cstdio>

int f[20];

int main(int argc, const char * argv[])
{

    int T ;
    int i , j ;

    freopen ( "/Users/alexstoick/Desktop/MagicTrick/MagicTrick/date.in" , "r" , stdin ) ;
    freopen ( "/Users/alexstoick/Desktop/MagicTrick/MagicTrick/date.out" , "w" , stdout ) ;

    scanf ( "%d" , & T ) ;
    for ( int test = 0 ; test < T ; ++ test )
    {

        int first_answer ;
        int second_answer ;
        int temp ;
        for ( i = 1 ; i < 17 ; ++ i )
            f[i] = 0 ;
        
        scanf ( "%d" , &first_answer ) ;
        --first_answer ;
        for ( i = 0 ; i < 4 ; ++ i )
            for ( j = 0 ; j < 4 ; ++ j )
                if ( i == first_answer)
                {
                    scanf ( "%d" , & temp ) ;
                    ++ f[temp] ;
                }
                else
                    scanf ( "%d" , & temp ) ;

        scanf ( "%d" , & second_answer ) ;
        --second_answer ;
        for ( i = 0 ; i < 4 ; ++ i )
            for ( j = 0 ; j < 4 ; ++ j )
                if ( i == second_answer )
                {
                    scanf ( "%d" , & temp ) ;
                    ++ f[temp] ;
                }
                else
                    scanf ( "%d" , & temp ) ;

        int number = -1 ;
        int appearances = 0 ;

        for ( i = 1 ; i < 17 ; ++ i )
        {
            if ( f[i] == 2 )
            {
                number = i ;
                ++ appearances ;
            }
        }
        
        printf ( "Case #%d: " , test + 1 ) ;

        if ( appearances >= 2 )
        {
            printf( "Bad magician!" ) ;
        }
        else if ( appearances == 1 )
        {
            printf( "%d" , number ) ;
        }
        else if ( appearances == 0 )
        {
            printf ( "Volunteer cheated!" ) ;
        }
        printf ( "\n" ) ;
    }

}

