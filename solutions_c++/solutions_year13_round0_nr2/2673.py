#include <iostream>
#include <conio.h>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

int lawn[11][11] ;
int N ;
int rowno ;
string caseout[2] ;
int x,y ;
int flagcorrect = 0 ;


int checkcell(int cell , int a, int b ){

    int rowcheck  = 1 ;
    int colcheck = 1;

    if(cell==1){
        //column check
        for(int i=0 ; i<a ; i++ ){
            if(cell!=lawn[i][b])
                colcheck = 0 ;
        }

        for(int i=a+1 ; i<x ; i++ ){
            if(cell!=lawn[i][b])
                colcheck = 0 ;
        }
        //row check

        for (int j =0; j<b ; j++ )
        {
            if(cell!=lawn[a][j])
                rowcheck = 0 ;
        }

        for (int j =b+1; j<y ; j++ )
        {
            if(cell!=lawn[a][j])
                rowcheck = 0 ;
        }

        if(rowcheck||colcheck)
            return 1 ;
        else
            return 0 ;

    }
    /*
    if(cell==2){
        //column check
        for(int i=a+1 ; i<x ; i++ ){
            if(cell>lawn[i][b])
                colcheck = 0 ;
        }
        //row check
        for (int j =b+1; j<y ; j++ )
        {
            if(cell>lawn[j][b])
                rowcheck = 0 ;
        }

        if(rowcheck||colcheck)
            return 1 ;
        else
            return 0 ;

    }
    */

    return 1 ;

}


int main()
{
    string word ;

    caseout[0] = "NO" ;
    caseout[1] = "YES" ;

    freopen("B-small-attempt1.in", "r", stdin);
    freopen("result.txt", "w", stdout);

    scanf("%d" , &N);

    for(int i=0; i<N ; i++){

        scanf("%d %d" , &x, &y ) ;



        for(int j =0 ; j<x ; j++){

                for(int k =0 ; k < y; k++){

                    scanf("%d" , &lawn[j][k] );
                    //cout<<lawn[j][k] ;
                }
            }

        if(x==1||y==1)
        flagcorrect = 1 ;
        else{

        flagcorrect = 1 ;

        for(int j=0; j<x ; j++){

            for(int k =0 ; k<y ; k++){

                    int result = checkcell(lawn[j][k], j ,k );
                    //cout<<result ;
                    if(result==0)
                    flagcorrect = 0 ;
            }
        }

        }

        cout<<"Case #"<<(i+1)<<": "<<caseout[flagcorrect]<<"\n" ;

    }

    return 0;

}

