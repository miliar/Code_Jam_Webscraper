#include <iostream>
#include <sstream>
#include <map>
#include <vector>
#include <list>
#include <fstream>
#include <algorithm>
#include <iomanip>   

using namespace std;
typedef unsigned int uint;



int pop_front(vector<double> &vec) {
    for (int i = 1; i < vec.size(); i++) {
        vec[i-1] = vec[i];
    }
    vec.pop_back();
}

int remove(vector<double> &vec, int index) {
    for (int i = index + 1; i < vec.size(); i++) {
        vec[i-1] = vec[i];
    }
    vec.pop_back();
}


double OtherMove(vector<double> &other, double me) {
       
    int i = 0;
    
    while (i < other.size() && other[i] < me)
        i++;
    
    int move = i == other.size() ? 0 : i;
    
    double ret = other[move];
    remove(other, move);
    
    return ret;
}

int PlayCheat(vector<double> me, vector<double> other, int aantal) {
    int score = 0;
    
    for (int i = 0; i < aantal; i++) {
        if (me.front() > other.front()) {
            pop_front(other);
            pop_front(me);
            score++;
        } else {
            other.pop_back();
            pop_front(me);
        }
    }
    
    return score;
}


int PlayNormal(vector<double> me, vector<double> other, int aantal) {
    int score = 0;
    
    for (int i = 0; i < aantal; i++) {
        double me_move = me.back();
        double other_move =  OtherMove(other, me_move);
        me.pop_back();
        
        if (me_move > other_move)
            score++;
    }
    
    return score;
}

void solve(istream& is, uint index)
{
    double aantal_stenen;
    is >> aantal_stenen;
    
    vector<double> me; vector<double> other; 
    for (int i = 0; i < aantal_stenen; i++){
        double t;
        is >> t;
        me.push_back(t);
    }
    
    for (int i = 0; i < aantal_stenen; i++){
        double t;
        is >> t;
        other.push_back(t);
    }
    
    sort(me.begin(), me.end());
    sort(other.begin(), other.end());

    int cheatscore = PlayCheat(me, other, aantal_stenen);
    int normalscore = PlayNormal(me, other, aantal_stenen);
    
    cout << "Case #" << index << ": " << cheatscore << " " << normalscore << endl;
}

void oef(istream& is)
{
    uint n;
    is >> n;
    for(uint i = 0;i < n; i++)
        solve(is, i+1);
}

#define EIGENTEST 1

int main()
{
    ifstream myfile ("/home/thomas/Downloads/D-large.in");
    
    if (myfile.is_open())
    {
        oef(myfile);
        
        myfile.close();
    }
    
    return 0;
}

