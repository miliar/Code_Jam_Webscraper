#include <iostream>
#include <vector>

using namespace std;

int main(){
    int T;
    int N;
    vector<double> x1;
    vector<double> y1;
    double tmp;
    cin >> T;
    for (int t1 = 1 ;  t1 <= T ; t1++){
        cin >> N;
        x1.clear();
        y1.clear();
        for (int i = 0 ; i < N ; i++){
            cin >> tmp;
            x1.push_back(tmp);
        }
        for (int i = 0 ; i < N ; i++){
            cin >> tmp;
            y1.push_back(tmp);
        }
        sort(x1.begin(), x1.end());
        sort(y1.begin(), y1.end());
        
        /*
        for (int i = 0 ; i < N ; i++){
            cout << x1[i] << " " << y1[i] << endl;
        }
        */
        
        int max = 0;
        int larger = 0;
        int i, j;
        for (i = N - 1 ; i >= 0 ; i--){
            for (j = N - 1 ; j >= 0 ; j--){
                if (x1[i] > y1[j])
                    break;
            }
            larger = j - i + 1;
            if (larger > max)
                max = larger;
            //cout << larger << endl;
        }
        int count = 0;
        int sentry = 0;
        for (i = 0 ; i < N ; i++){
            for (j = 0 ; j < N ; j++){
                if (x1[i] < y1[j])
                    break;
            }
            if (j > sentry){
                count++;
                sentry++;
            }
        }
        cout << "Case #" << t1 << ": " << count << " "<< max << endl;
        /*
        for (j = 0 ; j < N ; j++){
            for (i = 0 ; i < N  ; i++){
                if (x1[i] > y1[j])
                    break;
            }
            
            larger = i - j + 1;
            cout << j << " " << i << endl;
            //if (larger > max)
            //    max = larger;
            //cout << larger << endl;
        }
        */
        
        
        //cout << "MAX" << max << endl;
    }
    return 0;
}