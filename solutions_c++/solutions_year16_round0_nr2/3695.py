#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cstdio>
using namespace std;

template <class T>
class PriorityQueue{
    vector<pair<T,int*>> nodes;
    static bool compare(pair<T,int*> a, pair<T,int*> b){ return (*a.second > *b.second); }
public:
    void enqueue(T& s, int* priority){
        nodes.push_back({ s, priority });
        push_heap(nodes.begin(), nodes.end(), compare);
    }
    T dequeue(){
        pop_heap(nodes.begin(), nodes.end(), compare);
        T& ans = nodes.back().first;
        nodes.pop_back();
        return ans;
    }
    bool isEmpty(){ return nodes.empty(); }
};

int heuristic(string state){
    int counter = 0;
    char last = '+';
    int times = 1;
    for(char c : state){
        if(c == '-' && last == '+'){
            counter += times;
            times++;
        }
        last = c;
    }
    return counter;
}

int aStar(string start, string finish){
    unordered_map<string, pair<int,int>> scores;
    scores[start] = {0, heuristic(start)};
    PriorityQueue<string> q;
    q.enqueue(start, &scores[start].second);
    while(!q.isEmpty()){
        string state = q.dequeue();
        if(state == finish) break;
        for(int i=0; i<state.size(); i++){
            string newState = "";
            for(int j=i; j>=0; j--) newState += (state[j]=='+')?'-':'+';
            newState += state.substr(i+1, state.size()-i);
            int count = scores.count(newState);
            if(count == 0){
                int altG = scores[state].first + 1;
                if(count == 0 || altG < scores[newState].first){
                    scores[newState] = {altG, altG + heuristic(newState)};
                    q.enqueue(newState, &scores[newState].second);
                }
            }
        }
    }
    return scores[finish].first;
}

int main(){
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t = 0;
    cin >> t;
    for(int i=0; i<t; i++){
        string plate;
        cin >> plate;
        string finish = "";
        for(int j=0; j<plate.size(); j++) finish += '+';
        int ans = aStar(plate, finish);
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    return 0;
}
