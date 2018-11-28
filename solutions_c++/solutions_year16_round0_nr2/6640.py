#include <iostream>
#include <vector>
using namespace std;


int main()
{

    int t; cin >> t;

    for(int T = 1; T <= t; T++){

        int ans = 0;

        string w; cin >> w;

        vector<int> pancakes;

        int zeroes = 0;
        for(int i = 0; i < w.length(); i++)
        {
            if(w[i] == '+')
                pancakes.push_back(1);
            else{
                pancakes.push_back(0);
                zeroes++;
            }
        }

        while(pancakes.back() == 1 && !pancakes.empty()){
            pancakes.pop_back();
        }

        if(zeroes < pancakes.size() ){

            int e;
            for(int i = 0 ; i < pancakes.size(); i = e){

                e = i;

                if(i && pancakes[i] != pancakes[i - 1] ){
                    ans += 2;
                 //   cout << i << " COUNTED FOR" << endl;
                }

                while(pancakes[i] == pancakes[e] && e < pancakes.size()){

                  //  if(i) pancakes[e] = pancakes[i - 1];
                     e++;
                }

                for(int j = i; j < e && i; j++)
                    pancakes[j] = pancakes[i - 1];
            }


        }

        if(pancakes[0] == 0) ans++;

        cout  << "Case #" << T << ": " << ans << endl;
    }
    return 0;
}
