#include <cstdlib>
#include <iostream>

using namespace std;

long long  area_c(long long  r1, long long r2){
      return (r2*r2)-(r1*r1);
      }

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    long long  r,t;
    long long  y;
    long long used;
    for (int i=0; i<T;i++){
        cin >> r >> t;
        y = 0;
        while (t > 0) {
             used = area_c(r,r+1);
             if (t>=used) y++;
             t= t-used; 
             r=r+2;
              }
        cout << "Case #" << i+1 << ": " << y << endl;
    }

    return EXIT_SUCCESS;
}
