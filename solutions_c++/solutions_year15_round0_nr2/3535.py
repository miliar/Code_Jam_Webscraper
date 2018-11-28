#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int T;
    cin>>T;

    for(int c=1; c<=T; c++){


        int D;
        cin>>D;

        vector<int> cakes(D, 0);

        for(int i=0; i<D; i++){

            cin>>cakes[i];
        }

        sort(cakes.begin(), cakes.end());


        int min_minutes = cakes[D-1];

        int first_min = min_minutes;



        for(int t=1; t< first_min-1; t++ ){

            int cur_min = t;

            if(t+1 >= min_minutes){
                break;
            }


            for(int i=0; i<D; i++){

                if(cakes[i] <= t){
                    continue;
                }


                int num_mov = (cakes[i]/t -1) + min(1,cakes[i]%t);

                cur_min += num_mov;

                if(cur_min >= min_minutes){

                    break;
                }

            }

            if(cur_min < min_minutes){

                min_minutes = cur_min;
            }



        }


        cout<<"Case #"<<c<<": "<< min_minutes <<endl;


    }
    return 0;
}

