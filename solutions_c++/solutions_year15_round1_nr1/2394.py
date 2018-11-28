#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

    int T;

    cin>>T;

    for(int c=1; c<=T; c++){


        int N;
        cin>>N;

        vector<int> mush(N, 0);

        for(int i=0; i<N; i++){
            cin>> mush[i];
        }

        int min1 = 0;
        int min2 = 0;

        int minrate = 0;


        for(int i=0; i<N;i++){

            if(i+1 < N){

                if(mush[i] > mush[i +1]){

                    min1 += mush[i] - mush[i+1];
                }


                if(mush[i] > mush[i+1]){

                    minrate = max(minrate, (mush[i]-mush[i+1]));
                }

            }






        }


        for(int i=0; i<N-1; i++){

            if(minrate > mush[i]){

                min2 += mush[i];
            } else {
                min2 += minrate;

            }
        }

        cout<<"Case #"<<c<<": "<< min1<< " " << min2 << endl;



    }
    return 0;
}

