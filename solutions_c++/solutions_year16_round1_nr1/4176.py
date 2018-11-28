#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

vector<char> solve(char* start, char * end);

int main() {
    int T = 0;
    cin >> T;
    char buf[1001] = {};
    cin.getline(buf, 1001);
    //printf("%s\n",buf);

    for(int i = 1; i <= T; ++i){
        cin.getline(buf, 1001);
        //printf("%s\n",buf);
        vector<char> solution = solve(buf, buf + strlen(buf));
        //printf("%s\n",buf);
        cout << "Case #" << i << ": ";
        for(const auto& c : solution){
            cout << c;
        }
        cout << endl;
    }
}

vector<char> solve(char* start, char* end){
    if(start == end){
       return vector<char>();
    }
    char* biggest = start;
    //cout << *start  << *(end - 1)<< endl;
    for(char* c = start; c != end; ++c){
        if((*c) >= (*biggest)) biggest = c;
        //cout << *c;
    }
    //cout << *start  << *(end - 1)<< endl;
    vector<char> solution = solve(start, biggest);
    solution.insert(solution.begin(),*biggest);
    ++biggest;
    for(char* c = biggest; c!= end; ++c){
        solution.push_back(*c);
    }
    return solution;
}

