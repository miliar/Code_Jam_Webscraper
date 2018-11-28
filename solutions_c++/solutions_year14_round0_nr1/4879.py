#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>

#define MAX 100
#define test(a) cout << "TEST " << a << endl;
#define go(a,b) for(int a=0; a<b; a++)
#define case(a) fout << "Case #"<< a << ": " <<
using namespace std;




int main()
{

    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int n,i,j;
   fin >> n;
   go(a,n){
        int array[4][4];
        int brray[4][4];

        fin >> i;
        go(b,4){
            go(c,4){
                fin >> array[b][c];
            }
        }
        fin >> j;
        go(b,4){
            go(c,4){
                fin >> brray[b][c];
            }
        }
        int counter=0;
        int value=0;
         go(b,4){
            go(c,4){
                if(array[i-1][b]==brray[j-1][c]){
                    counter++;
                    value=array[i-1][b];
                }
            }
         }
         if(counter==0){
            case(a+1) "Volunteer cheated!" << endl;
         }
         if(counter==1){
            case(a+1) value << endl;
         }
         if(counter>1){
            case(a+1) "Bad magician!"  << endl;
         }


   }

}
