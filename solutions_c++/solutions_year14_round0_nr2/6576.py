//
//  main.cpp
//  CookieClicker
//
//  Created by Stoica Alexandru on 4/12/14.
//  Copyright (c) 2014 Stoica Alexandru. All rights reserved.
//

#include <cstdio>

int main(int argc, const char * argv[])
{

    int T ;
    
    freopen ( "/Users/alexstoick/Desktop/CookieClicker/CookieClicker/date.in" , "r" , stdin ) ;
    freopen ( "/Users/alexstoick/Desktop/CookieClicker/CookieClicker/date.out" , "w" , stdout ) ;
    
    scanf ( "%d" , & T ) ;
    
    for ( int test = 0 ; test < T ; ++ test )
    {
        
        double C , F , X ;
        double time = 0 ;
        double cookies_per_sec = 2 ;
        
        scanf ( "%lf%lf%lf" , & C , & F , & X ) ;
        
        bool final = false ;
        
        while ( ! final )
        {
            //decide if we want to upgrade
            
            double time_to_upgrade = C / cookies_per_sec ;
            double time_to_X_with_upgrades = time_to_upgrade +
                X / (cookies_per_sec + F ) ;
            double time_to_X = X / cookies_per_sec ;
            
            if ( time_to_X < time_to_X_with_upgrades )
            {
                time += time_to_X ;
                final = true ;
            }
            else
            {
                time += time_to_upgrade ;
                cookies_per_sec += F ;
            }
        }
        
        printf ( "Case #%d: %.7f\n" , test + 1 , time ) ;
        
    }
    
    return 0 ;
}

