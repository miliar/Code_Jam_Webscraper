#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

void negateBit(long long int * n, int bit){
    long long int t = ((*n)>>bit & 1);

    *n -= t<<bit;
    *n += (!t)<<bit;

    return;
}

int main(){
    int T, N, L;
    int i, j, k, t, n, l;

    char TEMP;

    cin >> T;
    for(t=0; t<T; t++){
        cin >> N >> L;
        vector<long long int> outlets;
        vector<long long int> devices;

        //printf("AAAA %d %d %d\n", T, N, L);
        scanf("%c", &TEMP);

        for(n=0; n<N; n++){
            long long int flow = 0;
            char read;

            //printf("READING (%d) ", n);
            for(l=L-1; l>=0; l--){
                scanf("%c", &read);
                flow += ((int)read - '0')<<l;

                //printf("%c", read);
            }
            //printf(" %lld\n", flow);

            scanf("%c", &TEMP);

            outlets.push_back(flow);
        }

        for(n=0; n<N; n++){
            long long int flow = 0;
            char read;

            //printf("READING (%d) ", n);
            for(l=L-1; l>=0; l--){
                scanf("%c", &read);
                flow += ((int)read - '0')<<l;

                //printf("%c", read);
            }
            //printf(" %lld\n", flow);

            scanf("%c", &TEMP);

            devices.push_back(flow);
            //printf(" %lld %lld\n", flow, devices[devices.size()-1]);
        }
        //printf("\n");

        /*for(n=0; n<N; n++)
            printf("%lld %lld\n", outlets[n], devices[n]);*/

        sort(outlets.begin(), outlets.end());
        sort(devices.begin(), devices.end());

        /*for(n=0; n<N; n++)
            printf("%lld %lld\n", outlets[n], devices[n]);*/

        int possible = 1;
        int switches = 0;
        for(l=L-1; l>=0 && possible; l--){
            for(n=0; n<N; n++){
                int out = outlets[n]>>l & 1;
                int dev = devices[n]>>l & 1;

                //printf("Bit %d of index %d: (%lld) out %d & %d dev (%lld)\n", l, n, outlets[n], out, dev, devices[n]);

                if(dev != out){
                    for(n=0; n<N; n++)
                        negateBit(&outlets[n], l);


                    switches++;

                    sort(outlets.begin(), outlets.end());
                    sort(devices.begin(), devices.end());

                    for(n=0; n<N; n++){
                        int out = outlets[n]>>l & 1;
                        int dev = devices[n]>>l & 1;
                        //printf("    NOT Bit %d of index %d: (%lld) out %d & %d dev (%lld)\n", l, n, outlets[n], out, dev, devices[n]);

                        if(dev != out){
                            possible = 0;
                            break;
                        }
                    }

                    break;
                }
            }

            sort(outlets.begin(), outlets.end());
            sort(devices.begin(), devices.end());
        }

        if(possible)
            printf("Case #%d: %d\n", t+1, switches);
        else
            printf("Case #%d: NOT POSSIBLE\n", t+1);
    }

    return 0;
}
