#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

bool compare(double a, double b) {
    double e = 0.000001;
    if((b-a) > e)  return true;
    return false;
}


int main()
{
    int t;
    cin>>t;

    for (int k = 0; k<t; k++){
        vector<double> her, him;
        double temp;
        int N,i, I, j;
        double ep = 0.000001;
        cin>>N;

        for(i = 0; i<N; i++) {
            cin>>temp;
            her.push_back(temp);
        }
        for(i=0;i<N;i++){
            cin>>temp;
            him.push_back(temp);
        }

        sort(her.begin(), her.end(), compare);
        sort(him.begin(), him.end(), compare);
/*
        for(i = 0; i<N; i++) {
            cout<<her[i]<<",";
        }
        cout<<endl;
        for(i = 0; i<N; i++) {
            cout<<him[i]<<",";
        }
        cout<<endl;
*/

        //deceitfull war
        int d_score = 0;
        for(i =0;i<N;i++){
            if (!compare(her[i], him[0])) break;
        }

        I = i;
        j = 0;
        for(i = I; i <N; i++) {
            if(!compare(her[i], him[j])){
               d_score++;
               j++;
            }
        }

        //war
        int w_score = 0;
        int him_s = 0, him_e = N-1;
        for(i = N-1; i>=0; i--) {
            if(!compare(her[i], him[him_e])){
                him_s++;
                w_score++;
            }
            else {
                him_e--;
            }
        }

        cout<<"Case #"<<k+1<<": "<<d_score<<" "<<w_score<<endl;
    }
    getchar();
    return 0;
}
