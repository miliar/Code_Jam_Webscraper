#include <iostream>
#include <cstdio>
#include <algorithm>

using namespace std;

vector<int> v;
int minimum = 1000000000;

void recurse(int steps){
    //cout << "START!\nMINI=" << minimum << ", steps: " << steps << "\nINPUT CHARACTER!";
    //int c;
    //cin >> c;
    //cout << "v: ";
    //for(unsigned int i = 0; i < v.size(); i++){
    //    cout << v[i] << " ";
    //}
    //cout << "\n";

    bool cool=true;
    for(unsigned int i = 0; i < v.size(); i++){
        if(v[i]>0){
            cool=false;
            break;
        }
    }
    if(cool){
        //cout << "COOL!\n";
        minimum = min(steps, minimum);
        return;
    }

    //cout << "NOT COOL!\n";

    for(unsigned int i = 0; i < v.size(); i++){
        //if(v[i]>0){
        v[i]--;
        //}
    }
    //cout << "STARTING RECURSION NUMBER 1!\n";
    recurse(steps+1);
    for(unsigned int i = 0; i < v.size(); i++){
        //if(v[i]>=0){
        v[i]++;
        //}
    }
    int maxi = 0, maxiIdx = 0;
    for(int i = 0; i < v.size(); i++){
        if(v[i] > maxi){
            maxi = v[i];
            maxiIdx=i;
        }
    }
    //cout << "ENDING RECURSION NO 1!\n";
    //cout << "STARTING RECURSION NUMBER 2!\n";

    if(maxi==1){
        //cout << "MAXI==1\n";
        minimum=min(minimum, steps+1);
        return;
    }
    if(maxi<=0){
        //cout << "MAXI==0\n";
        minimum=min(minimum, steps);
        return;
    }

    //for(unsigned int i = 0; i < v.size(); i++){
    //    cout << v[i] << " ";
    //}
    v[maxiIdx] = maxi/2;
    v.push_back(maxi/2 + maxi%2);
    //cout << "\n";
    recurse(steps+1);
    v.pop_back();
    v[maxiIdx]=maxi;
    //cout << "ENDING RECURSION NO 2!\n";
}

int Go(){
    v.clear();
    minimum = 1000000000;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++){
        int x;
        cin >> x;
        v.push_back(x);
    }
    recurse(0);
    return minimum;
}

int main(){
    int t;
    cin >> t;
    for(int qwe = 0; qwe < t; qwe++){
        int res = Go();
        printf("Case #%d: %d\n", qwe+1, res);
    }
}
