#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main ( ){
    ifstream fin ( "B-large.in" );
    ofstream fout ( "file2.txt" );
    int test;
   	fin >> test;
    double C , F , X;
    double result1 , result2;
    for ( int i=1 ; i <= test ; i++ ){
        result1 = 0;
        double time = 0;
        double cookie_per_sec = 2;
        fin >> C;
        fin >> F;
        fin >> X;
        //cout<<X<<endl;
        if ( X <= C ){
        result1 = X / cookie_per_sec;
        
        }
        else{
            do{
            	result1=time+X/cookie_per_sec;
            	result2=time+C/cookie_per_sec+(X/(cookie_per_sec+F));	
            	time+=C/cookie_per_sec;
            	cookie_per_sec+=F;
            }while (result2<=result1);			
        }
       // cout << "Case #" << testcase << ": " << fixed << setprecision(7) << result1 << endl;
        fout << "Case #" << i << ": " << fixed << setprecision(7) << result1 << endl;
    }
}
