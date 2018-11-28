#include <iostream>
#include <string>
#include <math.h>
#include <sstream>


using namespace std;

int main()
{
    int number,a,b,high;

    cin >> number;
    for(int i = 0; i < number; ++i){
        cin >> a >> b;
        int desired[a][b];
        for(int x = 0; x < a; ++x){
            for(int y = 0; y < b; ++y){
                cin >> desired[x][y];
            }
        }
        high = desired[0][0];
        int low = desired[0][0];
        for(int x = 0; x < a; ++x){
            for(int y = 0; y < b; ++y){
                if(desired[x][y] > high){
                    high = desired[x][y];
                }
                if(desired[x][y] < low){
                    low = desired[x][y];
                }
            }
        }

        int start[a][b];
        for(int y = 0; y < b; ++y){
            for(int x = 0; x < a; ++x){
                start[x][y] = high;
            }
        }

        for(int h = low; h < high; ++h){
            int x_works[a];
            for(int abc = 0; abc < a; ++abc){
                x_works[abc] = 0;
            }
            for(int x = 0; x < a; ++x){
                if(desired[x][0] == low){
                    bool line_works = true;
                    for(int y = 0; y < b; ++y){
                        if(desired[x][y] != low){
                            line_works = false;
                        }
                    }
                    if(line_works){
                        x_works[x] = 1;
                    }else{
                        x_works[x] = 0;
                    }
                   /* for(int y = 0; y < b && line_works; ++y){
                        desired[x][y]++;
                    }*/
                }
            }

            int y_works[a];
            for(int abc = 0; abc < b; ++abc){
                y_works[abc] = 0;
            }
            for(int y = 0; y < b; ++y){
                if(desired[0][y] == low){
                    bool line_works = true;
                    for(int x = 0; x < a; ++x){
                        if(desired[x][y] != low){
                            line_works = false;
                        }
                    }
                    if(line_works){
                        y_works[y] = 1;
                    }else{
                        y_works[y] = 0;
                    }
                }
            }
            for(int y = 0; y < b; ++y){
                for(int x = 0; x < a && y_works[y]; ++x){
                    desired[x][y] = h+1;
                }
            }
            for(int x = 0; x < a; ++x){
                for(int y = 0; y < b && x_works[x]; ++y){
                    desired[x][y] = h+1;
                }
            }
        }

        bool works = true;
        for(int x = 0; x < a; ++x){
            for(int y = 0; y < b; ++y){
                if(start[x][y] != desired[x][y]){
                    works = false;
                    //break;
                }
            }
        }


        cout << "Case #" << i+1 << ": ";
        if(works){
            cout << "YES";
        }else{
            cout << "NO";
        }
        cout << endl;
    }
    return 0;
}
