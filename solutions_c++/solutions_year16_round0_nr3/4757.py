#include <iostream>
#include<fstream>
#include<vector>
#include<string>
#include<cmath>
using namespace std;

int main(int argc, char *argv[])
{
    ifstream inputfile;
    ofstream outputfile;
    string fileName;
    int amount = 0;
    int amount1 = 1;
    int tempnum = 0;
    int tempnum1 = 0;
    long long int tempnum2 = 0;
    // int tempnum3 = 0;
    bool prime = true;
    bool jam = true;
    bool error = true;
    int i = 0;
    long long int j = 0;
    int n = 0;
    int l = 0;
    int k = 0;
    if ( argc == 2)
    {
        fileName = argv[1];
    }
    else 
    {
        cout << "Error - too many inputs" << endl;
        return 1;
    }
    
    inputfile.open(fileName.c_str(), ifstream::in);
    
    fileName.resize( fileName.size() - 3 );
    fileName = (fileName + ".out");
    
    outputfile.open(fileName.c_str(), ofstream::out);
    
    if (!inputfile.is_open()) 
    {
        cout << "Error - inputfile not opened." << endl;
        return 1;
    }
    if (!outputfile.is_open()) 
    {
        cout << "Error - outputfile not opened." << endl;
        return 1;
    }
    
    inputfile >> amount;
    
    while ( !inputfile.eof())
    {
        outputfile << "Case #" << amount1 << ": " << endl;
        inputfile >> tempnum;
        inputfile >> tempnum1;
        vector <int> vec (tempnum, 0);
        vector <int> vec1 (11, 0);
        vec.at(0) = 1;
        vec.at( tempnum - 1) = 1;
    

        
        while ( tempnum1 > 0 && error == true )
        {
            

            
            
            i = 2;
            jam = true;
            for ( unsigned y = 0 ; y < vec1.size() ; y++)
            {
                vec1.at(y) = 0;
            }
            while ( i <= 10)
            {
                prime = true;
                tempnum2 = 0;
                
                for ( k = 0 ; k < tempnum ; k++)
                {
                    if(vec.at(k) == 1)
                    {
                        tempnum2 = tempnum2 + pow(i,k);

                    }
                }
                j = 2;

                
                while ( j < 1000 && prime == true)
                {    
                    if( tempnum2 % j == 0 )
                    {
                        prime = false;
                        vec1.at(i) = j;
                    }
                    j++;
                }

                if( prime)
                {
                    jam = false;
                }
                i++;            
            }
            
            
            if ( jam )
            { 
                for( unsigned z = vec.size() - 1; z > 0 ; z--)
                {
                    outputfile << vec.at(z) ;
                }
                
                outputfile << vec.at(0) << " ";
                
                for( unsigned z = 2; z <= 10 ; z++)
                {
                    outputfile << vec1.at(z) << " " ;
                }
                outputfile << endl;
                
                tempnum1--;
            }

                
            // if( jam == 1 )
            // {
                
            //     for ( int z = tempnum  - 1 ; z >= 0 ; z--)
            //     {   
            //         outputfile << vec.at(z) ;
            //     }
                
            //     i = 2;
            //     while ( i <= 10)
            //     {
                
            //         tempnum2 = 0;
                    
            //         for ( k = 0 ; k < tempnum ; k++)
            //         {
            //             if(vec.at(k) == 1)
            //             {
            //                 tempnum2 = tempnum2 + pow (i,k);
            //             }
            //         }
                    
            //         // cout << tempnum2 << " ";
            //         j = 2;
            //         while ( j < tempnum2/2 && j > 0)
            //         {    
            //             if( tempnum2 % j == 0 )
            //             {
            //                 outputfile << " " << j ;
            //                 j = -100;
            //             }
            //             j++;
            //         }
                
                
            //         i++;
            //     }
                
            //     // cout << endl;
            //     outputfile << endl;
            //     tempnum1--;
            // }
            
            i = 0;
            for( unsigned z = 0; z < vec.size() ; z++)
            {
                if ( vec.at(z) == 0)
                {
                    i = 1;
                }
            }
            
            if ( i == 0)
            {
                error = false;
            }
                
                
                
            n = 1;
            l = 0;
            while ( n < tempnum - 1 && l == 0)
            {
                if( vec.at(n) == 1)
                {
                }
                else
                {
                    for ( int m = 1; m <= n ; m++)
                    {
                        vec.at(m) = 0;
                    }
                    vec.at(n) = 1;
                    l = 1;
                }
                
                
                n++;
            }
                
                
            // for( unsigned z = 0; z < vec.size() ; z++)
            // {
            //     cout << vec.at(z) ;
            // }
            // cout << endl;
    
        }



    }
    
    
    
    // cout << tempnum << endl;
    // cout << tempnum1 << endl;
    
    inputfile.close();
    outputfile.close();
    
    return 0;
}