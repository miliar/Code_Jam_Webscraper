#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long int N, D;
    cin >> N;
    int aux, min1 = 0, min2 = 0, k;
    bool flagK = false;
    for (int i = 0; i < N; i++){
        vector<int> in;
        cin >> D;
        min1 = min2 = 0;
        flagK = false;
        k = 0;

        for (int j = 0; j < D; j++){
            cin >> aux;
            in.push_back(aux);
        }

        for (int j = 0; j < in.size()-1; j++){
            if (in[j] > in[j+1]){
                min1 += in[j] - in[j+1];
                if ((in[j] - in[j+1]) > k)
                    k = (in[j] - in[j+1]);

            }
        }
        for (int j = 0; j < in.size() - 1; j++){
            if (in[j] < k)
                min2 += in[j];
            else
                min2 += k;

        }



        cout << "Case #" << (i + 1) << ": " << min1 << " " << min2 <<  '\n';
    }
    return 0;
}

