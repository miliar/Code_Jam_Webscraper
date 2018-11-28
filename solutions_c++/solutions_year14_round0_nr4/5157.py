#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

bool comp( float a, float b ) { return a > b; }

int main()
{
    int n,
        T, ctr = 1,
        i, j, k,
        z, y;
    vector <float> naomi, ken,
                   n1, k1;
    float a;
    
    ifstream fin( "input.txt" );
    ofstream fout( "output.txt" );
    
    fin >> T;
    
    while( ctr <= T )
    {
           naomi.clear();
           ken.clear();
           n1.clear();
           k1.clear();
           z=0;
           y=0;
           
           fin >> n;
           for( i=0; i<n; i++ )
           {
                fin >> a;
                naomi.push_back(a);
           }
           for( i=0; i<n; i++ )
           {
                fin >> a;
                ken.push_back(a);
           }
           
           sort( naomi.begin(), naomi.end(), comp );
           
           sort( ken.begin(), ken.end(), comp );
           
           n1 = naomi;
           
           k1 = ken;
           
           // for deceitful
           for( i=0; i<n; i++ )
           {
                for( j=0; j<n; j++ )
                {
                     if( n1[i] > k1[j] && k1[j] != 0 )
                     {
                         n1[i] = 0;
                         k1[j] = 0;
                         y++;
                         break;
                     }
                }
            }
            // For Sincere
            for( i=0; i<n; i++ )
            {
                 k=0;
                 for( j=0; j<n; j++ )
                 {
                      if( naomi[i] < ken[j] )
                      {
                          k = 1;
                          break;
                      }
                 }
                      if( k==1 )
                      {
                          if( ken[j] != 0 )
                          {
                           naomi[i] = 0;
                           ken[j] = 0;
                          }
                      }
                      else
                          z++;
             }
            
            fout << "Case #" << ctr++ << ": " << y << ' ' << z << '\n';
    }
}
