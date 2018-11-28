#include<iostream>
#include<fstream>

using namespace std;


int main(void)
{
    ifstream fin ;
    ofstream fout;
    fout.open("A-small-attempt5.txt");
    fin.open("A-small-attempt5.in");
 int T;
 fin >> T;//test cases
int count = 0;
 int arr1[4][4];
 int arr2[4][4];
 int row1;

 int row2;
 int answer;

 for ( int i = 0 ; i < T  ; i++ )
 {

        fin >> row1;//3
        row1--;
        for ( int k = 0 ; k < 4 ; k++ )
            {
                for ( int j =0 ; j < 4 ; j++ ){
                    fin >> arr1[k][j];
                }
            }

        fin >> row2;//3
        row2--;

         for ( int k = 0 ; k < 4 ; k++ )
            {
                for ( int j =0 ; j < 4 ; j++ ){
                    fin >> arr2[k][j];
                }
            }


        count = 0;
        for ( int l = 0; l < 4;l++ )
        {
            for( int n = 0 ; n < 4 ; n++)
            {
                if( arr1[row1][l] == arr2[row2][n] )
                {
                    count++;
                    answer = arr2[row2][n];
                    //cout << answer << endl;
                }
            }
        }


            if( count == 1){
                fout << "Case #" <<i+1 << ": " << answer << endl;
            }else if( count > 1 ){
                fout << "Case #" << i+1<< ": " << "Bad magician!" << endl;
            }else{
                fout << "Case #" << i+1 << ": "  << "Volunteer cheated!" << endl;
            }


 }


return 0;
}
