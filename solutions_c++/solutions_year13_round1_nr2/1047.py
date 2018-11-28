#include <cstdlib>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;
    long long E,R,N;
    long NN[10000];
    long EE[10000];
    long RR[10000];
    long YY[10000];
    int y;
    
    int curr;
    int doloop;

    for (int i=0; i<T;i++){
        cin >> E >> R >> N;
        for (int j=0; j < N; j++){
            cin >> NN[j];
            EE[j] = -1;
            RR[j] = 0;
            YY[j] - 0;
        }

        y= -1;
        curr = 0;
        while (curr >= 0 ) {
              if (EE[curr] == -1) {
                           if (curr==0) {EE[curr] = E;RR[curr] = R;} else {EE[curr]= RR[curr-1]; RR[curr] = R;};
                           if (RR[curr] > E) RR[curr] = E;
                           if (curr==0) 
                              YY[curr] = EE[curr] * NN[curr];
                           else
                              YY[curr] = YY[curr-1]+ ( EE[curr] * NN[curr]);
                           }
              else {
                     if (EE[curr]>0) {
                        EE[curr] --; EE[curr+1]=-1; RR[curr] = R;
                        if (curr>0) RR[curr] = RR[curr] + RR[curr-1] - EE[curr]; 
                        else RR[curr] = RR[curr] + E - EE[curr]; 
                           if (RR[curr] > E) RR[curr] = E;
                           if (curr==0) 
                              YY[curr] = EE[curr] * NN[curr];
                           else
                              YY[curr] = YY[curr-1]+ ( EE[curr] * NN[curr]);
                        
                      } else {EE[curr]=-1;curr = curr-2;}
              }
              curr++;
              if (curr==N) {
                if (y==-1) {y = YY[N-1];} else {
                    if (y< YY[N-1]) y=YY[N-1];
                    }
                curr--;
              }
        }
        

        cout << "Case #" << i+1 << ": " << y << endl;
    }
    return EXIT_SUCCESS;
}
