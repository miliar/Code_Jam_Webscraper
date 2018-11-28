#include <cstdlib>
#include <iostream>
#include "set"
#include <math.h> 

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	int y;
	int D;
	int DD[1001];
	int x;
	long Tot;
	long Pwr;
	int lvl;
    for (int T_i=0; T_i<T;T_i++){
        cin >> D;
        Tot = 0;
        lvl=0;
        y=0;
        for (int D_i=0; D_i<1001; D_i++){
            DD[D_i] = 0;
        };
        
        int Max_n;
        int Max_v;
        int Tgt_v;
        int Max_x;
        
        Max_x =0;
        Max_n=0;
        Max_v =0;
        Tgt_v = 0;
        for (int D_i=0; D_i<D; D_i++){
            cin >> x;
            DD[x] += 1;
            if (Max_x < x) Max_x = x;
            if (x>1) {
            if (Max_n < DD[x]) {
                Max_n = DD[x];
                Max_v = x;
            } else {
                if ((Max_n== DD[x]) && (Max_v < x)){
                    Max_n = DD[x];
                    Max_v = x;
                }
            }}
        };
        
        int b;
        int MinX;
        int Min2X;
        int Tgt2_v;

int Maxxx;
int xxxx;
if (Max_v >0) {

        MinX = Max_x;

        for (b=2;b<1001;b++){
              Tgt_v = b;
              Min2X = 0;
              Maxxx = 0;
                for (int D_i=0; D_i<1001; D_i++){
                    if (DD[D_i] > 0) {
                       xxxx= (ceil((float)D_i / Tgt_v)-1) * DD[D_i];
                       if (xxxx== 0){
                                  if (Maxxx < D_i) Maxxx = D_i;
                                  }
                       else {
                            if (Maxxx < Tgt_v) Maxxx = Tgt_v;
                            }
                       Min2X += xxxx ;
                       
                    }
                }
              Min2X += Maxxx;
              if (Min2X>0)
              if (Min2X < MinX) MinX= Min2X;
        }
        y = MinX;
} else {
       y= Max_x;
}
        cout << "Case #" << T_i+1 << ": " << y << endl;
    }
    return EXIT_SUCCESS;
}
