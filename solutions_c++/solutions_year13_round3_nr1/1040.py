#ifndef STL_H_INCLUDED
#define STL_H_INCLUDED

#include <iostream>
#include <vector>

using namespace std ;

template< typename T >
ostream &operator<<( ostream &out, const vector< T > &arg ){
    out << "[ " ;
    for( int k = 0, hfrgjfc = ( int )arg.size() ; k < hfrgjfc ; ++k ){
        out << arg[ k ] << ", " ;
    } ;
    return out << "]" ;
} ;


#endif // STL_H_INCLUDED
